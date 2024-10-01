// Load the AWS SDK for Node.js
const AWS = require('aws-sdk');
// Load credentials and set region from JSON file
AWS.config.loadFromPath('config.json');
const ec2 = new AWS.EC2({ apiVersion: '2016-11-15' });
const userData64 = new Buffer(`
#!/bin/bash
set -ex
sudo yum -y update
sudo yum -y install java-1.8.0
echo -ne '2\n' | sudo /usr/sbin/alternatives --config java
sudo yum -y install tomcat8
sudo yum -y install tomcat8-admin-webapps
sudo service tomcat8 start
if [ ! -f /usr/share/tomcat8/webapps/online-kaufen.war ]
then
	aws s3 cp s3://cloud-computing2019/online-kaufen.war /usr/share/tomcat8/webapps
fi
if [ ! -f application.properties ]
then
	aws s3 cp s3://cloud-computing2019/tomcat/application.properties .
fi
if [ ! -f context.xml ]
then
	aws s3 cp s3://cloud-computing2019/tomcat/context.xml .
fi
if [ ! -f tomcat-users.xml ]
then
	aws s3 cp s3://cloud-computing2019/tomcat/tomcat-users.xml .
fi
sudo cp tomcat-users.xml /usr/share/tomcat8/conf
sudo cp context.xml /usr/share/tomcat8/webapps/host-manager/META-INF
sudo cp context.xml /usr/share/tomcat8/webapps/manager/META-INF
sleep 15
sudo cp application.properties /usr/share/tomcat8/webapps/online-kaufen/WEB-INF/classes
sudo service tomcat8 restart
sudo chkconfig tomcat8 on
`).toString('base64');

// AMI is amzn-ami-2011.09.1.x86_64-ebs
const instanceParams = {
  ImageId: 'ami-035b3c7efe6d061d5',
  InstanceType: 't2.micro',
  KeyName: 'springapp',
  MinCount: 1,
  MaxCount: 1,
  SecurityGroups: ['launch-wizard-2'],
  UserData: userData64,
  IamInstanceProfile: {
    Name: 'ReadOnlyAccessS3'
  }
};

const ec2InstanceCreation = async () => {
  try {
    // Create a promise on an EC2 service object
    const instancePromise = ec2.runInstances(instanceParams).promise();
    const createInstance = await instancePromise;
    console.log('createInstance: ', createInstance);
    const instanceId = createInstance.Instances[0].InstanceId;

    const tagParams = {
      Resources: [instanceId],
      Tags: [
        {
          Key: 'Name',
          Value: 'Online-Kaufen-Dev'
        }
      ]
    };
    // Create a promise on an EC2 service object
    const tagPromise = ec2.createTags(tagParams).promise();
    await tagPromise;
    console.log('Instance tagged');
  } catch (err) {
    console.log('ERR :', err);
  }
};

ec2InstanceCreation();
