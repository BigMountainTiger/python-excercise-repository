from importlib.resources import path
from dotenv import load_dotenv
import base64
import threading
import http.server
import json
import os
import socketserver
import signal
from urllib import parse
import webbrowser
from pathlib import Path

load_dotenv()

evt = threading.Event()
data = {}


def launch_browser():
    success = webbrowser.open(os.getenv('oauth2URL'))


def start_local_server():
    PORT = int(os.getenv('callbackPort'))

    class HandlerClass(http.server.BaseHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def log_message(self, format, *args):
            pass

        def do_GET(self):
            try:
                parts = parse.urlparse(self.path)
                query = parse.parse_qs(parts.query)

                data['code'] = query.get('code')[0]

                self.send_response(302)
                self.send_header('Location', os.getenv('oauth2Redirect'))
                self.end_headers()

            finally:
                evt.set()

    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(
        ("", PORT),
        RequestHandlerClass=HandlerClass
    )

    def start():
        with httpd:
            httpd.serve_forever()

    x = threading.Thread(target=start, args=())
    x.start()

    return httpd


def get_token():
    conn = http.client.HTTPSConnection(os.getenv('oauthTokenDomain'))
    headers = {'content-type': 'application/json'}
    post_data = {'code': data['code']}

    try:

        conn.request('POST', os.getenv('oauthTokenPath'),
                     json.dumps(post_data), headers)

        response = conn.getresponse()
        body = json.loads(response.read().decode())

        data['token'] = body.get('token')

    finally:
        conn.close()


def decode_token():
    token = data.get('token')
    parts = token.split('.')

    payload = base64.b64decode(parts[1]+"==")
    data['payload'] = json.loads(payload)


def auth():
    httpd = start_local_server()
    signal.signal(signal.SIGINT, lambda s, f: evt.set())
    launch_browser()
    evt.wait(2 * 60)
    httpd.shutdown()

    get_token()

    token = data.get('token')
    home = str(Path.home())
    file_name = f"{home}/.oauth2_example/token"
    with open(file_name, 'w') as f:
        f.write(token)

    decode_token()

    print(f"Welcome {data.get('payload')['onpremisessamaccountname']}")
    # print()
    # print(json.dumps(data))
