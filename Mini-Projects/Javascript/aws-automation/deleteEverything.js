const AWS = require('aws-sdk');
AWS.config.loadFromPath('config.json');
const autoscaling = new AWS.AutoScaling();
const cloudwatch = new AWS.CloudWatch();
const elbv2 = new AWS.ELBv2();
const ec2 = new AWS.EC2();

const config = {
  loadBalancer: {
    name: 'load-balancer',
    ARN: process.argv[2]
  },
  targetGroup: {
    name: 'target-group',
    ARN: process.argv[3]
  },
  autoScaling: {
    launchConfigName: 'autoScalingLaunchConfig',
    groupName: 'autoScalingGroup'
  },
  aws: {
    key: 'springapp',
    securityGroupID: 'sg-0fcaf7e6d2577dbe1',
    AMI_ID: process.argv[4],
    SnapshotId: process.argv[5],
    volumeId: process.argv[6]
  },
  iam: {
    s3BucketRole: 'ReadOnlyAccessS3'
  },
  cloudWatch: {
    AlarmNames: ['scaleOut', 'scaleIn']
  }
};

const deleteAutoScalingGroup = () => {
  const params = {
    AutoScalingGroupName: config.autoScaling.groupName,
    ForceDelete: true
  };
  autoscaling.deleteAutoScalingGroup(params, (err, data) => {
    if (err) console.log('Failed to Delete AutoScalingGroup', err, err.stack);
    else {
      console.log('AutoScalingGroup Deleted!\n', data);
    }
    deleteLaunchConfiguration();
  });
};

const deleteLaunchConfiguration = () => {
  var params = {
    LaunchConfigurationName: config.autoScaling.launchConfigName
  };
  autoscaling.deleteLaunchConfiguration(params, (err, data) => {
    if (err)
      console.log('Failed to Delete Launch Configuration', err, err.stack);
    else {
      console.log('Launch Configuration Deleted!\n', data);
    }
    deleteLoadBalancer();
  });
};

const deleteLoadBalancer = () => {
  var params = {
    LoadBalancerArn: config.loadBalancer.ARN
  };
  elbv2.deleteLoadBalancer(params, (err, data) => {
    if (err) console.log('Failed to Delete Load Balancer', err, err.stack);
    else {
      console.log('Load Balancer Deleted!\n', data);
      setTimeout(() => {
        deleteTargetGroup();
      }, 10000);
    }
  });
};

const deleteTargetGroup = () => {
  const params = {
    TargetGroupArn: config.targetGroup.ARN
  };
  elbv2.deleteTargetGroup(params, (err, data) => {
    if (err) console.log('Failed to Delete Target Groups', err, err.stack);
    else {
      console.log('Target Groups Deleted!\n', data);
      deleteAlarms();
    }
  });
};

const deleteAlarms = () => {
  const params = {
    AlarmNames: config.cloudWatch.AlarmNames
  };
  cloudwatch.deleteAlarms(params, (err, data) => {
    if (err) console.log('Failed to Delete Alarms', err, err.stack);
    else {
      console.log('Alarms Deleted!\n', data);
    }
    deregisterImage();
  });
};

const deregisterImage = () => {
  const params = {
    ImageId: config.aws.AMI_ID
  };
  ec2.deregisterImage(params, (err, data) => {
    if (err) console.log('Failed to Deregister Image', err, err.stack);
    else {
      console.log('Image Deregistered!\n', data);
    }
    deleteSnapshot();
  });
};

const deleteSnapshot = () => {
  const params = {
    SnapshotId: config.aws.SnapshotId
  };
  ec2.deleteSnapshot(params, (err, data) => {
    if (err) console.log('Failed to Delete Snapshot', err, err.stack);
    else {
      console.log('Snapshot Deleted!\n', data);
    }
    if (config.aws.volumeId) deleteVolume();
  });
};

const deleteVolume = () => {
  const params = {
    VolumeId: config.aws.volumeId
  };
  ec2.deleteVolume(params, (err, data) => {
    if (err) console.log('Failed to Delete Volume', err, err.stack);
    else console.log('Volume Deleted!\n', data);
  });
};
deleteAutoScalingGroup();
