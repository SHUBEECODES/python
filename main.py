# print("namastey to everyone, we are learning python")

# #this is a comment
# """this is a multiline commenting , using Doc string . 
# python does not support multiline commenting , but we achieve it with the help of doc dtring"""

# Name = "Shubhangi"
# Age = 22

# #Naming Convention - 3ways
# sheriyansSchool = "students"  #camel case
# SheriyansSchool = "students" #pascal case
# sheriyans_school = "students" #snake case

# #datatypes

# #number
# a=12 #integer
# b=5.4 #float-decimal
# c=12/3 #float-fraction(any number which can be written in the form of p/q is a fraction, thus float)
# d=34j #complex

# #string- anything within"" or ''
# st = "ahsgdhdi  38e9w8e28  @#$%"

# #boolean- True or False - T and F capital
# b = True
# t = False
# print(type(t))

# #string takes more space than other data types because it stores every character with its unicode
# a = "A"
# print(ord(a)) #ord is used to get unicode
# print(chr(65)) #chr is used to get character from the unicode

# #indexing , positive idx starts from 0 and negative from -1 from the last element
# a="SHER"
# print(a[0])
# print(a[-1],a[3])

# #string indexing
# #a[start,stop(idx needed+1),step]
# a="SHER CODER"
# print(a[0:4:1])
# print(a[5:11:1])
# print(a[-1:-6:-1])
# print(a[::]) #default start=0, stop=last idx+1, step=1

# #Type conversion
# # function : int() , str(), float(),bool()
# a=12
# a = str(12)
# print(type(a))

# a=333
# print(bool(a))
# a=0.0
# print(bool(a)) #7 falsey values 0,0.0,"",{},[],(),False

# a=12 #int
# print(a/2) #float in the form of p/q therefore answer=6.0 -- implicit type conversion


# name="shubhangi"
# age=22
# print("Name=",name,"Age=",age)
# print(f"Name={name},Age={age}") #formatted string there is also a raw string

# age = input("What is your Age?")
# print(age)

#arithmetic operators -- python follows BODMAS
# a=12
# b=2
# print(a/b)
# print(a//b) #floor division, no value after decimal, to integer converted
# print(a+b)
# print(a-b)
# print(a*b)
# print(a**b) #exponential,power
# print(a%b)

#Assignment operator
#most basic, =

#compound assignment operations,comination of arithmetic and assignment
# a=20
# a+=20
# print(a)
# a-=10
# print(a)
# a*=2
# print(a)
# a/=10
# print(a)
# a=6.333
# a//=2
# print(a)

#comparison operator -- answer will be boolean, string can only be compared with string(ASCII)
# print(20<40)
# print(20!=20)
# print(20<=20)
# print(12.1>12)
# print("ABC">"BCD")

#logical operators--and,or,not
# print(12!=12 or 78>9 )
# print(22<44 and 66<88 and 90>100)
# print(not 12==12)

# print(126>130) #false
# print((456==456)!=(235==236)) #true
# print(12<10 or 45==56 or 69>70 or 15!=13) #true
# print(True and bool(0)) #false

#IF-ELSE -- spaces left before print is identation
# a=2
# if a>10:
#     print("i will do task A")
# else:
#     print("i will do task b")


# money =  int(input("Mom , please give me the money"))
# if money<=10:
#     print("i will buy chocobar")
# elif money<=20 and money>10:
#     print("i will have a mango dolly")
# else:
#     print("i will  buy a chocolatecone")

#QUESTIONS
# num1 = int(input("enter number1:"))
# num2 = int(input("enter number2:"))
# if num1>num2:
#     print(num1)
# else:
#     print(num2)

# gender = (input("Please tell your gender as (M or F):"))
# if gender=="m" or gender=='M':
#     print("Good Morning Sir")
# elif gender=="f" or gender=='f':
#     print("Good Morning Ma'am")
# else:
#     print("Good morning to you")

# num=int(input("Please enter a number:"))
# if num%2==0:
#     print("the number is even")
# else:
#     print("the number is odd")

