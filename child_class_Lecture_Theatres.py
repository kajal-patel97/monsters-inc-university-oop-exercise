# Should have a hall number
#import building
from parent_class_Building import *

class Lecture_Theatre(Building):

    def __init__(self, hall_number, location):
        self.hall_number = hall_number
        self.location = location

    #Methods

    def get_hall_number(self):
        return self.hall_number