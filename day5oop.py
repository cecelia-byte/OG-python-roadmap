# class Student:
#     name= "karan" 
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("adding new student in db")
        
# s1= Student("karan",89)
# print(s1.name,s1.marks)
# # print(s1.name)
# s2= Student("arjun",99)
# print(s2.name,s2.marks)

# class Student:
#     def __init__(self,name,marks1,marks2,marks3):
#         self.name=name
#         self.marks1=marks1
#         self.marks2=marks2
#         self.marks3=marks3
#     def average(self):
#         sum=self.marks1+self.marks2+self.marks3
#         avg=sum/3
#         print(avg)
#         return avg
#     @staticmethod
#     def hello():
#         print("hello from student class")
    
# s1=Student("Sam",89,78,69)
# print(s1.name,s1.marks1,s1.marks2,s1.marks3)
# s1.average()
# s1.hello()
# class Account:
#     def __init__(self,balance,account_number):
#         self.balance=balance
#         self.account_number=account_number
#     def debit(self,amount):
#         self.balance=self.balance-amount
#         print("debited amount:",amount)
#         print("remaining balance:",self.balance)
#     def credit(self,amount):
#         self.balance=self.balance+amount
#         print("credited amount:",amount)
#         print("current balance:",self.balance)
#     def display(self):
#         print("account number:",self.account_number)
#         print("balance:",self.balance)
# a1=Account(1000,"1234567890")  
# a1.debit(500)
# a1.credit(200)
# a1.display()
# del a1.account_number
# a1.display()
# class Person:
#     __name="Sam"
#     def __hello(self):
#         print("hello from person class")

#     def welcome(self):
#         self.__hello()

# p1=Person()
# p1.welcome()

# class Car:
#     color="red"
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class Toyota(Car):
#     def __init__(self,brand):
#         self.brand=brand

# # car1=Toyota("fortuner")
# # print(car1.brand)
# # print(car1.color)
# # car1.start()        
# class Fortuner(Toyota):
#     def __init__(self,type,brand):
#         self.type=type
#         super().__init__(brand)

# f1=Fortuner("electric","fortuner")
# print(f1.type)
# f1.start()
# print(f1.brand)

# class A:
#     varA="inside class A"
# class B:
#     varB="inside class B"
# class C(A,B):
#     varC="inside class C"

# c1=C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)
# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math

#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3)+"%"    
# stu1=Student(89,78,69)
# print(stu1.percentage)
# stu1.phy=90
# stu1.math=80
# print(stu1.percentage)
 
# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def show(self):
#         print(self.real,"i+",self.img,"j")
#     def add(self,num2):
#         newReal= self.real+num2.real
#         newImg=self.img+num2.img
#         return Complex(newReal,newImg)
# num1=Complex(2,3)
# num1.show()
# num2=Complex(4,5)
# num2.show()
# num3=num1.add(num2)
# num3.show()
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius*self.radius
#     def circumference(self):
#         return 2*3.14*self.radius
# c1=Circle(6)
# print(c1.area())
# print(c1.circumference())
# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary
#     def showDetails(self):
#         # return self.role,self.dept,self.salary
#         print("role",self.role)
#         print("dept",self.dept)
#         print("salary",self.salary)
# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("hr","cse",75000)
# e1=Engineer("sam",67)
# e1.showDetails()

class Order:
    def __init__(self,item,price):
     self.item=item
     self.price=price

    def __gt__(self,odr2):
       return self.price > odr2.price
odr1=Order("chips", 20)
odr2=Order("tea",15)

print(odr1>odr2)