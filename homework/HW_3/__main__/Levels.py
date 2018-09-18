import sys, pygame
from .Constants import Constants as Const
from .Brick import *

CONSTANTS = Const()

class Levels:

    def __init__(self):
        self.bricks = []
        self.current_level = 0

    def getBricks(self):
        return self.bricks

    def Load_Next_Level(self):
        self.current_level += 1
        level = "Level_" + str(self.current_level)
        try:
            start_level = getattr(self, level)
            start_level()
            return True
        except AttributeError:
            return False


    def Level_1(self):
        self.bricks = []
        y_ofs = 35
        for i in range(7):
            x_ofs = 35
            for j in range(8):
                if not x_ofs % 3:
                    next_brick = StrongBrick(x_ofs, y_ofs)
                else:
                    next_brick = Brick(x_ofs, y_ofs)
                (self.bricks).append(next_brick)
                x_ofs += CONSTANTS.BRICK_WIDTH + 10
            y_ofs += CONSTANTS.BRICK_HEIGHT + 5

    def Level_2(self):
        self.bricks = []

        brick = UnbreakableBrick(65, 125)
        self.bricks.append(brick)

        brick = UnbreakableBrick(65 + 2 * (CONSTANTS.BRICK_WIDTH + 10), 125)
        self.bricks.append(brick)

        brick = UnbreakableBrick(65 + CONSTANTS.BRICK_WIDTH + 10, 125 + (CONSTANTS.BRICK_HEIGHT + 5))
        self.bricks.append(brick)

        brick = Brick(65 + CONSTANTS.BRICK_WIDTH + 10, 125)
        self.bricks.append(brick)

        brick = StrongBrick(CONSTANTS.SCREEN_SIZE[0] - 65 - (CONSTANTS.BRICK_WIDTH + 10), 125)
        self.bricks.append(brick)

        brick = UnbreakableBrick(CONSTANTS.SCREEN_SIZE[0] - 65 - 3 * (CONSTANTS.BRICK_WIDTH + 10), 125)
        self.bricks.append(brick)

        brick = UnbreakableBrick(CONSTANTS.SCREEN_SIZE[0] - 65 - 2 * (CONSTANTS.BRICK_WIDTH + 10), 125 + (CONSTANTS.BRICK_HEIGHT + 5))
        self.bricks.append(brick)

        brick = Brick(CONSTANTS.SCREEN_SIZE[0] - 65 - 2 * (CONSTANTS.BRICK_WIDTH + 10), 125)
        self.bricks.append(brick)

        brick = StrongBrick(CONSTANTS.SCREEN_SIZE[0]//2  - 3 * (CONSTANTS.BRICK_WIDTH + 10) // 2, 255)
        self.bricks.append(brick)

        brick = UnbreakableBrick(CONSTANTS.SCREEN_SIZE[0]//2  + (CONSTANTS.BRICK_WIDTH + 10) // 2, 255)
        self.bricks.append(brick)

        brick = UnbreakableBrick(CONSTANTS.SCREEN_SIZE[0]//2  - (CONSTANTS.BRICK_WIDTH + 10) // 2, 255 + (CONSTANTS.BRICK_HEIGHT + 5))
        self.bricks.append(brick)

        brick = Brick(CONSTANTS.SCREEN_SIZE[0]//2  - (CONSTANTS.BRICK_WIDTH + 10) // 2, 255)
        self.bricks.append(brick)
