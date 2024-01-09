#EX1
arithmeticExpression=input("Enter arithmetic expression: ")
parts=arithmeticExpression.split()
result=" "
if len(parts)==3:
    num1=int(parts[0])
    operation=parts[1]
    num2=int(parts[2])
    if operation=='+':
       result=num1+num2
    elif operation== '-':
        result=num1-num2 
    elif operation=='*':
        result=num1*num2 
    elif operation=='/':
        if num2!=0:
            result=num1/num2
        else:
            result="Enter corect num2:"
    else:
        result="Enter corect expression"        
    print("Result of arithmetic expression: ", result)
#EX2
# import random
# list1=[random.randint(-10,20) for i in range(5)]
# print(list1)
#1
# print(list1[0])
# print(list1[4])
# #or
# print(max(list1),min(list1))
# #2
# count=0
# for num in list1:
#     if num<0:
#         count+=1
# print(count)
# #3
# count=0
# for num in list1:
#     if num>=0:
#         count+=1
# print(count)
# #4
# count=0
# for num in list1:
#     if num==0:
#         count+=1
# print(count)






