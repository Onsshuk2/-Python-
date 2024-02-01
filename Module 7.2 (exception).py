#EX1
name=input("Enter your name: ")
try:
   age=int(input("Enter your age: "))
   if  age<0 or age>130:
    raise ValueError ()
   print(f"Hello, {name}! Your age - {age}.")
except ValueError as e:
  print("Enter corect age", name)
#EX2
def userInfo(name,age):
    return f"Hello, {nameOfUser}! Your age - {ageOfUser}."
nameOfUser=input("Enter your name: ")
try:
   ageOfUser=int(input("Enter your age: "))
   if  ageOfUser<0 or ageOfUser>130:
    raise ValueError ()
   print(f"Hello, {nameOfUser}! Your age - {ageOfUser}.") 
except ValueError as e:
  print("Enter corect age", nameOfUser)
userInfo(nameOfUser,ageOfUser)
def userInfo(name,age):
   try:
      if  age<0 or age>130:
       raise ValueError ()
      print(f"Hello, {name}! Your age - {age}.")
   except ValueError as e:
      print("Enter corect age", name)
      return f"Hello, {name}! Your age - {age}."
nameOfUser=input("Enter your name: ")
ageOfUser=int(input("Enter your age: "))
userInfo(nameOfUser,ageOfUser)
#EX3
list1=list()
try:
   for i in range(3):
      numbers=int(input("Enter number: "))
      if numbers<0:
         raise ValueError ()
      list1.append(numbers)
except ValueError as e:
   print(" Enter number > 0")
else:
   print(sum(list1))
#EX4
def sumList(list1):
    return sum(list1)
list1=list()
try:
   for i in range(3):
      numbers=int(input("Enter number: "))
      if numbers<0:
         raise ValueError ()
      list1.append(numbers)
except ValueError as e:
   print(" Enter number > 0")
else:
   print(sum(list1))

sumList(list1)

def sumList():
    list1 = []
    try:
        for i in range(3):
            num = float(input("Enter number : "))
            if num < 0:
                raise ValueError()
            list1.append(num)
    except ValueError as e:
        return f" Enter corect number"
    return sum(list1)


result = sumList()
if isinstance(result, str):
    print(result)
else:
    print(result)


    
            

  
