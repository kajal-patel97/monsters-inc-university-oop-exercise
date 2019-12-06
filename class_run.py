#import the approriate class to run this.
from child_class_Student_Monster import *


# In this run i will be able to create a monster student with a name and id

print('Welcome to the enrollment of Monsters University!')
name = input('What is the name of the Monster you want to enroll? ')
skills = input('Please list your current skills  ')
uni_id = int(input('Please assign this monster with an ID....'))

creating_a_monster = Student_Monster(name, skills, uni_id)
print(f'The Monster you are enrolling is {creating_a_monster.get_name()}')
print(f'Skills: {creating_a_monster.get_skills()}')
print(f'Uni ID: {creating_a_monster.get_uni_id()}')