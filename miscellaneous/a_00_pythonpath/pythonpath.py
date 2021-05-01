# This prints the exact path as Jupyter notebook.
# Jupyter will add ipython extensions as it needs, but it follows the virtualenv.

import sys

def run():
  for p in sys.path:
    print(p)

if __name__ == '__main__':
  run()