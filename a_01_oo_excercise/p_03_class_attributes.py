# A class with both instance and class attributes
class AClass:
  a_class_attr = 'The class attribute'

  def print_class_attribute_by_self_reference(self):
    print(self.a_class_attr)

  def print_class_attribute_by_class_name(self):
    print(AClass.a_class_attr)

# Create an instance of AClass
obj_1 = AClass()

# A class attribute can be accessed by
# both the instance reference and the class name
obj_1.print_class_attribute_by_self_reference()
obj_1.print_class_attribute_by_class_name()
print()

# Add a instance attribute with the same name
obj_1.a_class_attr = 'This can override the class attribute'
obj_1.print_class_attribute_by_self_reference()
obj_1.print_class_attribute_by_class_name()
print()

# Delete the instance attribute
del obj_1.a_class_attr
obj_1.print_class_attribute_by_self_reference()
obj_1.print_class_attribute_by_class_name()
print()