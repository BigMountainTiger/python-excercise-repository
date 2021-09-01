# https://httpbin.org/
# The test web api - A simple HTTP Request & Response Service

# https://docs.python.org/3/library/http.client.html
# https://www.journaldev.com/19213/python-http-client-request-get-post

import http.client
import json
import urllib

# GET example
def get_example():
  # This is a public test server - https://httpbin.org
  conn = http.client.HTTPSConnection('httpbin.org')
  data = {
    'data': 'this is the data'
  }

  try:
    # urlencode the data for GET parameters
    args = urllib.parse.urlencode(data)
    conn.request('GET', f'/get?{args}')
    response = conn.getresponse()

    print(response.read().decode())
  finally:
    conn.close()

  print('Done with GET example')

# POST example
def post_example():

  conn = http.client.HTTPSConnection('httpbin.org')

  headers = { 'content-type': 'application/json' }
  data = { 'data': 'This is the test data' }

  try:
    conn.request("POST", "/post", json.dumps(data), headers)

    response = conn.getresponse()
    print(response.read().decode())
  finally:
    conn.close()

  print('Done with POST example')


if __name__ == '__main__':
  get_example()
  print()
  post_example()