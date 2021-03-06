# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Multiple Wall Detection"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

    
# Make a block
block =  [200, 150, 50, 50]
vel = [0, 0]
speed = 5

# make a wall
wall1 =  [300, 275, 200, 50]
wall2 =  [400, 450, 200, 50]
wall3 =  [100, 100, 50, 200]

walls = [wall1, wall2, wall3]

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    state = pygame.key.get_pressed()

    up = state[pygame.K_UP]
    down = state[pygame.K_DOWN]
    left = state[pygame.K_LEFT]
    right = state[pygame.K_RIGHT]

    if left:
        vel[0]  = -speed
    elif right:
        vel[0]  = speed
    else:
        vel[0]  = 0

    if up:
        vel[1] = -speed
    elif down:
        vel[1]  = speed
    else:
        vel[1]  = 0
        
        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the block in horizontal direction '''
    block[0] += vel[0]

    ''' resolve collisions '''
    for w in walls:
        if intersects.rect_rect(block, w):        
            if vel[0]> 0:
                block[0] = w[0] - block[2]
            elif vel[0] < 0:
                block[0] = w[0] + w[2]

    ''' move the block in vertical direction '''
    block[1] += vel[1]
    
    ''' resolve collisions '''
    for w in walls:
        if intersects.rect_rect(block, w):                    
            if vel[1] > 0:
                block[1] = w[1] - block[3]
            if vel[1] < 0:
                block[1] = w[1] + w[3]

    
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, block)

    for w in walls:
        pygame.draw.rect(screen, RED, w)

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
