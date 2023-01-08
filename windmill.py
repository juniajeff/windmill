import pygame
import math

#initializing pygame, standard settings, colors, width and height of the playscreen, mode and caption, clock
pygame.init()

BLACK = (0,0,0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 1200, 1000

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Windmill is moving")

clock = pygame.time.Clock()
speed = 60

#loading images
img = pygame.image.load('windmill.png')
bk = pygame.image.load('provence.png')
part = pygame.image.load('windmill_part.png')
part_s = pygame.transform.scale(part, (500, 500))
bk_bigger = pygame.transform.scale(bk, (1200,1000)) #transforming background image for fitting in the screen size

#function of rotation the image
def rotate2(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect.topleft)

#main function
def main():
    #game loop
    angle = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        #filling the screen with white color
        screen.fill(BLUE)

        pos = (50, 0)

        #show picture on the screen and background image
        screen.blit(bk_bigger, bk_bigger.get_rect(center=(600, 500)))
        screen.blit(img, img.get_rect(center=(300, 350)))
        rotate2(screen, part_s, pos, angle)
        angle += 1

        pygame.display.flip()
        clock.tick(speed)
#running the main function and game loop
if __name__ == "__main__":
    main()