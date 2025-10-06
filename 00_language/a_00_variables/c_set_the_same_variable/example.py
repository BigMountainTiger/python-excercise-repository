obj = {
    "value": "init value"
}


def print_object_value():
    print(obj['value'])


def set_object():
    global obj
    new_obj = {
        "value": "new value"
    }

    print(f'Old object id = {id(obj)}')
    print(f'New object id = {id(new_obj)}')

    obj = new_obj


print('Print the initial value')
print_object_value()


print()
print('Set the new object through a function')
set_object()

print()
print('The obj variable is now pointing to the new object')
print_object_value()


print()
print('Conclusion')
print('If a varibale is set to a new object, the other functions will be accessing the new object afterwards')
