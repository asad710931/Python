


class Apple:
    def __init__(self,color,taste,weight):
        self.color=color
        self.weight=weight
        self.taste=taste
    def __str__(self):
        return f"Color of you Apple is {(self.color)} \n Taste {self.taste} \nAnd weight about {self.weight}"
    def origin(self):
        if(self.taste=='sweet' and self.color=='golden'):
            return 'Canada'
        elif(self.taste=='sweetest' and self.color=='red'):
            return 'Australia'
        else:
            return 'Not Match'


myapple = Apple("golden","sweet",12)
myapple1 = Apple("red","sweetest",7)

print(myapple)

print(myapple.origin())
print(myapple1.origin())

class Human:
    def __init__(self,name,age,ethnicity,gender,height):
        self.name=name
        self.age=age
        self.ethnicity=ethnicity
        self.gender=gender
        self.height=height
    def __str__(self):
        return f'{self.name} \t{self.age} \t    {self.ethnicity} \t {self.gender} \t \t{self.height}cm'
        
print('Name |\tAge  | Ethnicity |\tGender  |\tHeight')
print("-----+-------+-----------+----------+------------------|")
person1 = Human('Asad',24,'Bangali','Male',178)

person2 = Human('Aamir',19,'Pakistani','Male',168)

person3 = Human('Hakeem',33,'Egyptian','Male',170)

person4 = Human('Omar',29,'European','Male',185)

    
print(person1)
print("-----+-------+-----------+----------+-------------------|")
print(person2)
print("-----+-------+-----------+----------+-------------------|")
print(person3)
print("-----+-------+-----------+----------+-------------------|")
print(person4)
print("-----+-------+-----------+----------+-------------------|")
    


