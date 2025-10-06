from functools import wraps

# The wraps is used to preserve the original meta information
# of a function after decoration

print('The "wraps" is used to preserve the original meta information of a function')
print('wraps is a decorator')
print()

# Without wraps
def scream(func):
    def wrapper(*args, **kwargs):
        print('Scream before calling the function')
        func(*args, **kwargs)

    return wrapper

@scream
def the_func():
    print('The function is called')

    
the_func()
print(the_func)
print('Without wraps, the meta information of the "the_func" is replaced by the "wrapper"')


print()


# With wraps
def scream(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Scream before calling the function')
        func(*args, **kwargs)

    return wrapper

@scream
def the_func():
    print('The function is called')

the_func()
print(the_func)
print('With wraps, the meta information of the "the_func" is preserved')