from dotenv import load_dotenv
import os
import http.client
import json
import urllib
import json 

load_dotenv()
UN = os.environ.get('UN')
PASSWORD = os.environ.get('PASSWORD')
TURL = os.environ.get('TURL')


def gettoken():
    conn = http.client.HTTPSConnection(TURL)

    headers = {'content-type': 'application/x-www-form-urlencoded'}
    data = urllib.parse.urlencode({
        'username': UN,
        'password': PASSWORD,
        'grant_type': 'password'
    })
    
    try:
        conn.request("POST", "/Token", data)
        response = conn.getresponse()
        text = response.read().decode()

        return json.loads(text)['access_token']
    finally:
        conn.close()


def run():

    token = gettoken()
    print(token)

if __name__ == '__main__':
    run()
