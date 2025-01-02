class getterANDsetter():
   def __init__(self):
      self._name="ab"

   @property 
   def name(self):
      print("getter method called")
      return self._name
   
   @name.setter
   def name(self,n):
      print("Setter method called")
      self._name=n

obj=getterANDsetter()

print(obj.name)
obj.name="rahul"
print(obj.name)




class Employee():
   
    def __init__(self,name,age):
      self._name=name
      self._age=age
    def get_name(self):
       return self._name

emp=Employee("Rahul",25)
print(emp.get_name())



