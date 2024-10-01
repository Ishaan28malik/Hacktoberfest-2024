const AWS = require('aws-sdk');
AWS.config.loadFromPath('config.json');
const ec2 = new AWS.EC2({ apiVersion: '2016-11-15' });
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

createAMI(process.argv[2]);