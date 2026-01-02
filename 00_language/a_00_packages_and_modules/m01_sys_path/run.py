import sys

# 1. sys.path is a built-in variable within Python's sys module that contains a list of directories the interpreter
#   searches to locate modules for import

# 2. When multiple modules with the same name are present in different directories listed in sys.path,
#   Python will load the first one it finds by searching the directories in the order they appear in the list

# 3. When you have two different paths in sys.path where one is a sub-path of the other
#   (or just two different absolute/relative paths pointing to the same directory or file),
#   the Python interpreter might load the same code twice

print("Current sys.path:")
for path in sys.path:
    print(path)