from bird import Bird


class TypeBird(Bird):
    def __init__(self, home_bird=True):
        super().__init__()
        self.home_bird = home_bird
