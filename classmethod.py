class PythonLearn:
    number = 100 #class variable

    def __init__(self, a, b):
        self.number1 = a
        self.number2 = b



    def methodlearn(self):
        print("Method learning is in progress")

    def sum(self):
        return self.number1 + self.number2 + self.number

##obj1= PythonLearn()
##obj1.methodlearn()

obj2= PythonLearn(10,20)
print(obj2.sum())