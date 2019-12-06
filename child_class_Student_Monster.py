# Should have a uni id and a grade

# Import the Monster parent class
from parent_class_Monster import  *

class Student_Monster(Monster):

# Monster Atrributes
    def __init__(self, monster_name, skills,uni_id, grade = 'C'):
        super().__init__(monster_name, skills)
        self.__uni_id = uni_id
        self.__grade = grade

# Monster Methods

    def get_uni_id(self):
        return self.__uni_id

    def get_grade (self):
        return f'This is your Monster Grade: {self.__grade}'

    def set_grade(self, grade):
         self.__grade = grade

# name = input('What is your name?')
# skill = input('What is ur skill?  ')
#
# little = Student_Monster(name, skill, 101, 3)
# print(little.get_uni_id())
# print(little.get_name())