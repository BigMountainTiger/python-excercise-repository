# https://docs.snowflake.com/en/user-guide/python-connector-install.html
# https://pypi.org/project/python-dotenv/
# pip install snowflake-connector-python

import os
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()
user = os.getenv('SNOWUSER')
pwd = os.getenv('SNOWPWD')
account = os.getenv('ACCOUNT')

def run():
  ctx = snowflake.connector.connect(
    user = user,
    password = pwd,
    account = f'{account}.us-east-1'
  )
  cs = ctx.cursor()

  try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])

  finally:
    cs.close()

  ctx.close()

if __name__ == '__main__':
  run()