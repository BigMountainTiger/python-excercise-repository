import requests


if __name__ == '__main__':

    URL = 'https://httpbin.org/get?parameter=parameter-value'

    # response is using a context manager
    with requests.get(URL) as r:
        data = r.json()
        text = r.text

    print('data\n')
    print(data)

    print()
    print('text\n')
    print(text)
