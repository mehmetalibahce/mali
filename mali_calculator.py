#Mehmet Ali Hesap Makinesi

class Calc(object):
    
    #init metodu
    def __init__(self,a,b):
        "initialize values"
        self.value1=a
        self.value2=b
    
    #toplama
    def plus(self):
        "addition a+b"
        result=self.value1+self.value2
        return result
    
    #cikarma
    def minus(self):
        "differance a-b"
        result=self.value1-self.value2
        return result
    
    def multiply(self):
        "multiplication a*b"
        result=self.value1*self.value2
        return result
    
    def divide(self):
        "division a/b"
        result=self.value1/self.value2
        return round(result,2)

print("Choose Operation (1:Plus 2:Minus 3:Multiply 4:Divide)")
operation=input("Please press operation code (1,2,3,4) from keyboard:  ")


v1=input("First Value: ")
v2=input("Second Value: ")
c1=Calc(float(v1),float(v2))

if operation=="1":
    print("Addition Result={}".format(c1.plus()))
elif operation=="2":
    print("Subtraction Result={}".format(c1.minus()))
elif operation=="3":
    print("Multiplication Result={}".format(c1.multiply()))
elif operation=="4":
    print("Division Result={}".format(c1.divide()))
else:
    print("There is no proper selection. Please try again.")