import pygame

# Initialize Pygame and set up window
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
ground_y = 400

# Player variables
player_y = ground_y
vertical_velocity = 0
gravity = 0.5
jump_speed = -12
is_jumping = False
player_rect = pygame.Rect(100, player_y, 50, 50)

# Circle particle

groundY = screen_width - 100
groundX = 100
circleX = groundX
circleY = groundY
verticalVelocity = -80
HorizontalBVelocity = 60
gravity = 0.5

clock = pygame.time.Clock()
# Game loop
run = True
while run:
    # dt = clock.tick(60) # Control frame rate
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                vertical_velocity = jump_speed
                is_jumping = True

    # # Apply physics
    # vertical_velocity += gravity
    # player_y += vertical_velocity
    
    # # Ground collision
    # if player_y >= ground_y:
    #     player_y = ground_y
    #     vertical_velocity = 0
    #     is_jumping = False
        
    # # Update player position (use round for pixel precision)
    # player_rect.y = round(player_y)

    # print(player_rect.center)

    # Drawing
    # screen.fill((163, 232, 254)) # Sky color
    # pygame.draw.rect(screen, (88, 242, 152), (0, ground_y, screen_width, screen_height - ground_y)) # Ground
    # pygame.draw.rect(screen, (255, 0, 0), player_rect) # Player
    pygame.draw.circle(screen, (255, 0, 0), (25, 25), 25)
    pygame.display.update()

pygame.quit()
