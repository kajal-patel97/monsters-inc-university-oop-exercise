# Monster Should have a name and skills in their attributes

class Monster():

    #Monster Attributes
    def __init__(self, name, skills = ['']):
        self.name = name
        self.skills = skills

    #Monster Methods
    def added_skills (self, skill):
        the_monster_in_question = self
        the_monster_in_question.skills.append(skill)