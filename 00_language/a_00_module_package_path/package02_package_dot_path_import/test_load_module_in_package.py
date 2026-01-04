from package_1.dir_1 import module_1

# Look at the package_1/dir_1/module_1.py file
# "." means current directory, ".." parent directory, "..." one more parent above.
# Relative import above top-level package is an error
module_1.print()