import pygame
import pygame.locals
# This import simply saves you the hassle of having to type 
# pygame.K_UP, pygame.K_DOWN, etc. thrughout the code
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# Define a Player class with position and speed attributes
class Player:
    def __init__(self, x=0, y=0, speed=0.25):
        self.x = x
        self.y = y
        self.speed = speed;
    
    def __str__(self): 
        return f"Player [x:{self.x} y:{self.y}]" 

# Define a Board class which will be the digital representation
# of your board
class Board:
    height = 0,
    width = 0

    def __init__(self, height, width):
        self.height = height
        self.width = width

# pygame initialization
pygame.init()

my_board = Board(500, 500)
my_player = Player(my_board.width/2, my_board.height/2)

# get an instance of the pygame display and set the height and width
screen = pygame.display.set_mode((my_board.width, my_board.height))

# Booleans to track if a direction key is being held down 
# Since pygame's event listener only registers on keydown or keyup 
# It doesnt know if a key is being held down
up_key_press = False
down_key_press = False
left_key_press = False
right_key_press = False

# The main game loop
running = True
while running:
    # loop through the events and check if the quit button was clciked
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # Check keydown event - Set the booleans for the keys when
        # they are pressed or released. This tracks if the key is held down
        elif event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                up_key_press = True
            elif event.key == K_DOWN:
                down_key_press = True
            elif event.key == K_LEFT:
                left_key_press = True
            elif event.key == K_RIGHT:
                right_key_press = True
        elif event.type == pygame.KEYUP:
                up_key_press = False
                down_key_press = False
                left_key_press = False
                right_key_press = False

    # Update the player position here, checking for the board boundaries
    if left_key_press and my_player.x > 0:
        my_player.x -= my_player.speed
        # print(my_player)
    if right_key_press and my_player.x < my_board.width:
        my_player.x += my_player.speed
        # print(my_player)
    if up_key_press and my_player.y > 0:
        my_player.y -= my_player.speed
        # print(my_player)
    if down_key_press and my_player.y < my_board.height:
        my_player.y += my_player.speed
        # print(my_player)
    #fill the screen with white
    screen.fill((255, 255, 255))
    # draw a blue (0,0,255) circle on the center (250,250) of the screen with a radius of 75
    pygame.draw.circle (screen, (0, 0, 255), (my_player.x, my_player.y), 20)

    # to display the screen call the flip() method
    pygame.display.flip()