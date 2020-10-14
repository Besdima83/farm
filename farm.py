from bird import Bird


class Farm(Bird):
    def __init__(self):
        super().__init__()

    def pick_up_eggs(self):
        name = self.get_name()
        egg = self.get_eggs()
        if self.im_home_bird():
            print(f"У птицы {name} {egg} яиц")
        else:
            print(f"У птицы {name} нет яиц")
