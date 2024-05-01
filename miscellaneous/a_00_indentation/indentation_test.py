def run():

    def tab_test():
        print()
        if 1 == 1:
            print('Single Tab')

        if 1 == 1:
                print('Double tab')

        if 1 == 1:
                    print('Tripple tab')

    tab_test()
    
    def space_test():
        print()
        if 1 == 1:
         print('Single space')

        if 1 == 1:
          print('Double space')

        if 1 == 1:
           print('Tripple space')

    space_test()

    print()
    print('Indentation can be any size, as long as it is consistent in the code block')
    print('But the formatter, ie. autopep8, will replace make the indentations consistent')


if __name__ == '__main__':
    run()