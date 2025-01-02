# class Vehicle():
#     def __init__(self,mileage, typee):
#         self.typee=typee
#         self.mileage=mileage
#     def display(self):
#         print(f"Type : {self.typee}, Mileage :{self.mileage}")


# class Bike(Vehicle):

#     def __init__(self, company, mileage):
#         super().__init__(mileage, typee="Bike")
#         self.company=company
#     def display(self):
#         super().display()
#         print("Comapny: ",self.company)


# bike=Bike("TVS",30)
# print(bike.company)
# print(bike.mileage)
# print(bike.typee)
# bike.display()


# class Car(Vehicle):
#     def __init__(self,typee,mileage,company):
#         super().__init__(typee,mileage)
#         self.company=company
#     def display(self):
#         super().display()
#         print("Company: ",self.company)
    
# b1=Car("Car",28,"Toyota")
# b1.display()


# Python Program to depict multiple inheritance
# when every class defines the same method

# Python Program to depict multiple inheritance
# when method is overridden in both classes

# class Class1:
# 	def m(self):
# 		print("In Class1") 
	
# class Class2(Class1):
# 	def m(self):
# 		super().m()
# 		print("In Class2")

# class Class3(Class1):
# 	def n(self):
# 		print("In Class3") 
		
# class Class4(Class2, Class3):
# 	def m(self):
# 		super().m()
# 		super().n()
# 		print("In Class4")

# obj = Class4()
# obj.m()

# cls2=Class2()
# cls2.m()









# Mutiple inheritance example and MRO 

# class Class1:
# 	def m(self):
# 		print("In Class1")

# class Class2(Class1):
# 	def m(self):
# 		print("In Class2")      #2
# 		super().m()             #1

# class Class3(Class1):
# 	def m(self):
# 		print("In Class3")      #3
# 		super().m()             #1

# class Class4(Class2, Class3):
# 	def m(self):
# 		print("In Class4")      #4
# 		super().m()             #2 1
	
# obj = Class4()
# obj.m()         

# print(Class4.mro())





# class CL1:
#     def m(self):
#         print("In class 1")


# class CL2(CL1):
#     def m(self):
#         super().m()
#         print("In class 2")

# class CL3(CL1):
#     def m(self):
#         super().m()
#         print("In class 3")

# class CL4(CL2,CL3):
#     def m(self):
#         super().m()
#         print("In class 4")

# obj4=CL4()
# obj4.m()

# print(CL4.mro())







# Access specifiers
# ------------------private--------------------


# class employee():
# 	def __init__(self):
# 		self.__name = "Ramu"
# e=employee()
# print(e.__name)                         # aceessing directly causing error

# print(e._employee__name)                # aceessing indirectly











# -------------------Hybrid inheritance----------------------------

# class Animal:
# 	def speak(self):
# 		print("Animal speaks")
# class Cat(Animal):
# 	def meow(self):
# 		print("Cat meow")
# class Tiger(Animal):
# 	def roar(self):
# 		print("Tiger runs")
# class Leopard(Cat,Tiger):
# 	def prey(self):
# 		print("Good predator")

# leopard = Leopard()
# leopard.speak()
# leopard.meow()










# ------------------------------------Polymorphism------------------------------------


# class Animal:
#     def speak(self):
#         raise NotImplementedError("Subclass must implement this method")

# class Dog(Animal):

#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
    
# animals = [Dog(), Cat()]

# for a in animals:
#     print(a.speak())









#---------------------------------------Data Abstraction----------------------------------------

# from abc import ABC, abstractmethod

# class Car(ABC):
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
    
#     @abstractmethod
#     def details(self):
#         pass

#     def accelerate(self):
#         print("Car accelerates")

#     def brake(self):
#         print("Brakes applied")

# class Sedan(Car):
#     def details(self):
#         print(f"Brand : {self.brand}, model : {self.model}, year : {self.year}")
#     def sunroof(self):
#         print("No sunroof")
# sedan =Sedan("Toyota", "Fortuner",2015)
# sedan.details()
# sedan.accelerate()
# sedan.brake()
# sedan.sunroof()


# car=Car("M","D",2016)
# car.details()














# -------------------------------------------------ATM machine in python-----------------------------------

# class ATM():
#     def __init__(self):
#         self.pin= None
#         self.balance=0
#         self.menu()
#     def menu(self):
#         while(True):
#             option=input(""" Enter
#                             1 to Create pin
#                             2 to Deposit
#                             3 to Withdraw
#                             4 to Check balance
#                             E/e to exit
#                             """)
#             if option == "1":
#                 self.create_pin()
#             elif option=="2":
#                 self.deposit()
#             elif option=="3":
#                 self.withdraw()
#             elif option =="4":
#                 self.check_balance()
#             elif option== "E" or option == "e":
#                 print("Wrong input")
#                 break
#     def create_pin(self):
#         temp=int(input("Enter 4 digit pin : "))
        
