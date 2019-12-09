# as a uni admin i want to be able to add a student to a spooky workshop so that the workshops has a student

#import appropriate class
from parent_class_Spooky_Workshops import *
scaryclass = Spooky_Workshops('Maths', 'Ben', 'London', 1)

prompt_to_add = input('What students would you like to add to the workshops?  ')
added_students = scaryclass.adding_student_to_workshop(prompt_to_add)


print(f'You have added: {scaryclass.list_of_students[]}')