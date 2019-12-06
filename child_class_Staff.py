from parent_class_Monster import*


class Staff(Monster):

    def __init__(self, monster_name):
        super().__init__(monster_name)
        self.monster_name = monster_name
