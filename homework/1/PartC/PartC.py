
import pygame, sys, time, random
from pygame.locals import *

class ImageRect(pygame.Rect):
    def __init__(self, image, *args):
        pygame.Rect.__init__(self, *args)
        self.image = image


# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# set up the window
WINDOW_WIDTH = 2000
WINDOW_HEIGHT = 2000
INIT_SPRITE_SIZE = 80
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption("You know what time it is!!!")

# set up the colors
BLACK = (0, 0, 0)

# set up the block data structure
player = pygame.Rect(300, 100, 180, 180)
playerImage = pygame.image.load('banana.png')
playerStretchedImage = pygame.transform.scale(playerImage, (INIT_SPRITE_SIZE, INIT_SPRITE_SIZE))

jellyImage = pygame.image.load('peanut-butter.png')
jellyImage = pygame.transform.scale(jellyImage, (INIT_SPRITE_SIZE, INIT_SPRITE_SIZE))

peanutButterImage = pygame.image.load('jelly.png')
peanutButterImage = pygame.transform.scale(peanutButterImage, (INIT_SPRITE_SIZE, INIT_SPRITE_SIZE))

foods = []
for i in range(20):
    rect = ImageRect(
        random.choice((peanutButterImage, jellyImage)),
        random.randint(0, WINDOW_WIDTH - INIT_SPRITE_SIZE),
        random.randint(0, WINDOW_HEIGHT - INIT_SPRITE_SIZE),
        INIT_SPRITE_SIZE,
        INIT_SPRITE_SIZE
    )
    foods.append(rect)

foodCounter = 0
NEWFOOD = 40

# set up keyboard variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 20
GROWTH_AMOUNT = 20

# set up music
pickUpSound = pygame.mixer.Sound('pickup.wav')
pygame.mixer.music.load('peanut-butter-jelly-time.mp3')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

# run the game loop
while True:
    # check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == K_LEFT or event.key == ord('a'):
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == ord('d'):
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == ord('w'):
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == ord('s'):
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False
            if event.key == ord('x'):
                player.top = random.randint(0, WINDOW_HEIGHT - player.height)
                player.left = random.randint(0, WINDOW_WIDTH - player.width)
            if event.key == ord('m'):
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0] - 10, event.pos[1] - 10, 20, 20))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # add new food
        foodCounter = 0
        rect = ImageRect(
            random.choice((peanutButterImage, jellyImage)),
            random.randint(0, WINDOW_WIDTH - INIT_SPRITE_SIZE),
            random.randint(0, WINDOW_HEIGHT - INIT_SPRITE_SIZE),
            INIT_SPRITE_SIZE,
            INIT_SPRITE_SIZE
        )
        foods.append(rect)

    # draw the black background onto the surface
    windowSurface.fill(BLACK)

    # move the player
    if moveDown and player.bottom < WINDOW_HEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOW_WIDTH:
        player.right += MOVESPEED


    # draw the block onto the surface
    windowSurface.blit(playerStretchedImage, player)

    # check if the block has intersected with any food squares.
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left, player.top, player.width + 2, player.height + 2)
            playerStretchedImage = pygame.transform.scale(playerImage, (player.width, player.height))
            if musicPlaying:
                pickUpSound.play()

    # draw the food
    for food in foods:
        windowSurface.blit(food.image, food)

    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(40)