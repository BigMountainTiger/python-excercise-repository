from mypack import module_1
import mypack

def test():
  mypack.module_1.print_me()
  module_1.print_me()

if __name__ == '__main__':
  test()