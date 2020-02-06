class Person: #class for the example individuals
    def __init__(self,name,age,food,occupation):
        self.name = name
        self.age = age
        self.food = food
        self.occupation = occupation

    def introduction(self):
        print('My name is', self.name, 'and I am', self.age, 'years old. I am a', self.occupation, 'and I love to eat' ,self.food)
        
