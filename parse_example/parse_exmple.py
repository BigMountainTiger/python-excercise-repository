import parse


def run():

    format = 'www.{domain}.com'
    result = parse.parse(format, 'www.google.com')

    domain = result['domain']
    print(domain)


if __name__ == '__main__':
    run()
