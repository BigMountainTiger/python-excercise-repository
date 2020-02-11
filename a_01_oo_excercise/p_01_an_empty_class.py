# Python allows empty class
class EmptyClass:
  pass

# Create an instance of the class
obj_1 = EmptyClass()

# Attrubutes can be added to an object dynamically
obj_1.attribute1 = "The attribute 1"
obj_1.attribute2 = "The attribute 2"

print(obj_1.attribute1 + ' - ' + obj_1.attribute2)
print(obj_1.__dict__)

# Attributes can be deleted from an object
del obj_1.attribute2
print(obj_1.__dict__)