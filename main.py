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
a={1,2,3,4,5}
b={4,5,6,7,8}
s= a|b
print(s)


