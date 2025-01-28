
class Math():
    def max(nums):
        x=0
        for n in nums:
            if n>x:
                x=n
        return x
    def min(nums):
        x=100000000000000000000
        for n in nums:
            if n<x:
                x=n
        return x
print(Math.min([1,21,5,6,7,8,19,0]))
print(Math.max([1,21,5,6,7,8,19,0]))


class Square():
    def __init__(self,height="0",width="0"):
        self.height=height
        self.width=width
    @property
    def height(self):
        print('retriving height')
        return self.__height
    @height.setter
    def height(self,value):
        if value.isdigit():
            self.__height=value
        else:
            print('Only numbers')
    @property
    def width(self):
        print('Retriving width')
        return self.__width
    @width.setter
    def width(self,value):
        if value.isdigit():
           self.__width=value
        else:
            print('Only numbers')
    def get_area(self):
        return int(self.__height)*int(self.__width)

square=Square('10','10')
#square.height='20'
#square.width='10'

print("Area : ",square.get_area())
''''''
class Employee():
    def __init__(self,name='unknown',age='0',gender='unknown',position='unknown',joinYear='2011'):
        self.name=name
        self.age=age
        self.gender=gender
        self.position=position
        self.joinYear=joinYear
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name=value
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        self.__age=value
    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self,value):
        self.__gender=value
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self,value):
        self.__position=value
    @property
    def joinYear(self):
        return self.__joinYear
    @joinYear.setter
    def joinYear(self,value):
        self.__joinYear=value
    @property
    def workingYears(self):
        import datetime
        return datetime.datetime.now().year-int(self.__joinYear)
    def __str__(self):
        return "{} working for {} years as an {}".format(self.__name,self.workingYears,self.__position)
    
                   
employee = Employee("Asad",26,"Male","Computer Programmer","2016")

print(employee)

#inheritance 

class Animal():
    def __init__(self,name='unknown',weight=0,color='brown'):
        self.__name=name
        self.__weight=weight
        self.__color=color
    @property
    def name(self):
        return self.__name 
    def __str__(self):
        return "{} this from {}".format(self.name,type(self).__name__)
    def __gt__(self,ani2):
        if self.__weight>ani2.__weight:
            return True
        else:
            return False

'''
=========Magic Method=========

__eq__   : Equal
__ne__   : Not Equal
__gt__   : Greater Then
__lt__     : Less Then
__ge__   : Greater then or Equal
__le__     : Less then or Equal
__add__  :  Addition 
__sub__  : Subtraction
__mul__  : Multiplication
__div__   : division
__mod__ : modulus
'''
class Dog(Animal):
     def __init__(self,name='unknown',weight=0,color='brown',owner='unknown '):
         Animal.__init__(self,name,weight,color)
         self.__owner=owner
     def __str__(self):
          return super().__str__ ()+" owened by "+self.__owner



    
animal = Animal('Spot',242,'black')
dog=Dog('dev',234,'white','denial')
print(dog)   
print(animal>dog)












