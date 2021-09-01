# https://docs.python.org/3/tutorial/errors.html

# 1. Finally is always executed
# 2. If there is an except block, the except block is executed before the finally block

def raise_exception():
  raise Exception('An exception is raised')

def try_finaly():
  try:
    raise_exception()
  finally:
    print('1st Finally is always executed')

def try_catch_finally():
  try:
    try_finaly()
  except Exception as e:
    print(e)
  finally:
    print('2nd Finally is always executed')

if __name__ == '__main__':
  try_catch_finally()