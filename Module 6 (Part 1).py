#EX1
# from colorama import Fore, Back, Style, init
# init()
# def myText():
#     print(Fore.LIGHTBLACK_EX
#     +"\" Dont compare yourself with anyone in this world...")
#     print(Fore.RED+'if',Fore.WHITE+'you', Fore.RED+'do so', Fore.WHITE+"you are insulting yourself",Fore.LIGHTBLACK_EX+'\"',Fore.WHITE+'\nBill Gates')
# myText()
#EX2
# def myNumber(a,b):
#     for i in range(a,b+1):
#         if i %2==0:
#             print(i)
# myNumber(2,8)
#EX3
def square(side,symbol,full):
    if full:
        for i in range(side):
            print(symbol*side)
    else:
        print(side*symbol)
        for i in range(side-2):
            print(symbol+' '*(side-2)+symbol)
        if side>1:
            print(symbol*side)
square(5, '*', False)
#EX4
# def minNumber(list1):
#     list2=min(list1)
#     print(list2)
# list1=[5,2,6,4,7]
# minNumber(list1)
#EX5
# def productNumber(a,b):
#     if a>b:
#         a,b=b,a
#     product=1
#     for i in range(a,b+1):
#         product*=i
#     print(product)
# productNumber(2,6)
#EX6
# def countNumber(number):
#     count=len(str(number))
#     print(count)
#     return count
# number=2341
# countNumber(number)
#EX7
# def polindromWord(number):
#     number1=str(number)
#     polindrom=number1[::-1]
#     return number1==polindrom
# result=polindromWord(1221)
# print(result)
# polindromWord(result)
      

              


    