from collections import defaultdict

from PythonMainClass import PythonMainClass


class StringLearn(PythonMainClass):
    Str12 = "I love"


    def strmethod(self):
        Str10 = PythonMainClass.Str
        Str11 = PythonMainClass.Str1
        Str11len = len(Str11)
        Dict={}
        List = []

        List1 = list(Str11)
        List2 = list(Str10)
        tupple1 = tuple(List2)
        print(List1)
        print(tupple1)
        d = defaultdict(list)

    #    if StringLearn.Str12 in Str11:
    #        return Str10+Str11

        for k, v in zip(List1, List2):
            d[k].append(v)
        print(d)
        print("End of code execution")



Obj1 = StringLearn()
print(Obj1.strmethod())