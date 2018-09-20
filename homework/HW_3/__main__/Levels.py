import sys, pygame
from .Constants import Constants as Const
from .Brick import *
import random

CONSTANTS = Const()

class Levels:

    def __init__(self):
        self.bricks = []
        self.current_level = 0

    def getBricks(self):
        return self.bricks

    def Load_Next_Level(self):
        self.Level_4()
        return True

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
                self.bricks.append(next_brick)
                x_ofs += CONSTANTS.BRICK_WIDTH + 10
            y_ofs += CONSTANTS.BRICK_HEIGHT + 5

    def Level_2(self):
        self.bricks = [

            StrongBrick(65, 125),

            StrongBrick(65 + 2 * (CONSTANTS.BRICK_WIDTH + 15), 125),

            StrongBrick(65 + CONSTANTS.BRICK_WIDTH + 15, 125 + (CONSTANTS.BRICK_HEIGHT + 15)),

            Brick(65 + CONSTANTS.BRICK_WIDTH + 15, 125),

            StrongBrick(CONSTANTS.SCREEN_SIZE[0] - 65 - (CONSTANTS.BRICK_WIDTH + 15), 125),

            StrongBrick(CONSTANTS.SCREEN_SIZE[0] - 65 - 3 * (CONSTANTS.BRICK_WIDTH + 15), 125),

            StrongBrick(CONSTANTS.SCREEN_SIZE[0] - 65 - 2 * (CONSTANTS.BRICK_WIDTH + 15), 125 + (CONSTANTS.BRICK_HEIGHT + 15)),

            Brick(CONSTANTS.SCREEN_SIZE[0] - 65 - 2 * (CONSTANTS.BRICK_WIDTH + 15), 125),

            StrongBrick(CONSTANTS.SCREEN_SIZE[0]//2  - 3 * (CONSTANTS.BRICK_WIDTH + 15) // 2, 255),

            StrongBrick(CONSTANTS.SCREEN_SIZE[0]//2  + (CONSTANTS.BRICK_WIDTH + 15) // 2, 255),

            StrongBrick(CONSTANTS.SCREEN_SIZE[0]//2  - (CONSTANTS.BRICK_WIDTH + 15) // 2, 255 + (CONSTANTS.BRICK_HEIGHT + 15)),

            Brick(CONSTANTS.SCREEN_SIZE[0]//2  - (CONSTANTS.BRICK_WIDTH + 15) // 2, 255),
        ]

    def Level_3(self):
        for j in range(12):
            a = random.randint(20, 500)
            b = random.randint(20, 400)
            brick = Brick(a, b)
            self.bricks.append(brick)

    def Level_4(self):

        self.bricks = []

        for x in range(0, 9):
            for y in range(0, 4):
                self.bricks.append(Brick(x*(CONSTANTS.BRICK_WIDTH + 10) + 10, (CONSTANTS.BRICK_HEIGHT + 10)*y + 75))

        self.bricks.extend(CamoUnbreakableBrick(x * (CONSTANTS.BRICK_WIDTH + 10) + 220, 250) for x in range(3))

        for x in range(0, 3):
            self.bricks.append(Brick(x*(CONSTANTS.BRICK_WIDTH + 10) + 10, (CONSTANTS.BRICK_HEIGHT + 10)*7 + 75))

        for x in range(6, 9):
            self.bricks.append(Brick(x*(CONSTANTS.BRICK_WIDTH + 10) + 10, (CONSTANTS.BRICK_HEIGHT + 10)*7 + 75))