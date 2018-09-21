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

            UnbreakableBrick(0, 20),

            UnbreakableBrick((CONSTANTS.BRICK_WIDTH + 15), 20),

            UnbreakableBrick(CONSTANTS.SCREEN_SIZE[0] - CONSTANTS.BRICK_WIDTH, 20),

            UnbreakableBrick(CONSTANTS.SCREEN_SIZE[0] - CONSTANTS.BRICK_WIDTH - (CONSTANTS.BRICK_WIDTH + 15), 20),
        ]

    def Level_3(self):
        self.bricks = []
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

    def Level_5(self):
        self.bricks = []
        y_ofs = 35
        count = 0
        rand_brick = 0
        for i in range(15):
            x_ofs = 42
            for j in range(8):
                count += 1
                if (26 <= count <= 27) or (30 <= count <= 31) or (34 <= count <= 35) or (38 <= count <= 39) \
                        or (count == 65) or (72 <= count <= 73) or (count == 80) or (count == 99) or (count == 102) \
                        or (count == 107) or (count == 110) or (count == 116) or (count == 117):
                    next_brick = UnbreakableBrick(x_ofs, y_ofs)
                elif (52 <= count <= 53) or (60 <= count <= 61) or (count == 82) or (count == 87) or (count == 90) or (count == 95):
                    next_brick = ThanosBrick(x_ofs, y_ofs)
                elif (count == 81) or (88 <= count <= 89) or (96 <= count <= 98) or (103 <= count <= 107)  \
                        or (111 <= count <= 115) or (count >= 118):
                    pass
                elif count == rand_brick:
                    next_brick = TrollBrick(x_ofs, y_ofs)
                elif count == 2 or count == 7 or count == 11 or count == 14 or 20 <= count <= 21:
                    next_brick = Brick(x_ofs, y_ofs)
                else:
                    next_brick = StrongBrick(x_ofs, y_ofs)

                (self.bricks).append(next_brick)
                x_ofs += CONSTANTS.BRICK_WIDTH + 10
            y_ofs += CONSTANTS.BRICK_HEIGHT + 5