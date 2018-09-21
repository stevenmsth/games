import pygame
import random
from .Constants import Constants as Consts

CONSTANTS = Consts()

class Brick:

    class STATUS:
        NORMAL = 1
        DAMAGED = 2
        DESTROYED = 3
        UNBREAKABLE = 4

    STATUS_COLORS = {
        STATUS.NORMAL: CONSTANTS.YELLOW,
        STATUS.DAMAGED: CONSTANTS.RED,
        STATUS.DESTROYED: CONSTANTS.BLACK,
        STATUS.UNBREAKABLE: CONSTANTS.GREY,
    }

    hits_to_break = 1

    def __init__(self, x_ofs, y_ofs, status = STATUS.NORMAL):
        self.rect = pygame.Rect(x_ofs, y_ofs, CONSTANTS.BRICK_WIDTH, CONSTANTS.BRICK_HEIGHT)
        self.status = status
        self.color = CONSTANTS.RED

    def onHit(self):
        self.status = Brick.STATUS.DESTROYED
        self.hits_to_break = 0

class StrongBrick(Brick):
    def __init__(self, x_ofs, y_ofs, status = Brick.STATUS.NORMAL):
        Brick.__init__(self, x_ofs, y_ofs, status)
        self.hits_to_break = 2
        self.color = CONSTANTS.GREEN

    def onHit(self):
        if self.hits_to_break > 0:
            self.hits_to_break -= 1
            self.color = CONSTANTS.RED
        else:
            self.status = Brick.STATUS.DESTROYED
            self.color = Brick.STATUS_COLORS[Brick.STATUS.DESTROYED]

class UnbreakableBrick(Brick):

    hits_to_break = -1

    def __init__(self, x_ofs, y_ofs, status = Brick.STATUS.NORMAL):
        Brick.__init__(self, x_ofs, y_ofs, status)
        self.color = CONSTANTS.GREY

    def onHit(self):
        pass

class ThanosBrick(Brick):
    count = 0
    randUnlockTime = random.randint(240000, 360000)
    def __init__(self, x_ofs, y_ofs, status = Brick.STATUS.NORMAL):
        Brick.__init__(self, x_ofs, y_ofs, status)
        self.color = CONSTANTS.PURPLE
        self.hits_to_break = -1

    def onHit(self):

        if pygame.time.get_ticks() >= self.randUnlockTime:
            if self.count == 0:
                self.count += 1
                self.hits_to_break = 3
                pass

            if self.hits_to_break > 0:
                if self.hits_to_break == 3:
                    self.hits_to_break += -1
                    pass
                elif self.hits_to_break == 2:
                    self.hits_to_break += -1
                    self.color = CONSTANTS.GREEN
                else:
                    self.hits_to_break += -1
                    self.color = CONSTANTS.RED
            else:
                self.status = Brick.STATUS.DESTROYED
                self.color = Brick.STATUS_COLORS[Brick.STATUS.DESTROYED]


class TrollBrick(Brick):

    hits_to_break = 1
    restartLevel = False

    def __init__(self, x_ofs, y_ofs, status = Brick.STATUS.NORMAL):
        self.rect = pygame.Rect(x_ofs, y_ofs, CONSTANTS.BRICK_WIDTH, CONSTANTS.BRICK_HEIGHT)
        self.status = status
        self.color = CONSTANTS.WHITE

    def onHit(self):
        restartLevel = True
