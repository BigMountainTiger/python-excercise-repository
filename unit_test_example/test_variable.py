A = 'Initial Value'

def get_func():
    def func():
        print(A)

    return func

func = get_func()

A = 'Updated value !!!!'

# Expect to print the updated value
# because a variable if an object reference, the object is immutable

func()