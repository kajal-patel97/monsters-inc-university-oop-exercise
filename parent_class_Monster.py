# Monster Should have a name and skills in their attributes

class Monster():

    #Monster Attributes
    def __init__(self, monster_name):
        self.__monster_name = monster_name
        self.__skills = []

    #Monster Methods
    def get_name(self):
        return self.__monster_name

    def added_skills (self, skill):
        the_monster_in_question = self
        the_monster_in_question.__skills.append(skill)


    def get_skills(self):
        return self.__skills

    def list_of_monsters(self):
            list_monsters = []
            for list_monsters in self.list_of_students:
                stu_id.extend([student.get_uni_id()])
            return stu_id