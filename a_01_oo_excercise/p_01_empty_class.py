class EmptyClass:
  pass

obj_1 = EmptyClass()

obj_1.property1 = "property 1"
obj_1.property2 = "property 2"

print(obj_1.property1 + ' - ' + obj_1.property2)
print(obj_1.__dict__)