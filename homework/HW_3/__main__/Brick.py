import pygame
from .Constants import Constants as Consts

CONSTANTS = Consts()

class Brick:
    #Type: [number of hits to break, color]; hits to break < 0 for any unbreakable ones.
    brick_types = {"Basic":[1, CONSTANTS.YELLOW], "Unbreakable":[-1, CONSTANTS.GREY], "Destroyed":[0, CONSTANTS.BLACK]}

    def __init__(self, x_ofs, y_ofs, brick_type = "Basic"):
        self.rect = pygame.Rect(x_ofs, y_ofs, CONSTANTS.BRICK_WIDTH, CONSTANTS.BRICK_HEIGHT)
        self.brick_type = brick_type
        self.getTypeInfo()

    def getTypeInfo(self):
        self.hits_to_break = ((Brick.brick_types)[self.brick_type])[0]
        self.color = ((Brick.brick_types)[self.brick_type])[1]

    def onHit(self):
        to_do_name = self.brick_type + "_onHit"
        try:
            to_do = getattr(self, to_do_name)
            to_do()
        except AttributeError:
            self.brick_type = "Destroyed"
            self.getTypeInfo()

    def Basic_onHit(self):
        self.brick_type = "Destroyed"
        self.getTypeInfo()

    def Unbreakable_onHit(self):
        pass