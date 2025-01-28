import pygame
import random
import math 

pygame.init()

WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DPong_Table")

# Paddle dimensions
paddle_width, paddle_height = 20, 120
left_paddle_x = 100 - paddle_width / 2
right_paddle_x = WIDTH - (100 - paddle_width / 2)
left_paddle_y = HEIGHT / 2 - paddle_height / 2
right_paddle_y = HEIGHT / 2 - paddle_height / 2
right_paddle_vel = left_paddle_vel = 0

# Ball properties
radius = 15
ball_x, ball_y = WIDTH / 2, HEIGHT / 2
ball_vel_x, ball_vel_y = 0.7, 0.7

# Colors
RED = (255, 0, 0)
YELLOW = (0, 0, 255)
BLACK = (0, 0, 0)

# Reset ball and paddle positions
def reset_ball():
    global ball_x, ball_y, ball_vel_x, ball_vel_y, left_paddle_y, right_paddle_y
    ball_x, ball_y = WIDTH / 2, HEIGHT / 2
    angle = random.uniform(-math.pi / 4, math.pi / 4)  # Random angle between -45 and 45 degrees
    speed = 0.5  # Constant speed
    ball_vel_x = speed * math.cos(angle) * (1 if random.choice([True, False]) else -1)
    ball_vel_y = speed * math.sin(angle)
    
    # Reset paddle positions
    left_paddle_y = HEIGHT / 2 - paddle_height / 2
    right_paddle_y = HEIGHT / 2 - paddle_height / 2

# Game loop
function = True
while function:
    wn.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            function = False 
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.5 
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.5
            if i.key == pygame.K_w:
                left_paddle_vel = -0.5
            if i.key == pygame.K_s:
                left_paddle_vel = 0.5
        if i.type == pygame.KEYUP:
            right_paddle_vel = 0
            left_paddle_vel = 0
    
    # Ball movement and wall collision
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1
    if ball_x >= WIDTH - radius or ball_x <= 0 + radius:
        reset_ball()  # Reset ball and paddles when the ball goes out of bounds

    # Paddle movement control
    left_paddle_y += left_paddle_vel
    right_paddle_y += right_paddle_vel

    # Keep paddles within the screen boundaries
    left_paddle_y = max(0, min(HEIGHT - paddle_height, left_paddle_y))
    right_paddle_y = max(0, min(HEIGHT - paddle_height, right_paddle_y))

    # Paddle collision
    if left_paddle_x <= ball_x - radius <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width + radius
            ball_vel_x *= -1

    if right_paddle_x <= ball_x + radius <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x - radius
            ball_vel_x *= -1

    # Ball movement
    ball_x += ball_vel_x
    ball_y += ball_vel_y

    # Drawing objects
    pygame.draw.circle(wn, YELLOW, (int(ball_x), int(ball_y)), radius)
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))

    pygame.display.update()
