const AWS = require('aws-sdk');
AWS.config.loadFromPath('config.json');
const autoscaling = new AWS.AutoScaling();

const config = {
  AutoScalingGroupName: 'autoScalingGroup',
  PolicyName: process.argv[2]
};

const params = {
  AutoScalingGroupName: config.AutoScalingGroupName,
  HonorCooldown: true,
  PolicyName: config.PolicyName
};
autoscaling.executePolicy(params, (err, data) => {
  if (err) console.log('Policy Execution Failed!', err, err.stack);
  else console.log('Policy Executed!', data);
});
