#EX1
def productList(list1):
    product=1
    for i in list1:
        product *= i
    return product
list2=[2,3,4,5]
result=productList(list2)
print(f'Product: {result}')
productList(list2)
#EX2
def minList(list1):
    return list3
list2=[6,2,3,4] 
list3=min(list2)
minList(list3)
print(list3)
#EX3
def primeNumbers(list1):
    count=0
    for num in list1:
       if num>1:
        primeNumber=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
               primeNumber=0
        count+=primeNumber
    print(count)
    return count
list1=[3,5,7,11,13,15,17,18]
countPrime=[]
primeNumbers(list1)
#EX4
def deliteNumber(list):
    return countNumber

list1= ["1","2","3","4"]
count=len(list1)
list2=list1.remove("2")
count1=len(list1)
countNumber=count-count1
print(countNumber)
deliteNumber(countNumber)
#EX5
def threeList(list3):
    return list3
list1=[1,2,3,4]
list2=[5,6,7,8]
list3=list1+list2
print(list3)
threeList(list3)
#EX6
def numberInPower(power,list0):
    list1=[]
    for i in list0:
       list1.append(i**power)
    print(list1)
    return list1
list0=[1,2,3]
power=3
numberInPower(power,list0)


