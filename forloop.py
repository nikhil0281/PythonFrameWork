Dict1={}
list1=[11,12,13,14,15,16]
List2={21,22,23,24,25,26}
a = len(list1)
print("{}{}".format("Length of list is ", a))  # this is use concatinate two strings

Tupple1 = tuple(List2)
print(Tupple1)

Dict2={zip(list1,List2)}
print(Dict2)

#for i in range(1,a+1):
   # Dict1[list1[i-1]] = List2[i-1]
print(Dict1)