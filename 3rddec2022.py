#lamda funtion,map(),reduce(),filter()
#void==ananomus funstion
x = lambda a: a+ 10
print(x(20))

#Object oriented programming(oops)
#abstraction==hidding of irrrelevant data input and output
#encapsulation==bring all data in onegroup
#polymorphism==which has maney forms===capable of multitasking
#inheritance===aquring some propeerties
#these all are independent
#1.class==eg mobile phone/car blue print
#2.Object== 

class Car:
    h = 10
    w=20

JAGUAR = Car()
ferrari = Car()
TATA = Car()
print(JAGUAR.h)
print(JAGUAR.w)
print(ferrari.h)
print(TATA.h)

'''1.init helps the class initialize object's attribute.
And is called everytime an object is created from a class 
2.By using self keyword you can easily acess all the objects defiend within the class  including funtion ''' 
class  Student :
    def __init__(st,name,reg):  #parametarized funtion
        st.name = name
        st.reg = reg

bhai = Student("Anurag", 4115007)
print(bhai.name)
print(bhai.reg)                 

class Student:
    def __init__(self,name,reg):
        self.name = name
        self.reg = reg
    '''all the variables and all are the members of class'''
    def pr(self):
        print("Hello my name is "+self.name)
obj = Student("Aravind",12219443)
obj.reg = 4115008

print(obj.reg)
#greener chart

