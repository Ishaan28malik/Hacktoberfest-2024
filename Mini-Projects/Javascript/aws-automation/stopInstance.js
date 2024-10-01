const AWS = require('aws-sdk');
AWS.config.loadFromPath('config.json');
const ec2 = new AWS.EC2();

const instanceId = process.argv[2];

const stopInstance = () => {
  const params = {
    InstanceIds: [instanceId]
  };
  ec2.stopInstances(params, (err, data) => {
    if (err) console.log('Error Stopping the Instance', err, err.stack);
    else {
      console.log('Stopping Operation Started on Instance', data);
      const params = {
        Filters: [{ InstanceId: instanceId }]
      };
      ec2.waitFor('instanceStopped', params, (err, data) => {
        if (err) console.log(err, err.stack);
        else {
          console.log('Instance stopped', data);
          createImage(instanceId);
        }
      });
    }
  });
};

const createAMI = instanceId => {
  return new Promise((resolve, reject) => {
    const imageParams = {
      BlockDeviceMappings: [
        {
          DeviceName: '/dev/sdc',
          VirtualName: 'ephemeral1'
        }
      ],
      Description: 'An AMI for Online-Kaufen',
      InstanceId: instanceId,
      Name: 'Online-kaufen-AMI',
      NoReboot: true
    };
    ec2.createImage(imageParams, (err, data) => {
      if (err) {
        console.log(err, err.stack);
        reject(err);
      } else {
        console.log('create image :', data);
        resolve(data);
      }
    });
  });
};

stopInstance();
