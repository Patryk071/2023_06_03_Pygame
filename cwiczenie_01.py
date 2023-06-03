import pygame

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moja pierwsza gra")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

X, Y = 10, 10
RECT_WIDTH, RECT_HEIGHT = 20, 20
X1, X2 = 50, 250
Y1, Y2 = 100, 300

#pętla główna programu
run = True
while run:
    #obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        pygame.draw.rect(WIN, WHITE, (X, Y, RECT_WIDTH, RECT_HEIGHT))
        pygame.draw.circle(WIN, WHITE, (X + 10, Y + 60), 20, 0)

        #linia pozioma - rózne X
        pygame.draw.line(WIN, RED, (X1, Y), (X2, Y), 5)
        #linia lionowa - rózne Y
        pygame.draw.line(WIN, GREEN, (X, Y1), (X, Y2), 5)

        #plus
        pygame.draw.line(WIN, RED, (X1, 200), (X2, 200), 6)
        pygame.draw.line(WIN, GREEN, (150 - 3, Y1), (150 - 3, Y2), 6)

        pygame.display.update()