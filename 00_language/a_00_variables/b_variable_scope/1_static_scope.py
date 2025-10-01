# Python uses static (or lexical) scoping. 
# This means that the scope of a variable, and thus which variable a name refers to,
# is determined by the textual layout of the code at the time the code is written, 
# not at runtime based on the call stack.


# Here's what that implies:
# Predictability:
# When you read Python code, you can determine where a variable is defined and what value it refers to simply by
# looking at the code's structure and the nesting of functions and blocks.
# This makes code easier to understand and debug.

# LEGB Rule:
# Python's name resolution follows the LEGB rule: Local, Enclosing function locals, 
# Global, Built-in. When a name is referenced,
# Python searches for it in this order through the nested scopes where it was defined.

# Closures:
# Static scoping enables the creation of closures, where a nested function "remembers" the environment in which it was created, 
# including the values of non-local variables from its enclosing scope, even after the enclosing function has finished executing.

# While Python is a dynamically typed language (meaning variable types are determined at runtime), its scoping rules are static. 
# This distinction is important to understand when working with variables and functions in Python.