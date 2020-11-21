const cdk = require('@aws-cdk/core');
const ecr = require('@aws-cdk/aws-ecr');

class C02PythonWordPdfEcrStack extends cdk.Stack {

  constructor(scope, id, props) {
    super(scope, id, props);

    const REPOSITORY_ID = `${id}-REPOSITORY`;
    const REPOSITORY_NAME = `experiment-1`;
    new ecr.Repository(this, REPOSITORY_ID, {
      repositoryName: REPOSITORY_NAME,
      removalPolicy: cdk.RemovalPolicy.DESTROY
      
    })

  }
}

module.exports = { C02PythonWordPdfEcrStack }
