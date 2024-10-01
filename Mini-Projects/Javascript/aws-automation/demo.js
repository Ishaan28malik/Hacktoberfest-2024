const AWS = require('aws-sdk');
AWS.config.loadFromPath('config.json');
const autoscaling = new AWS.AutoScaling();
const cloudwatch = new AWS.CloudWatch();
const elbv2 = new AWS.ELBv2();

const config = {
  loadBalancer: {
    name: 'load-balancer',
    ARN: null,
    reference: null
  },
  targetGroup: {
    name: 'target-group',
    ARN: null
  },
  autoScaling: {
    launchConfigName: 'autoScalingLaunchConfig',
    groupName: 'autoScalingGroup'
  },
  aws: {
    key: 'springapp',
    securityGroupID: 'sg-0fcaf7e6d2577dbe1',
    AMI_ID: process.argv[2]
  },
  iam: {
    s3BucketRole: 'ReadOnlyAccessS3'
  }
};

createLoadBalancer = () => {
  const params = {
    Name: config.loadBalancer.name,
    SecurityGroups: ['sg-0fcaf7e6d2577dbe1'],
    Subnets: ['subnet-91a5f5cd', 'subnet-a3491ec4']
  };
  elbv2.createLoadBalancer(params, createLoadBalancerCB);
};
createLoadBalancerCB = (err, data) => {
  if (err) console.log('Creation of Load Balancer Failed! ', err, err.stack);
  else {
    config.loadBalancer.ARN = data.LoadBalancers[0].LoadBalancerArn;
    const splitARN = config.loadBalancer.ARN.split('/');
    const id = splitARN[splitARN.length - 1];
    config.loadBalancer.reference = `app/${config.loadBalancer.name}/${id}`;
    console.log('Loadbalancer Created\n', data);
    createTargetGroup();
  }
};

createTargetGroup = () => {
  const params = {
    Name: config.targetGroup.name,
    Port: 8080,
    Protocol: 'HTTP',
    VpcId: 'vpc-4d0c6f37'
  };
  elbv2.createTargetGroup(params, createTargetGroupCB);
};

createTargetGroupCB = (err, data) => {
  if (err) console.log('Creation of Target Group Failed! ', err, err.stack);
  else {
    console.log('Target Group Created!\n', data);
    config.targetGroup.ARN = data.TargetGroups[0].TargetGroupArn;
    modifyTargetGroupAttributes();
  }
};

modifyTargetGroupAttributes = () => {
  const params = {
    Attributes: [
      {
        Key: 'deregistration_delay.timeout_seconds',
        Value: '0'
      },
      {
        Key: 'stickiness.enabled',
        Value: 'true'
      }
    ],
    TargetGroupArn: config.targetGroup.ARN
  };
  elbv2.modifyTargetGroupAttributes(params, modifyTargetGroupAttributesCB);
};

modifyTargetGroupAttributesCB = (err, data) => {
  if (err)
    console.log(
      'Modification of Target Group Attribute Failed! ',
      err,
      err.stack
    );
  else {
    console.log('Target Group Attribute Modified!\n', data);
    createListener();
  }
};

createListener = () => {
  const params = {
    DefaultActions: [
      {
        TargetGroupArn: config.targetGroup.ARN,
        Type: 'forward'
      }
    ],
    LoadBalancerArn: config.loadBalancer.ARN,
    Port: 8080,
    Protocol: 'HTTP'
  };
  elbv2.createListener(params, createListenerCB);
};

createListenerCB = (err, data) => {
  if (err) console.log('Creation of Listener Failed! ', err, err.stack);
  else {
    console.log('Listener Created!\n', data);
    createAutoScalingLaunchConfig();
  }
};

createAutoScalingLaunchConfig = () => {
  const params = {
    ImageId: config.aws.AMI_ID,
    InstanceType: 't2.micro',
    LaunchConfigurationName: config.autoScaling.launchConfigName,
    SecurityGroups: [config.aws.securityGroupID],
    KeyName: config.aws.key,
    IamInstanceProfile: config.iam.s3BucketRole
  };

  autoscaling.createLaunchConfiguration(params, createLaunchConfigurationCB);
};

createLaunchConfigurationCB = (err, data) => {
  if (err)
    console.log(
      'Creation of AutoScaling Launch Config Failed! ',
      err,
      err.stack
    );
  else {
    console.log('AutoScaling Launch Config Created\n', data);
    createAutoScalingGroup();
  }
};

