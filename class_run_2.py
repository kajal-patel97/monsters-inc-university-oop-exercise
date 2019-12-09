#import appropriate class
from parent_class_Spooky_Workshops import *

# As an admin i want to be able to list all the spooky workshops so that i can inform students of the work shops happening

# First you need to create some spooky classes to list

class1 = Spooky_Workshops('Class Hiding', 'Liz', 'USA', 1)
class2 = Spooky_Workshops('Class Attack', 'Bea', 'USA', 2)
class3 = Spooky_Workshops('Class Theory', 'Ant', 'USA', 3)
class4 = Spooky_Workshops('Class Practical', 'Mike', 'USA', 4)

# Now list all the classes

print(f'These are all the Classes we offer: {class1.scary_subject}, {class2.scary_subject}, {class3.scary_subject}, {class4.scary_subject}')