# name=input("Please enter your name:")
# age=int(input("please enter your age"))
 
# if age>=18:
#      print(f"hello {name} you are a valid voter")
# else:
#      print(f"hello {name},you are not a valid voter")
#      print(f"you can vote after{18-age}years")

# year = int(input("enter a year"))
# if year%4==0 and (year%100!=0 or year%400==0):
#     print(f"{year} is a leap year")
# elif year%100==0 and year%400==0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# temp = int(input("enter temprature"))
# if(temp<0):
#     print("freezing cold")
# elif temp>=0 and temp<10:
#     print("very cold")
# elif temp>=10 and temp<20:
#     print("cold")
# elif temp>=20 and temp<30:
#     print("pleasant")    
# elif temp>=30 and temp<40:
#     print("hot") 
# else:
#     print("very hot")   
  
    #FOR LOOP
# n = int(input("which number's table you want to print?"))
# for i in range(1,11,1):
#     print(f"{n}x{i}={n*i}")

#LOOPS ON STRINGS
# a="my name is shubhangi"
# for i in range(len(a)):
#     print(a[i])

    #direct iteration on string
# for i in range(1,21,1):
#    if i==15:
#       continue
#    print(i)
    
#FOR LOOP QUESTIONS

# n = int(input("enter an integer"))
# sum=0
# for i in range(2,n):
#     if(n%i==0 ):
#        print("not prime")
#        break
# else:
#     print("prime")   

# a="abcba"
# s=(a[-1:-(len(a)+1):-1]) 
# # print(s)
# if(a==s):
#     print("palindrome")
# else:
#     print("not a palindrome")

# a= input("enter a string")
# char=0
# digits=0
# symbols=0
# for i in range(len(a)):
#     if(ord(a[i])>=65 and ord(a[i])<=90 or (ord(a[i])>=97 and ord(a[i])<=122)):
#         char+=1
#     elif(ord(a[i])>=48 and ord(a[i])<=57):
#         digits+=1
#     else:
#         symbols+=1
# print(f"char={char}")  
# print(f"digits={digits}")
# print(f"symbols={symbols}")    

#while loop
# a=1
# while a<=30:
#     print(a)
#     a+=1

# num = int(input("enter a number : "))
# n=num 
# rev=0
# while num>0:
#     rev=rev*10+num%10
#     num=num//10
# if n==rev:
#     print(f"{n} is a palindrome")
# else:
#     print(f"{n} is not a palindrome")   


#WHILE LOOP NUMBER GUESSING GAME
  
# import random

# num = random.randint(1,20)



# tries=0

# while True:
#     guess = int(input("Please guess the number : "))

#     if num==guess:
#         print(f"Yayy , you have guessed the number in {tries} tries ")
#         break
#     elif num>guess:
#         print(f"Think of a higher number")
#         tries+=1
#     elif num<guess:
#         print(f"Think of a little lower number")
#         tries+=1
#     else:
#         print("sorry you are wrong")
#         tries+=1
        



#FUNCTIONS
# def hello():
#     print("Hi , All")

# hello()

# def sum(a,b):
#     print(f"sum = {a+b}")

# sum(12,122) 


# def palindrome(st):
#    rev=""
#    for i in range(len(st)-1,-1,-1):
#       rev+=st[i]
      
#       if rev==st:
#         print("palindrome")      



# palindrome(input("enter string"))

#LIST

# a=[12,13,14,15,16,17.6]
# print(a)
# a[1]=19
# print(a)

#index traversing
# for i in range(1,len(a),1):
#     print(i,a[i])

#direct traversing
# for i in a:
#     print(i)    

#List functions

# l=[1,2,3,-4,5,-6,7,-8,9,-10]
# a=[]
# b=[]
# for i in l:
#     if i>0:
#         a.append(i)
#     else:b.append(i)
#MEAN OF ELEMENT IN LIST
# l=[1,2,3,4,5]

# sum=0
# for i in l:
#     sum+=i
# print(sum//len(l)) 

