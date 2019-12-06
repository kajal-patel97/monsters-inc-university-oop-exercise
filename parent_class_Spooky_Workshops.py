# should have:
# - scary subject
# - Staff
# -list of student monsters
# location

#import lecture theatre class and student monsters

from child_class_Lecture_Theatres import *
from child_class_Student_Monster import  *

class Spooky_Workshops():

    def __init__(self, scary_subject, staff, location, hall_number):
        self.scary_subjects = []
        self.staff = staff
        self.location = location
        self.hall_number = hall_number
        self.list_of_students = []

    # methods
    def adding_student_to_workshop(self, student):
        workshop = self
        workshop.list_of_students.append(student)

    def list_all_subjects(self):
        return f'These are all the Scary Subjects we offer: {self.scary_subjects}'




