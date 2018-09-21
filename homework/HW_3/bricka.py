"""
Original code source:
     bricka (a breakout clone)


     Developed by Leonel Machava <leonelmachava@gmail.com>
     http://codeNtronix.com
"""
import sys
import tkinter
import pygame
from homework.HW_3.__main__.Constants import Constants as Consts
from homework.HW_3.__main__.Levels import Levels

CONSTANTS = Consts()


class Bricka:

    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode(CONSTANTS.SCREEN_SIZE)
        pygame.display.set_caption("bricka (a breakout clone by codeNtronix.com)")
        
        self.clock = pygame.time.Clock()

        if pygame.font:
            self.font = pygame.font.Font(None,30)
        else:
            self.font = None

        self.init_game()

        
    def init_game(self):
        self.lives = 3
        self.score = 0
        self.state = CONSTANTS.STATE_BALL_IN_PADDLE

        self.ball_vel = CONSTANTS.BALL_VELOCITY
        self.levels = Levels()

        self.init_next_level()

    def init_next_level(self):
        self.lives = 3
        keep_going = self.levels.Load_Next_Level()
        if keep_going:
            self.bricks = self.levels.getBricks()
            self.paddle = pygame.Rect(300, CONSTANTS.PADDLE_Y, CONSTANTS.PADDLE_WIDTH, CONSTANTS.PADDLE_HEIGHT)
            self.ball = pygame.Rect(300, CONSTANTS.PADDLE_Y - CONSTANTS.BALL_DIAMETER, CONSTANTS.BALL_DIAMETER,
                                    CONSTANTS.BALL_DIAMETER)
            self.state = CONSTANTS.STATE_BALL_IN_PADDLE
        else:
            self.state = CONSTANTS.STATE_WON

    def draw_bricks(self):
        for brick in self.bricks:
            pygame.draw.rect(self.screen, brick.color, brick.rect)
        
    def check_input(self):

        self.checkForQuit()
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.paddle.left -= CONSTANTS.PADDLE_MOVE_INCREMENT
            if self.paddle.left < 0:
                self.paddle.left = 0

        if keys[pygame.K_RIGHT]:
            self.paddle.left += CONSTANTS.PADDLE_MOVE_INCREMENT
            if self.paddle.left > CONSTANTS.MAX_PADDLE_X:
                self.paddle.left = CONSTANTS.MAX_PADDLE_X

        if keys[pygame.K_SPACE] and self.state == CONSTANTS.STATE_BALL_IN_PADDLE:
            self.ball_vel = CONSTANTS.BALL_VELOCITY
            self.state = CONSTANTS.STATE_PLAYING

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if(self.state == CONSTANTS.STATE_GAME_OVER or self.state == CONSTANTS.STATE_WON):
                        self.init_game()
                    elif(self.state == CONSTANTS.STATE_GET_NEXT_LEVEL):
                        self.state = CONSTANTS.STATE_START_NEXT_LEVEL

                if event.key == pygame.K_UP and self.state == CONSTANTS.STATE_BALL_IN_PADDLE and self.levels.current_level == 1 and self.lives == 3 and (CONSTANTS.STATE_CL == 6 or CONSTANTS.STATE_CL == 7):
                    CONSTANTS.STATE_CL += 1
                elif event.key != pygame.K_UP:
                    pass
                else:
                    CONSTANTS.STATE_CL = 6

                if event.key == pygame.K_a and self.state == CONSTANTS.STATE_BALL_IN_PADDLE and self.levels.current_level == 1 and self.lives == 3 and CONSTANTS.STATE_CL == 15:
                    self.cl = tkinter.Tk()
                    self.cl.geometry("400x150")

                    self.frame = tkinter.Frame(self.cl)
                    self.frame.pack()

                    self.message = tkinter.Label(self.frame, text="Enter the number below\n")
                    self.message.pack()

                    self.ls = tkinter.Entry(self.frame)
                    self.ls.pack()

                    self.cfl = tkinter.Button(self.frame, text="Confirm", command=self.cL)
                    self.cfl.pack()

                    self.cl.mainloop()
                elif event.key != pygame.K_a:
                    pass
                else:
                    CONSTANTS.STATE_CL = 6

                if event.key == pygame.K_LEFT and self.state == CONSTANTS.STATE_BALL_IN_PADDLE and self.levels.current_level == 1 and self.lives == 3 and (CONSTANTS.STATE_CL == 10 or CONSTANTS.STATE_CL == 12):
                    CONSTANTS.STATE_CL += 1
                elif event.key != pygame.K_LEFT:
                    pass
                else:
                    CONSTANTS.STATE_CL = 6

                if event.key == pygame.K_s:
                    if CONSTANTS.PADDLE_MOVE_INCREMENT == 10:
                        CONSTANTS.PADDLE_MOVE_INCREMENT = 20
                    else:
                        CONSTANTS.PADDLE_MOVE_INCREMENT = 10

                if event.key == pygame.K_DOWN and self.state == CONSTANTS.STATE_BALL_IN_PADDLE and self.levels.current_level == 1 and self.lives == 3 and (CONSTANTS.STATE_CL == 8 or CONSTANTS.STATE_CL == 9):
                    CONSTANTS.STATE_CL += 1
                elif event.key != pygame.K_DOWN:
                    pass
                else:
                    CONSTANTS.STATE_CL = 6

                if event.key == pygame.K_RIGHT and self.state == CONSTANTS.STATE_BALL_IN_PADDLE and self.levels.current_level == 1 and self.lives == 3 and (CONSTANTS.STATE_CL == 11 or CONSTANTS.STATE_CL == 13):
                    CONSTANTS.STATE_CL += 1
                elif event.key != pygame.K_RIGHT:
                    pass
                else:
                    CONSTANTS.STATE_CL = 6


                if event.key == pygame.K_z:
                    for brick in self.bricks:
                        brick.onHit()
                        if brick.hits_to_break == 0:
                            self.bricks.remove(brick)

                if event.key == pygame.K_b and self.state == CONSTANTS.STATE_BALL_IN_PADDLE and self.levels.current_level == 1 and self.lives == 3 and CONSTANTS.STATE_CL == 14:
                    CONSTANTS.STATE_CL += 1
                elif event.key != pygame.K_b:
                    pass
                else:
                    CONSTANTS.STATE_CL = 6

                if not (event.key == pygame.K_b or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a):
                    CONSTANTS.STATE_CL = 6



    def move_ball(self):
        self.ball.left += self.ball_vel[0]
        self.ball.top  += self.ball_vel[1]

        if self.ball.left <= 0:
            self.ball.left = 0
            self.ball_vel[0] = -self.ball_vel[0]
        elif self.ball.left >= CONSTANTS.MAX_BALL_X:
            self.ball.left = CONSTANTS.MAX_BALL_X
            self.ball_vel[0] = -self.ball_vel[0]
        
        if self.ball.top < 0:
            self.ball.top = 0
            self.ball_vel[1] = -self.ball_vel[1]
        elif self.ball.top >= CONSTANTS.MAX_BALL_Y:
            self.ball.top = CONSTANTS.MAX_BALL_Y
            self.ball_vel[1] = -self.ball_vel[1]

    def handle_collisions(self):
        for brick in self.bricks:
            if self.ball.colliderect(brick.rect):
                if brick.hits_to_break > 0:
                    self.score += 3
                if (self.ball.right - self.ball_vel[0] <= brick.rect.left or self.ball.left - self.ball_vel[0] >= brick.rect.right) and (not (self.ball.bottom - 2 < brick.rect.top or self.ball.top + 2 > brick.rect.bottom)):
                    self.ball_vel[0] = -self.ball_vel[0]
                    if self.ball.right + self.ball_vel[0] <= brick.rect.left:
                        self.ball.right = brick.rect.left + self.ball_vel[0]
                    if self.ball.left + self.ball_vel[0] >= brick.rect.right:
                        self.ball.left = brick.rect.right + self.ball_vel[0]
                else:
                    self.ball_vel[1] = -self.ball_vel[1]
                    if self.ball.bottom + self.ball_vel[1] < brick.rect.top:
                        self.ball.bottom = brick.rect.top + self.ball_vel[1]
                    if self.ball.top + self.ball_vel[1] >= brick.rect.bottom:
                        self.ball.top = brick.rect.bottom + self.ball_vel[1]

                brick.onHit()
                if brick.hits_to_break == 0:
                    self.bricks.remove(brick)
                break

        temp_state = self.state
        self.state = CONSTANTS.STATE_GET_NEXT_LEVEL
        for brick in self.bricks:
            if brick.hits_to_break > 0:
                self.state = temp_state
            else:
                continue

            
        if self.ball.colliderect(self.paddle):
            self.ball.top = CONSTANTS.PADDLE_Y - CONSTANTS.BALL_DIAMETER
            self.ball_vel[1] = -self.ball_vel[1]

            if (self.ball.left + CONSTANTS.BALL_RADIUS < self.paddle.left + (CONSTANTS.PADDLE_WIDTH // 2)):
                if (self.ball.left + CONSTANTS.BALL_RADIUS < self.paddle.left + (CONSTANTS.PADDLE_WIDTH // 4)):
                    self.ball_vel[0] = -7
                else:
                    self.ball_vel[0] = -5
            else:
                if (self.ball.left + CONSTANTS.BALL_RADIUS > self.paddle.left + (3 * CONSTANTS.PADDLE_WIDTH // 4)):
                    self.ball_vel[0] = 7
                else:
                    self.ball_vel[0] = 5

        elif self.ball.top > self.paddle.top:
            self.lives -= 1
            if self.lives > 0:
                self.state = CONSTANTS.STATE_BALL_IN_PADDLE
            else:
                self.state = CONSTANTS.STATE_GAME_OVER

    def show_stats(self):
        if self.font:
            font_surface = self.font.render("SCORE: " + str(self.score) + " LIVES: " + str(self.lives), False, CONSTANTS.WHITE)
            self.screen.blit(font_surface, (205,5))

    def cL(self):
        temp = self.ls.get()
        try:
            self.levels.current_level = int(temp) - 1
        except ValueError:
            self.message.config(text="Not an integer. Enter an integer.")
            return -1
        if (self.levels.current_level < 0):
            self.levels.current_level = 1
            self.message.config(text="Number must be greater than 0.")
            return -1

        self.init_next_level()
        self.cl.withdraw()
        self.cl.quit()

    def show_message(self,message):
        if self.font:
            size = self.font.size(message)
            font_surface = self.font.render(message,False, CONSTANTS.WHITE)
            x = (CONSTANTS.SCREEN_SIZE[0] - size[0]) / 2
            y = (CONSTANTS.SCREEN_SIZE[1] - size[1]) / 2
            self.screen.blit(font_surface, (x,y))

    def terminate(self):
        print("terminating")
        pygame.quit()
        sys.exit()

    def checkForQuit(self):
        for event in pygame.event.get(pygame.QUIT):  # get all the QUIT events
            self.terminate()  # terminate if any QUIT events are present
        for event in pygame.event.get(pygame.KEYUP):  # get all the KEYUP events
            if event.key == pygame.K_ESCAPE:
                self.terminate()  # terminate if the KEYUP event was for the Esc key
            pygame.event.post(event)  # put the other KEYUP event objects back
        
            
    def run(self):
        while 1:

            self.clock.tick(50)
            self.screen.fill(CONSTANTS.BLACK)
            self.check_input()

            self.checkForQuit()

            if self.state == CONSTANTS.STATE_PLAYING:
                self.move_ball()
                self.handle_collisions()
            elif self.state == CONSTANTS.STATE_BALL_IN_PADDLE:
                self.ball.left = self.paddle.left + self.paddle.width / 2
                self.ball.top  = self.paddle.top - self.ball.height
                self.show_message("PRESS SPACE TO LAUNCH THE BALL")
            elif self.state == CONSTANTS.STATE_GAME_OVER:
                self.show_message("GAME OVER. PRESS ENTER TO PLAY AGAIN")
            elif self.state == CONSTANTS.STATE_WON:
                self.show_message("YOU WON! PRESS ENTER TO PLAY AGAIN")
            elif self.state == CONSTANTS.STATE_GET_NEXT_LEVEL:
                self.show_message("LEVEL COMPLETE!  PRESS ENTER TO CONTINUE!")
            elif self.state == CONSTANTS.STATE_START_NEXT_LEVEL:
                self.init_next_level()

            self.draw_bricks()

            # Draw paddle
            pygame.draw.rect(self.screen, CONSTANTS.BLUE, self.paddle)


            # Draw ball
            pygame.draw.circle(self.screen, CONSTANTS.WHITE, (self.ball.left + CONSTANTS.BALL_RADIUS, self.ball.top + CONSTANTS.BALL_RADIUS), CONSTANTS.BALL_RADIUS)

            self.show_stats()

            pygame.display.flip()

if __name__ == "__main__":
    Bricka().run()
