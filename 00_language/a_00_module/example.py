from module import what_is_A, text
import module

if __name__ == '__main__':

    # Expect the original text
    print('Without any new assignment')
    print(what_is_A())

    # Expect the original text
    print()
    text = 'New value'
    print('The new value is assigned to the importing variable')
    print(what_is_A())

    # Expect the new text
    print()
    text = 'New value'
    print('The new value is assigned to the orginal variable through the module')
    print(what_is_A())

