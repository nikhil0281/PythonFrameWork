from classmethod import PythonLearn


class PythonInheritance(PythonLearn):
    classvar = 500

    def __init__(self):
        PythonLearn.__init__(self,100,200)

    def Inherimethod(self):
        return self.number+self.number1+self.number2+PythonInheritance.classvar


PiObj = PythonInheritance()
print(PiObj.Inherimethod())