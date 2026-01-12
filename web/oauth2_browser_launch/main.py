from nis import match
from unittest import case
from dotenv import load_dotenv
import sys

from auth import auth
from verify import verify

load_dotenv()


if __name__ == '__main__':

    args = sys.argv
    what = 'verify'
    if len(args) > 1:
        what = args[1]

    if what == 'auth':
        auth()
    elif what == 'verify':
        verify()
    else:
        print('Nothing to do')
