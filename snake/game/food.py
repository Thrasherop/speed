import random
from game import constants
from game.actor import Actor
from game.point import Point



class Food(Actor):

    def __init__(self):
        super().__init__()
        super().set_position(Point(random.randint(0, constants.MAX_X), random.randint(0, constants.MAX_Y)))
        super().set_text("@")
        self._points = 1

    # def get_position(self):
    #     return super().get_position()

    def get_points(self):
        return self._points

    def reset(self):
        super().set_position(Point(random.randint(0, constants.MAX_X), random.randint(0, constants.MAX_Y)))