#         if len(str(temp)) ==4:
#             self.pin=temp
#             print("Pin created successfully")
#         else:
#             print("Incorrect pin type")
#     def deposit(self):
#         temp=int(input("Enter your pin : "))
#         if temp == self.pin:
#             amount = int(input("Enter amount to deposit : "))
#             self.balance+=amount
#             print("Deposited succesfully")
#         else:
#             print("Incorrect pin")
#     def withdraw(self):
#         temp=int(input("Enter your pin : "))
#         if temp == self.pin:
#             amount = int(input("Enter amount to withdraw : "))
#             if amount<=self.balance:
#                 self.balance-=amount
#                 print("Withdraw succesfull")
#             else:
#                 print("Insufficient balance")
#         else:
#             print("Incorrect pin")
#     def check_balance(self):
#         temp=int(input("Enter pin : "))
#         if temp==self.pin:
#             print("Balance : ",self.balance)
#         else:
#             print("Incorrect pin")

# atm=ATM()














#------------------------------------------ Fraction operations------------------------------------------------

# class fraction:
#     def __init__(self,n,d) -> None:
#         self.num=n
#         self.den=d
    
#     def __add__(self,other):
#         temp_num=self.num*other.den +other.num*self.den
#         temp_den=self.den*other.den
#         return "{}/{}".format(temp_num,temp_den)
    
# frac1=fraction(3,4)
# frac2=fraction(5,6)
# print(frac1+frac2)











#------------------------------------------Reference variable------------------------------------------------------

# class employee():
#     def __init__(self,name,role) -> None:
#         self.__name=name
#         self.__role=role

# def info(emp):
#     if emp._employee__role =="Trainee":
#         print(f"{emp._employee__name} is a trainee")
#     else:
#         print(f"{emp._employee__name} is a Permanent employee")
# emp1=employee("ankit","Trainee")
# info(emp1)











#------------------------------------------------------Class Attributes-----------------------------------------------------

# class Employee():
#     emp_id=1

#     def __init__(self,name,role):
#         self.id=Employee.emp_id
#         self.name=name
#         self.role=role
#         Employee.emp_id+=1

#     def display(self):
#         print(f"Emp id : {self.id}, name: {self.name}, role : {self.role}")

# emp1=Employee("Arun","SDE")
# emp2=Employee("Priyansh","Lawyer")

# emp1.display()
# print(emp1.emp_id)
# emp2.display()
# print(emp2.emp_id)























# li=[1,2,3]
# methodd="insert"
# getattr(li, methodd)(2,5)
# print(li)



# class ElectronicDevice:
#     def __init__(self, brand, serial_number):
#         self.brand=brand
#         self.serial_number= serial_number

# class Computer(ElectronicDevice):
#     def __init__(self, brand, serial_number, memory, processor):
#         super().__init__(brand,serial_number)
#         self.memory =memory
#         self.processor= processor

# class TV(ElectronicDevice):
#     def __init__(self, brand, serial_number, max_resolution):
#         super().__init__(brand, serial_number)
#         self.max_resolution=max_resolution

# class Desktop(Computer):
#     def __init__(self, brand, serial_number, memory, processor, display_size):
#         super().__init__(brand, serial_number, memory, processor)
#         self.display_size = display_size

# class Laptop(Computer):
#     def __init__(self, brand, serial_number, memory, processor, is_graphic_card):
#         super().__init__(brand, serial_number, memory, processor)
#         self.is_graphic_card = is_graphic_card








# class Character:
    
#     def __init__(self, x, y, img_file, speed, life_counter):
#         self.x = x
#         self.y = y
#         self.img_file = img_file
#         self.speed = speed
#         self.life_counter = life_counter
 
 
# class Enemy(Character):
    
#     def __init__(self, x, y, img_file, speed):
#         Character.__init__(self, x, y, img_file, speed, 5)
#         self.message = "I'm here to protect my master"
 
 
# class Player(Character):
    
#     def __init__(self, x, y, img_file, speed=56, life_counter=6):
#         Character.__init__(self,x, y, img_file, speed, life_counter)
 
 
# class DifficultEnemy(Enemy):
    
#     def __init__(self, x, y, img_file):
#         Enemy.__init__(self,x,y, img_file, 80)
 
 
# class EasyEnemy(Player):
    
    
#     def __init__(self, x, y, img_file):
#         Enemy.__init__(self, x, y, img_file, 40)
#         self.life_counter = 1









# Method overloading


# def opr(a, b, c):
#     print(a+b)


# def opr(a, b):
#     print(a*b)

# opr(2,5,7)   



# for i in range(1,11):
#     if i%2 == 0:
#         print(i)
#     else:
#         print(500)







# for i in range(1,11):
#     if i%2==0:
#         print(i)
#     else:
#       print(500)


# for i in range(1,11):
#   print(i)
#   else:
#     print(500)









# try:
#   f=open('qwe.txt', mode='r')
#   f.write("Hello")
# except Exception as e:
#   print(e)
# else:
#   print("No exception occured")
# finally:
#     try:
#         f.close()
#     except:
#         pass





# def long_sub(lst):
#   i=0
#   total_len=0
#   list_len=len(lst)
#   while i<list_len:
#     j=i
#     length=0
#     while j<list_len-1:
#       if lst[j]<lst[j+1]:
#         length+=1
#         j+=1
#       else:
#         i+=1
#         if total_len<length:
#           total_len=length
#           break
#     if total_len<length:
#       total_len=length
#       i+=1

#   return total_len

# l=[10, 20, 30, 40, 50, 60, 70, 80]

# print(long_sub(l))





g= [{"Name":"abc", "marks":[10,20,30]},{"Name":"def","marks":[40,50,60]}]

r=sum(list(map(lambda x: sum(x("marks")), g)))

print(r)