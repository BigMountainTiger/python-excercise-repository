import http.client
import json
import jwt
from pathlib import Path


def load_keys():
    conn = http.client.HTTPSConnection('login.microsoftonline.com')
    conn.request('GET', '/common/discovery/v2.0/keys')
    response = conn.getresponse()

    key_map = {}
    keys = json.loads(response.read().decode()).get('keys')

    for key in keys:
        kid = key.get('kid')
        key_map[kid] = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(key))

    return key_map


def load_token():
    home = str(Path.home())
    file_name = f"{home}/.oauth2_example/token"
    # Exception if file not exist
    with open(file_name, 'r') as f:
        token = f.read()

    return token


def decode_token(key_map, token):
    header = jwt.get_unverified_header(token)
    alg = header.get('alg') or 'RS256'
    kid = header.get('kid')
    key = key_map.get(kid)

    data = jwt.decode(
        token,
        key=key,
        algorithms=[alg],
        options={
            "verify_aud": False
        }
    )

    return data


def verify():
    key_map = load_keys()
    token = load_token()
    data = decode_token(key_map, token)

    print(data)