# l=[1,2,3,4,5]
# max=l[0]
# secmax=l[0]
# for i in l:
#     if i>max:
#         secmax=max
#         max=i
#     elif i>secmax:
#         secmax=i

# print(f"largest={max} and second largest={secmax}")
# 
# SORTED OR NOT
# for i  in range(len(l)-1):
#     if l[i]>l[i+1]:
#         print("not sorted")
#         break
# else:
#     print("sorted")  

#TUPLE

# a=(1,2,3,4,5,4,4,5.5)
# print(type(a))
# print(a.index(3))
# print(a.count(4))

#tuple unpacking
# a,b,c,d=(1,2,3,4)
# print(a,b,c,d)

# a=(1,) #type of a is typle but for a=(1) it is int
# print(type(a))

#SET
 #hash() function
# a = "hello"
# print(hash(a))

# a={1,2,3,4,5}
# a.clear()
# print(a)

#ADVANCED SET FUNCTIONS
# a={1,2,3,4,5}
# b={4,5,6,7,8}
# s= a^b
# print(s)


#DICTIONARY
# d={1:"hello",2:56}
# print(d[2])
# d={1:10,2:20,3:30,4:40}
# #CRUD OPERATIONS
# d[5]=50 #create
# d[1]=100 #update
# del d[4] #deletion
# print(d)
 
#DICTIONARY TRAVERSING
# d={1:10,2:20,3:30,4:40}
# for i in d:
#     print(i) #keys
# for i in d:
#     print(d[i]) #values
# for i in d.values():
#     print(i)    #another way to access values    

#DEEP COPY
# a=[1,2,3,4,5]
# b=a.copy()
# b[0]=100
# print(a)

# d1={1:10,2:20,3:30}
# d2={4:40,5:50}

# for i in d2:
#     d1[i]=d2[i]
# print(d1)    TO MERGE TWO DICTT
# d={10:100,20:200,30:300,40:400,50:500,60:500}
# a=[1,1,1,1,2,2,3,3,4,4,5,5,5,6,6]
# di={}
# count=1
# for i in range(0,len(a)-1,1):
#     if a[i]==a[i+1]:
#         count+=1
#     else:
#         di[a[i]]=count
#         count=1
# di[a[i]]=count
# print(di)         
# d={}
# for i in a:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d) 
# 
# d1={10:100,20:200,30:300}
# d2={20:400,30:500,50:700}
# for i in d2:
#     if i in d1:
#         d1[i]=d1[i]+d2[i]
#     else:
#         d1[i]=d2[i]   
# print(d1)   
# 
# EXCEPTION HANDLING
# a = int(input("enter your number"))
# try:
#     print(10/a)
# except Exception as err:
#     print(f"you cannot divide a number by {err}")
# else:
#     print("good no error occured")
# finally:
#     print("i will run no matter what")


#RAISE 
# age = int(input("enter your age"))
# try:
#     if age>18 or age<10:
#         raise ValueError("age must be between 10 and 18")
#     else:
#         print("welcome to the club")
# except Exception as err:
#     print(f"{err} occured")


# print("all done")    
 #FILE HANDLING
# p = open('main.py')
# print(p.read())

# r = open('sup.txt','w') # 'w'writes inside the file and if we change it it will change the statement so, we will append it
# r.write("Hello my name is Shubhangi and i am writing inside this file") 
# r.close()

# r = open('sup.txt','a')
# r.write("i am appending some content")
# r.close()

# r = open('batman.txt','x') # 'x' just creates a new file
# r.close()


#FOUR MODES IN OPEN IN FILE HANDLING - 'r','w','a','x'

#OOPS IN PYTHON
# class Factory:
#    a = 12

#    def hello(self):
#       print("Hello, how are you!!")

# print("hello i am getting initialised")

# obj = Factory()
# print(obj.a) 
# obj.hello()
   
# class Factory:
#     def __init__(self,material,zips,pocket):
#         self.material = material
#         self.zips = zips
#         self.pocket = pocket

#     def show(self):
#         print(f"your details are :- {self.material},{self.pocket},{self.zips}")    


