# https://docs.python.org/3/tutorial/errors.html

# 1. Finally is always executed
# 2. If there is an except (catch) block, the except (catch) block is executed before the finally block
# 3. The finally block is always executed regardless if there is an exception and if the expcetion is from the try or the catch block
# 4. try/except/finally is a unit block, only when the inner block finishs, the outer block starts

def raise_exception():
  raise Exception('An exception is raised')

def try_finaly():
  try:
    raise_exception()
  except Exception as e:
    print(f'Exception re-raise - {e}')
    raise e
  finally:
    print('1st Finally is always executed, even the exception is from the catch block')

def try_catch_finally():
  try:
    try_finaly()
  except Exception as e:
    print(f'Exception caught - {e}')
  finally:
    print('2nd Finally is always executed')

if __name__ == '__main__':
  try_catch_finally()