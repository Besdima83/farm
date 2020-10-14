from typeBird import TypeBird


class Chicken(TypeBird):
    def __init__(self, name="Курица", egg=6):
        super().__init__(home_bird=True)
        self.name = name
        self.egg = egg

    def get_name(self):
        return self.name

    def get_eggs(self):
        return self.egg

    def im_home_bird(self):
        return self.home_bird

class Goose(TypeBird):
    def __init__(self, name="Гусь", egg=9):
        super().__init__(home_bird=True)
        self.name = name
        self.egg = egg

    def get_name(self):
        return self.name

    def get_eggs(self):
        return self.egg

    def im_home_bird(self):
        return self.home_bird


class Sparrow(TypeBird):
    def __init__(self, name="Воробей"):
        super().__init__(home_bird=False)
        self.name = name

    def get_name(self):
        return self.name

    def im_home_bird(self):
        return self.home_bird

class Dove(TypeBird):
    def __init__(self, name="Голубь"):
        super().__init__(home_bird=False)
        self.name = name

    def get_name(self):
        return  self.name

    def im_home_bird(self):
        return self.home_bird

