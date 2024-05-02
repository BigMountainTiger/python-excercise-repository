# A class with an instance method, a class method,
# and a static method
class AClass:
  a_class_attr = 'The class attribute'

  def __init__(self):
    self.a_instance_attr = 'The instance attribute'

  def an_instance_method(self):
    print("From the instance method - {}".format(self.a_instance_attr))

  @classmethod
  def a_class_method(cls):
    print("From the class method - {}".format(cls.a_class_attr))
  
  @staticmethod
  def a_static_mathod():
    print('Print from a static method')


# Create an instance of AClass and call the methods
obj_1 = AClass()
obj_1.an_instance_method()
obj_1.a_class_method()
obj_1.a_static_mathod()
print()

# Class and static methods can be accessed by the class name
AClass.a_class_method()
AClass.a_static_mathod()