#creating a class

class MyClass:
    x=19

#creating an object for the class

obj1 = MyClass()

'''whenever we create an object or the class in intiated then the init method is
executed'''

class MyClass2:
    def __init__(self,p):
        self.x=19
        print(self.x)
        print(p)

obj2 = MyClass2(3)

#object methods
    
class MyClass3:
    def __init__(self):
        self.a=8
    def prin(self):
        print(self.a)

obj3 = MyClass3()
obj3.prin()
''' there must be self parameter in any object and in init method which is a
reference to the current instance of the class, and is used to access variables
that belongs to the class.'''
'''It does not have to be named self , you can call it whatever you like, but it
has to be the first parameter of any function in the class'''

class MyClass4:
    def __init__(anything):
        anything.any = 'your wish'
    def prin(select):
        print(select.any)

obj4 = MyClass4();
obj4.prin()

#Modify Object Properties

obj4.any = 19
obj4.prin()

#Delete Object Properties

del obj4.any

'obj4.prin()# any way this statement gives error'

#Delete Objects

del obj4
