List1 = [1, 2, 3, 4]
Tupple1 = (11, 12, 13, 14)
Dict1 = {"a": "Capital A", "b": "Capital B", 3: "Three Number"}
Dict2 = {}
if List1[0]== 9:
    print("List 0th Positon number is 1")
elif Tupple1[1]== 2:
    print("Tupple 1st number is 12")
elif Dict1["a"]== "Capital A":
    print("Dictonary is in progress... ")
    List1 = [1, 10, 1, 4]
    Tupple1 = (11, 12, 13, 14)
    Dict1 = {"a": "Capital A", "b": "Capital B", 3: "Three Number"}

if List1[0] >= Tupple1[0]:
        print("List 0th Positon number is 1")
elif List1[1] < 2:
        print("List 1st number is 2")
else:
    print("number doesn't match")
    Dict2[List1[0]] = Tupple1[0]
    Dict2[List1[1]] = Tupple1[1]
    Dict2[List1[2]] = Tupple1[2]
    Dict2[List1[3]] = Tupple1[3]
    print(Dict2)

