import pygame
pygame.font.init()

WIDTH, HEIGHT = 800, 400
SPACESHIP_WIDTH = 40
SPACESHIP_HEIGHT = 60

# okno gry
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Gra w statki')

FPS = 60
STEP = 5

GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)

#łądowanie obrazków
#przeskalowanie
SPACE = pygame.transform.scale(pygame.image.load('ribbon-light-space.jpg'), (WIDTH, HEIGHT))

WHITE_SPACESHIP_IMAGE = pygame.transform.scale(pygame.image.load('spaceship_white.png'), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
WHITE_SPACESHIP = pygame.transform.rotate(WHITE_SPACESHIP_IMAGE, 270)
YELLOW_SPACESHIP_IMAGE = pygame.transform.scale(pygame.image.load('spaceship_yellow.png'), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP_IMAGE, 90)


def draw_window(white, yellow):
    WIN.blit(SPACE, (0, 0))
    WIN.blit(WHITE_SPACESHIP, (white.x, white.y))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    pygame.display.update()


def white_move(keys_pressed, white):
    if keys_pressed[pygame.K_w]: #góra
        white.y -= STEP
    if keys_pressed[pygame.K_s]: #dół
        white.y += STEP
    if keys_pressed[pygame.K_d]: #prawo
        white.x += STEP
    if keys_pressed[pygame.K_a]: #lewo
        white.x -= STEP

#głowny kod programu, sterowanie, rysowanie, gra
def main():
    #pygame.init()

    white = pygame.Rect(100, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(300, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()

    #pętla główna programu
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        white_move(keys_pressed, white)

        draw_window(white, yellow)

    pygame.quit()


if __name__ == '__main__':
    main()