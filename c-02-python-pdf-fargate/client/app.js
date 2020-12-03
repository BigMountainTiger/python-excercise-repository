const aws = require('aws-sdk');
const lambda = new aws.Lambda({ region: 'us-east-1' });

const lambda_name = 'WORD_2_PDF_LAMBDA';

(async () => {
  
  const payload = {
    Payload: 'This is the payload'
  };

  const result = await lambda.invoke({
    FunctionName: lambda_name,
    Payload: JSON.stringify(payload)
  }).promise();

  console.log(result);

})();

