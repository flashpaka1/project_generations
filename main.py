import pygame
import sys

background_colour = (255, 255, 255)
screen_h, screen_w = 1000, 1000
screen = pygame.display.set_mode((screen_h, screen_w))
pygame.display.set_caption('Darwin')

object_color = (0, 0, 225)
object_w, object_h = 10, 10
object_x, object_y = (screen_w - object_w) // 2, (screen_h - object_h) // 2
object_speed = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        object_x -= object_speed
    if keys[pygame.K_RIGHT]:
        object_x += object_speed
    if keys[pygame.K_UP]:
        object_y -= object_speed
    if keys[pygame.K_DOWN]:
        object_y += object_speed

    screen.fill(background_colour)
    pygame.draw.rect(screen, object_color, (object_x, object_y, object_w, object_h))
    pygame.display.flip()

pygame.quit()
sys.exit()