print("Hello")
a = "ABCD"
print(a)
a, b, c, d = 1, 2.5, "Nikhil Mathur", "My name is :"
print(a)
# print(d+b)
print("{}{}".format(d, b))
e = "{}{}".format(d, b)
print(e)
print(type(b))

values = [1, 2, "Nikhil", 3, 4, 6.7]
print(values[-1])
print(values[2])
print(values[1:4])
values.append("Mathur")
print(values)
values.insert(6,"Shipra")
print(values[-1])

TuppleVal = (1, 2, 3, 4, "Nikhil")
print(TuppleVal)

DicVal={"a":1, "b":"Capital B", 2:"Number"}
print(DicVal[2])
DicVal1={}
DicVal1["A"]="Capital A"
DicVal1["B"]='Capital B'
print(DicVal1["B"])
