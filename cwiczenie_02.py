import pygame
pygame.font.init() #obsługa czcionek

WIDTH, HEIGHT = 800, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moja pierwsza gra")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

RECT_WIDTH, RECT_HEIGHT = 20, 20

X = (WIDTH // 2) - (RECT_WIDTH // 2)
Y = (HEIGHT // 2) - (RECT_HEIGHT // 2)

STEP = 20

#pętla główna programu
run = True
while run:
    pygame.time.delay(50)

    #obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    #obsługa przycisków
    if keys[pygame.K_LEFT]: #w lewo
        X -= STEP
    if keys[pygame.K_RIGHT]: #w prawo
        X += STEP
    if keys[pygame.K_UP]: #w górę
        Y -= STEP
    if keys[pygame.K_DOWN]: #w dół
        Y += STEP

    #"Czyszczenie ekranu"
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, (X, Y, RECT_WIDTH, RECT_HEIGHT))

    pygame.display.update()

pygame.quit()