class Constants:

    def __init__(self):
        self.SCREEN_SIZE   = 640,480

        # Object dimensions
        self.BRICK_WIDTH   = 60
        self.BRICK_HEIGHT  = 15
        self.PADDLE_WIDTH  = 100
        self.PADDLE_HEIGHT = 12
        self.BALL_DIAMETER = 16
        self.BALL_RADIUS   = self.BALL_DIAMETER // 2

        # Object velocities
        self.PADDLE_MOVE_INCREMENT = 10
        self.BALL_VELOCITY = [5, -5]

        self.MAX_PADDLE_X = self.SCREEN_SIZE[0] - self.PADDLE_WIDTH
        self.MAX_BALL_X   = self.SCREEN_SIZE[0] - self.BALL_DIAMETER
        self.MAX_BALL_Y   = self.SCREEN_SIZE[1] - self.BALL_DIAMETER
        self.PADDLE_SPEED = 5

        # Paddle Y coordinate
        self.PADDLE_Y = self.SCREEN_SIZE[1] - self.PADDLE_HEIGHT - 10

        # Color constants
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.GREY = (128, 128, 128)
        self.BLUE = (0,0,255)
        self.YELLOW = (200,200,0)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.BRICK_COLOR = (200,200,0)
        self.PURPLE = (148, 0, 211)


        # State constants
        self.STATE_BALL_IN_PADDLE = 0
        self.STATE_PLAYING = 1
        self.STATE_WON = 2
        self.STATE_GAME_OVER = 3
        self.STATE_GET_NEXT_LEVEL = 4
        self.STATE_START_NEXT_LEVEL = 5