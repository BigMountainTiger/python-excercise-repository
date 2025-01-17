text = 'This is a text string'

print('Multiple line string can use either single or double quote')


single_quote_string = f'''
    line No.1 - 1
    line No.2 - "{text}"
    line No.3 - 3
'''
print(single_quote_string)

double_quote_string = f"""
    line No.1 - 1
    line No.2 - '{text}'
    line No.3 - 3
"""
print(double_quote_string)


print('It is more convenient to use double quote if working with SQL')
print('It is more convenient to use single quote if working with JSON')
