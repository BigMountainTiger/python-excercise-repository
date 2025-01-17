import requests


if __name__ == '__main__':

    URLs = [
        'https://httpbin.org/get?parameter=parameter-value-1',
        'https://httpbin.org/get?parameter=parameter-value-2'
    ]

    result = ''
    with requests.Session() as s:
        for url in URLs:
            r = s.get(url)
            r.raise_for_status()

            # remove trailing carriage return
            text = r.text.rstrip('\n').rstrip('\r')
            result = f'{result}{text}\n'

    result = result[:-1]
    print(result)