createAutoScalingGroup = () => {
  const params = {
    AutoScalingGroupName: config.autoScaling.groupName,
    AvailabilityZones: ['us-east-1b'],
    LaunchConfigurationName: config.autoScaling.launchConfigName,
    DefaultCooldown: 30,
    MaxSize: 2,
    MinSize: 1
  };
  autoscaling.createAutoScalingGroup(params, createAutoScalingGroupCB);
};

createAutoScalingGroupCB = (err, data) => {
  if (err)
    console.log('Creation of AutoScaling Group Failed! ', err, err.stack);
  else {
    console.log('AutoScaling Group Created\n', data);
    attachTargetGroupsToAutoScalingGroup();
  }
};

attachTargetGroupsToAutoScalingGroup = () => {
  const params = {
    AutoScalingGroupName: config.autoScaling.groupName,
    TargetGroupARNs: [config.targetGroup.ARN]
  };
  autoscaling.attachLoadBalancerTargetGroups(
    params,
    attachTargetGroupsToAutoScalingGroupCB
  );
};

attachTargetGroupsToAutoScalingGroupCB = (err, data) => {
  if (err) console.log('Attachment of Target Group Failed! ', err, err.stack);
  else {
    console.log('Target Group Attached with AutoScaling Group\n', data);
    putScalingPolicies();
  }
};

putScalingPolicies = () => {
  const scaleOut = {
    AdjustmentType: 'ChangeInCapacity',
    AutoScalingGroupName: config.autoScaling.groupName,
    PolicyName: 'ScaleOut',
    ScalingAdjustment: 1,
    Cooldown: 15
  };

  const scaleIn = {
    AdjustmentType: 'ChangeInCapacity',
    AutoScalingGroupName: config.autoScaling.groupName,
    PolicyName: 'ScaleIn',
    ScalingAdjustment: -1,
    Cooldown: 15
  };
  autoscaling.putScalingPolicy(scaleOut, scaleOutPolicyCB);
  autoscaling.putScalingPolicy(scaleIn, scaleInPolicyCB);
};

scaleOutPolicyCB = (err, data) => {
  if (err) console.log('Creation of ScaleOut Policy Failed! ', err, err.stack);
  else {
    console.log('ScaleOut Policy Created\n', data);
    createCloudWatchAlarmsForPolicies('scaleOut', data.PolicyARN);
  }
};

scaleInPolicyCB = (err, data) => {
  if (err) console.log('Creation of ScaleIn Policy Failed! ', err, err.stack);
  else {
    console.log('ScaleIn Policy Created\n', data);
    createCloudWatchAlarmsForPolicies('scaleIn', data.PolicyARN);
  }
};

createCloudWatchAlarmsForPolicies = (AlarmName, PolicyARN) => {
  const globalAlarmConfig = {
    AlarmName,
    EvaluationPeriods: 1,
    MetricName: 'RequestCount',
    Namespace: 'AWS/ApplicationELB',
    Dimensions: [
      {
        Name: 'LoadBalancer',
        Value: config.loadBalancer.reference
      }
    ],
    AlarmActions: [PolicyARN],
    DatapointsToAlarm: 1,
    Statistic: 'Sum'
  };
  const scaleOut = {
    ...globalAlarmConfig,
    ComparisonOperator: 'GreaterThanOrEqualToThreshold',
    Period: 120,
    Threshold: 3,
    AlarmDescription: 'This will be used to scale out'
  };

  const scaleIn = {
    ...globalAlarmConfig,
    ComparisonOperator: 'LessThanOrEqualToThreshold',
    Period: 180,
    Threshold: 2,
    AlarmDescription: 'This will be used to scale in'
  };
  const params = AlarmName === 'scaleOut' ? scaleOut : scaleIn;
  cloudwatch.putMetricAlarm(params, createCloudWatchAlarmsForPoliciesCB);
};

createCloudWatchAlarmsForPoliciesCB = (err, data) => {
  if (err) console.log('Creation of CloudWatch Alarm Failed! ', err, err.stack);
  // an error occurred
  else console.log('CloudWatch Alarm Created!\n', data); // successful response
};

/**
 * Starting Point
 */
createLoadBalancer();
