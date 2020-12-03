const cdk = require('@aws-cdk/core');
const iam = require('@aws-cdk/aws-iam');
const lambda = require('@aws-cdk/aws-lambda');

class C02PythonWordPdfLambdaStack extends cdk.Stack {

  constructor(scope, id, props) {
    super(scope, id, props);
    
    const ROLE_NAME = `${id}_LAMBDA_ROLE`;
    const role = new iam.Role(this, ROLE_NAME, {
      roleName: ROLE_NAME,
      description: ROLE_NAME,
      assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
    });

    role.addToPolicy(new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      resources: ['*'],
      actions: ['logs:CreateLogGroup', 'logs:CreateLogStream', 'logs:PutLogEvents', 's3:GetObject', 's3:PutObject']
    }));

    const LAMBDA_NAME = `WORD_2_PDF_LAMBDA`;
    new lambda.Function(this, LAMBDA_NAME, {
      runtime: lambda.Runtime.DOTNET_CORE_3_1,
      functionName: LAMBDA_NAME,
      description: LAMBDA_NAME,
      timeout: cdk.Duration.seconds(15),
      role: role,
      code: lambda.Code.fromAsset('./lambdas/word2pdf/bin/Debug/netcoreapp3.1/publish'),
      memorySize: 256,
      handler: 'Word2pdf::Word2pdf.Function::FunctionHandler'
    });
    
  }
}

module.exports = { C02PythonWordPdfLambdaStack }