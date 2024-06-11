def range_test():
    # 1st entry is inclusive, 2nd is exclusive
    for i in range(0, 4, 2):
        print(i)

def copy_test():
    l = [1, 2, 3, 4]
    l_copy = l.copy()

    l[0] = 100

    # yet copy is shallow, it is OK for immutables
    print(l)
    print(l_copy)

if __name__ == '__main__':
    # range_test()
    copy_test()

