import pkg_basic
from pkg_basic.inner import A

def outter(x):
    a_obj = A()
    return a_obj.inner(x)