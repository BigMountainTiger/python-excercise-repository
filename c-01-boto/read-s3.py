# https://support.snowflake.net/s/question/0D50Z000070P0PvSAK/invalid-utf8-detected-in-string
# https://docs.snowflake.com/en/sql-reference/sql/create-file-format.html

import boto3

def read_s3():
  s3 = boto3.client('s3',
    aws_access_key_id='Key',
    aws_secret_access_key='s-key'
  )

  r = s3.select_object_content(
        Bucket='mlg-snowpipe',
        Key='Lead.txt',
        ExpressionType='SQL',
        Expression="select * from s3object s WHERE s.propertyCounty <> null limit 2",
        InputSerialization = {'CSV': {'FileHeaderInfo': 'USE', 'FieldDelimiter': '|'}},
        OutputSerialization = {'CSV': {'FieldDelimiter': '|'}}
      )

  for event in r['Payload']:
    if 'Records' in event:
        records = event['Records']['Payload'].decode('utf-8')
        print(records)

    elif 'Stats' in event:
        statsDetails = event['Stats']['Details']
        print("Stats details bytesScanned: ")
        print(statsDetails['BytesScanned'])
        print("Stats details bytesProcessed: ")
        print(statsDetails['BytesProcessed'])


if __name__ == '__main__':
    read_s3()