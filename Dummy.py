from collections import defaultdict
d = defaultdict(list)

list3 = [1,2,4,3,4,3]
list4 = ['a','b','c','d','e','f']

for k,v in zip(list3, list4):
    d[k].append(v)

print(d)