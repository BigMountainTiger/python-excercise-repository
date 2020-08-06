# https://support.snowflake.net/s/question/0D50Z000070P0PvSAK/invalid-utf8-detected-in-string
# https://docs.snowflake.com/en/sql-reference/sql/create-file-format.html

import boto3

def read_s3():

  session = boto3.Session(profile_name = 'snowflake')
  s3 = session.client('s3')

  r = s3.select_object_content(
        Bucket='mlg-snowpipe',
        Key='Lead.txt',
        ExpressionType='SQL',
        Expression="select * from s3object s WHERE s.LeadID = '90403765' limit 1",
        #Expression="select * from s3object",
        InputSerialization = {'CSV': {'FileHeaderInfo': 'USE', 'FieldDelimiter': '|'}},
        OutputSerialization = {'CSV': {'FieldDelimiter': '|'}},
        # ScanRange={
        # 'Start': 30000,
        # 'End': 35000
        # }
      )

  for event in r['Payload']:
    if 'Records' in event:
        payload = event['Records']['Payload']
        records = payload.decode('utf-8')
        print(payload)
        print(records)

    elif 'Stats' in event:
        statsDetails = event['Stats']['Details']
        print("Stats details bytesScanned: ")
        print(statsDetails['BytesScanned'])
        print("Stats details bytesProcessed: ")
        print(statsDetails['BytesProcessed'])


if __name__ == '__main__':
    read_s3()