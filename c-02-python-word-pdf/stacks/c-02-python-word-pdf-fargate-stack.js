const cdk = require('@aws-cdk/core');
const ec2 = require("@aws-cdk/aws-ec2");
const ecr = require('@aws-cdk/aws-ecr');
const ecs = require("@aws-cdk/aws-ecs");
const iam = require('@aws-cdk/aws-iam');

class C02PythonWordPdfFargateStack extends cdk.Stack {

  constructor(scope, id, props) {
    super(scope, id, props);
    
    const tagResource = (resource) => {
      const tag = { key: 'VPC-TAG', value: 'FARGATE-VPC' };
      cdk.Tags.of(resource).add(tag.key, tag.value);
    };

    const VPC_NAME = `${id}-VPC`;
    const vpc = new ec2.Vpc(this, VPC_NAME, {
      maxAZs: 2,
      subnetConfiguration: [{
        cidrMask: 24,
        name: 'PUBLIC-SUBNET-CONFIG',
        subnetType: ec2.SubnetType.PUBLIC
      }]
    });
    tagResource(vpc);

    const CLUSTER_NAME = `${id}-CLUSTER`;
    const cluster = new ecs.Cluster(this, CLUSTER_NAME, { vpc, clusterName: CLUSTER_NAME });
    tagResource(cluster);

    const TASK_ROLE_NAME = `${id}-TASK-ROLE`;
    const task_role = new iam.Role(this, TASK_ROLE_NAME, {
      roleName: TASK_ROLE_NAME,
      description: TASK_ROLE_NAME,
      assumedBy: new iam.ServicePrincipal('ecs-tasks.amazonaws.com'),
    });

    task_role.addToPolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      resources: ['*'],
      actions: ['s3:GetObject', 's3:PutObject']
    }));

    const FARGATE_NAME = `${id}-FARGATE`;
    const fargateTaskDefinition = new ecs.FargateTaskDefinition(this,
      FARGATE_NAME, {
        memoryMiB: "512",
        cpu: "256",
        taskRole: task_role
    });
    tagResource(fargateTaskDefinition);

    const REPOSITORY_ID = `${id}-REPOSITORY`;
    const REPOSITORY_NAME = `experiment-1`;
    const repository = new ecr.Repository(this, REPOSITORY_ID, {
      repositoryName: REPOSITORY_NAME,
      removalPolicy: cdk.RemovalPolicy.DESTROY
    });

    const CONTAINER_NAME = `${id}-CONTAINER`;
    fargateTaskDefinition.addContainer(CONTAINER_NAME, {
      image: ecs.ContainerImage.fromEcrRepository(repository, '0.0.1')
    });
  }
}

module.exports = { C02PythonWordPdfFargateStack }