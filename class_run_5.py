from parent_class_Spooky_Workshops import *
from child_class_Student_Monster import *


# Ask for information
# evaluate information
# say which option you chose
# I should be able to create a monster
# List all workshops
# Add student to spooky workshop
# I should be able to see students grade
# print full information of student
# search for student by name
monster1 = Student_Monster('Ant', '101', 'C')
monster2 = Student_Monster('Bee', '102', 'A')
monster3 = Student_Monster('Dave', '103', 'B')
monster4 = Student_Monster('Stace', '104', 'A')
student_list = []
student_list.extend([monster1, monster2, monster3, monster4])

workshop1 = Spooky_Workshops('Maths', 'Joe', 'London', '1')
workshop2 = Spooky_Workshops('Scare Attack', 'Craig', 'Miami', '2')
workshop3 = Spooky_Workshops('Theory', 'Penny', 'London', '3')
running_workshops = []
running_workshops.extend([workshop1, workshop2, workshop3])

while True:
    print('Please select from the following...')
    print('1 -- Create a Monster')
    print('2 -- List all workshops ')
    print('3 -- Add student to Spooky Workshop')
    print('4 -- See student grades')
    print('5 -- See all student information ')
    print('6 -- Search for a student ')

    option = input('Please select an option number?  ')

    if option == '1':
        print('You have selected option 1 - Create a Monster ')
        name = input('What is the students name you want to add? ')
        id = input('What is there ID?  ')
        grade = input('What is their grade?  ')
        print('Thank you!')
        new_student = Student_Monster(name, id, grade)
        print('Well Done, You created a Monster called ', new_student.get_name())

    elif option == '2':
        print('You have selected option 2 - List all workshops ')
        for subject in running_workshops:
            print(subject.scary_subject)

    elif option == '3':
        print('You have selected option 3 - Add student to Spooky Workshop')
        # select student
        #     iterate over student list with index so human can decide
        #         start a counter at 0,
        #         print counter before objct name
        #         increment counter
        #     prompt user for input
        #     save studen object in variable to use later
        count = 0
        for student in student_list:
            print(count, '-', student.get_name())
            count += 1
        student_select_index = input('What student would you like to add to a workshop? (choose a number)')
        selected_student = student_list[int(student_select_index)]

        # Select workshop
            # iterate over workshoo list with index so human can decide
            # prompt user for input
            # save workshop object in variable to use later
        count = 0
        for workshop in running_workshops:
            print(count, '-', workshop.get_subject())
            count += 1
        workshop_select_index = input('Choose a workshop to add to: (choose a number)')
        selected_workshop = running_workshops[int(workshop_select_index)]

        selected_workshop.adding_student_to_workshop(selected_student)
        print('Well done Student has been added!')
    # elif option == '3':
    #     print('You have selected option 3 - Add student to Spooky Workshop')
    #     workshop = input('Select a workshop to add a student to? ')
    #     id = input('Please enter the ID of the student you want to add... ')
    #
    #     for student in student_list:
    #         if id == student.get_uni_id():
    #             for subject in running_workshops:
    #                 if workshop == subject.scary_subject:
    #                     subject.adding_student_to_workshop(student)
    #                     print(f'The following student {subject.list_student_id()} has been added')


        # run method adding_student_to_workshopwith selected studen


    elif option == '4':
        print('You have selected option 4 - See student grades ')
        student_id = input('Please give a student ID...')
        for student in student_list:
            if student_id == student.get_uni_id():
                print(student.get_grade())

    elif option == '5':
        print(' You have selected option 5 - See all students ')
        see_students = input('Please enter a student ID...')
        for student in student_list:
            if student_id == student.get_uni_id():
                print(f'Name: {student.get_name()}')
                print(f'Uni ID {student.get_uni_id()}')
                print(f'Grade: {student.get_grade()}')

    elif option == '6':
        print(' You have selected option 6 - Search for a student')