# reebok = Factory("Polyster",3,2)
# campus = Factory("nylon",2,3)

# print(reebok.material)

# class Animal:
#     name = "Lion" #class attribute

#     def __init__(self,age):
#         self.age = age  #instance attribute

#     def show(self):
#         print(f"how are you , my age is {self.age}") #instance method

#     @classmethod
#     def hello(cls):
#         print("hello how are you") #class method 

#     @staticmethod
#     def static():
#         print("hello all")      #static method


# obj = Animal(12)
# obj.static()

#INHERITANCE

# class Factory: #parent class/super class
#     def __init__(self,name):
#         self.name = name
#     a="Hello i am a Factory"
#     def show(self):
#         print(f"hello my name is {self.name}")

# class FactoryMumbai(Factory): #child class/ sub class
#     def __init__(self, name,age):
#         super().__init__(name) #it will be the same initialised to parent constructor
#         self.age= age

# obj = FactoryMumbai("shubhangi",22)  #constructer can be accessed
# obj.show() #methods can be accessed
# print(obj.a) #attributes can also be accessed by child class


#MULTIPLE INHERITANCE
# class Animal:
#     name1="lion"
#     def __init__(self,name):
#         self.name = name
# class Human:
#     name2="Shyam"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Robots(Animal,Human): #since Animal is inherited first , therefore its constructor will be called first. If human is inherited first then its constructor will be called
#     name3 = "Charlie123"

# obj =  Robots()
# print(obj.name3)            



      #MULTILEVEL INHERITANCE

# class Factory:
#     def __init__(self,material,zips):
#           self.material = material
#           self.zips = zips

# class BhopalFactory(Factory):
#      def __init__(self, material, zips,color):
#           super().__init__(material, zips)
#           self.color = color

# class PuneFactory(BhopalFactory):
#      def __init__(self, material, zips, color,pockets):
#           super().__init__(material, zips, color)
#           self.pockets = pockets


# obj = PuneFactory()    

#POLYMORPHISM
# METHOD OVERRIDING

# class Animal:
#     def show(self):
#         print("Hello how are you")
# class Human(Animal):
#     def show(self):
#         print("My name is Shubhangi")

# obj = Human()
# obj.show()   #the method of the child class will override the method of the parent class when the method name is same in both parent class and child class  
# 

#ENCAPSULATION
# PUBLIC ACCESS MODIFIERS AND PROTECTED
# class Pune:
#     a="pune"
#     _b = "I am pune factory" #PROTECTED SINCE IT IS WITH AN UNDERSCORE , BUT IT IS THE SAME AS PUBLIC
#     __c = "I am a private attribute" #PRIVATE ATTRIBUTE USING A DOUBLE UNDERSCORE

#     def sh(self):
#         print(Pune.__c) #private attribute is accessed inside the class only , using the class

# class Bhopal(Pune):
#     def show(self):
#         print(super().a)  # this is normally public access modifier use. Not the use of super().a but just to show that all the methods and attributes are accessible     

# obj = Bhopal()
# obj2 = Pune()
# obj2.sh()

#ABSTRACTION

# from abc import ABC,abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass

#     @abstractmethod
#     def area(self):
#         pass

# class Square(abstract):
#      def perimeter(self,side):
         
#          print("i calculate perimeter")  

#      def area(self,side):
#          print("i calculte area")

# obj = Square() 
# obj.area(2)       
# 
# DUNDER METHODS
class Animal:
    def __init__(self,name,age): #initialization dunder method, we have already seen
        self.name=name 
        self.age=age 
    def __str__(self): #dunder method of string
        return f"The name of your Animal is {self.name}"   
    # def __add__(self,other):
    #     return f"The sum of ages is {self.age+ other.age}"
    def __add__(self,other):
        sum=0
        for i in other:
            sum+=i.age
        return f"the sum of the age is {self.age+sum}"    

    
obj = Animal("Lion",12)
obj2 = Animal("tiger",22)
obj3 = Animal("Monkey",13)
print(obj+(obj2,obj3))  #here we have passed obj2 and obj3 in the form of tuple

