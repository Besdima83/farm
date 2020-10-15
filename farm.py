class Farm:
    def __init__(self):
        pass

    def pick_up_eggs(self, bird):
        if bird.im_home_bird():
            print(f"У птицы {bird.get_name()} {bird.get_eggs()} яиц")
        else:
            print(f"У птицы {bird.get_name()} нет яиц")

