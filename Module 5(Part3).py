import random
list1=[random.randint(1,20) for i in range(5)]
list2=[random.randint(10,25) for i  in range(5)]
print(list1)
print(list2)
#1
# list3=list1+list2
# print(list3)
# #2
# list3=list1+list2
# print(set(list3))
#3
# list3=[]
# for i in list1:
#     if i in list2:
#        list3.append(i)
# print(list3)
#4
set1=set(list1)
set2=set(list2)
list3=list(set1.intersection(set2))
print(list3)
#or
list3=[set1,set2]
print(list3)
#5
# list3=min(list1),min(list2),max(list1),max(list2)
# print(list3)