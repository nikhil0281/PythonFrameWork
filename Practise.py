from PythonMainClass import PythonMainClass


class Practise(PythonMainClass):

    Dict={}
    List10=[]
    List11=()


    def Practisemethod(self):
        List10 = PythonMainClass.List123
        List11 = tuple(PythonMainClass.List789)
        Dict = {List10[0]: List11[0]}
        print(List10)
        print(List11)
        print(Dict)

PracOb = Practise()
PracOb.Practisemethod()

