#class with construction
class Human:
    def __init__(self,name,age,ethnicity,gender,height):
        self.name=name
        self.age=age
        self.ethnicity=ethnicity
        self.gender=gender
        self.height=height
    def __str__(self):
        return f'{self.name} \t{self.age} \t    {self.ethnicity} \t {self.gender} \t \t{self.height}cm'
    


person1 = Human('Asad',30,'Bangali','Male',175)



#inheritance in class

class UNMilitary(Human):
    def __init__(self,name,age,ethnicity,gender,height,state,rank):
        super().__init__(name,age,ethnicity,gender,height)
        self.state=state
        self.rank=rank
    def __str__(self):
        return f'My Name is {self.name} I am {self.age} Old from  {self.state} \nI am a {self.rank} In UN Task Force !'
    

major1=UNMilitary('Muhammad Ali',33,'Bangali','Male',178,'Bangladesh','Major General')

print(major1)