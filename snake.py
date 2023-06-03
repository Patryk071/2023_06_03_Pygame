import pygame
import random
pygame.font.init()

WIDTH, HEIGHT = 480, 480
SIZE = 20
WIDTH_BOX = WIDTH // SIZE
HEIGHT_BOX = HEIGHT // SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)

class Snake():
    def __init__(self):
        self.__len = 1
        self.__position = [(WIDTH // 2, HEIGHT // 2)]
        self.__move_direction = UP
        self.color = GREEN
        self.store = 0

    #pozycja głowy
    #zracamy ostatni element z listy pozycji weza
    def head_position(self):
        return self.__position[-1]

    #kierunek weza
    def direction(self, move_direction):
        if self.__len > 1 and (move_direction[0] * -1, move_direction[1] * -1) == self.__move_direction:
            return
        else:
            self.__move_direction = move_direction

    #sterowanie wezem
    def move(self):
        head = self.head_position()
        x, y = self.__move_direction

        new_position = (((head[0] + (x * SIZE)) % WIDTH), (head[1] + (y * SIZE)) % HEIGHT)

        #uderzam w swoj ogon
        if len(self.__position) > 2 and new_position in self.__position[2:]:
            self.reset()
        #czy uderzyłam w prawą lub lewą ścianę
        elif (new_position[0] == 0 and x == 1) or (new_position[0] == 460 and x == -1):
            self.reset()
        #czy uderzyłam w sufit lub podłogę
        elif (new_position[1] == 0 and y == 1) or (new_position[1] == 460 and y == -1):
            self.reset()
        #jeśli nowa pozycja jest OK, to zaktualizaj liste z wężem
        else:
            self.__position.append(new_position)
            if len(self.__position) > self.__len:
                del self.__position[0]

    #zbierenie pozywienia
    def eat(self):
        self.__len += 1
        self.store += 1

    def reset(self):
        self.__len = 1
        self.__position = [(WIDTH // 2, HEIGHT // 2)]
        self.__move_direction = UP
        self.color = GREEN
        self.store = 0

    #rysowanie
    def draw(self, win):
        for p in self.__position[::-1]:
            r = pygame.Rect((p[0], p[1]), (SIZE, SIZE))
            pygame.draw.rect(win, self.color, r)


class Food():
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.random_position()

    #losowa pozycja jedzenia
    def random_position(self):
        self.position = (random.randint(0, WIDTH_BOX - 1) * SIZE, random.randint(0, HEIGHT_BOX - 1) * SIZE) #czy na pewno odjac 1??

    #rysowanie jedzenia
    def draw(self, win):
        rect = pygame.Rect(self.position, (SIZE, SIZE))
        pygame.draw.rect(win, self.color, rect)


#rysowanie planszy - siatki
def draw_board(win):
    #tlo
    win.fill(BLACK)

    #linie poziome
    for i in range(0, int(WIDTH_BOX)):
        pygame.draw.line(win, GREY, (0, i * SIZE), (WIDTH, i * SIZE))
    #lienie pionowe
    for i in range(0, int(WIDTH_BOX)):
        pygame.draw.line(win, GREY, (i * SIZE, 0), (i * SIZE, WIDTH))

#głowny kod programu, sterowanie, rysowanie, gra
def main():
    pygame.init()

    #okno gry
    win = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    pygame.display.set_caption('Gra w węża')

    #rysowanie siatki
    draw_board(win)

    #inicjalizacja obiektów z klas
    snake = Snake()
    food = Food()

    #pętla główna programu
    run = True
    while (run):
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #sterowanie wężem
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: #gora
                    snake.direction(UP)
                elif event.key == pygame.K_DOWN: #dół
                    snake.direction(DOWN)
                elif event.key == pygame.K_LEFT: #lewo
                    snake.direction(LEFT)
                elif event.key == pygame.K_RIGHT: #prawo
                    snake.direction(RIGHT)

        snake.move()
        #sprawdzenie, czy jedzenie powstało w miejscu weza
        if snake.head_position() == food.position:
            snake.eat()
            food.random_position()

        draw_board(win)
        snake.draw(win)
        food.draw(win)

        win.blit(win, (0, 0))

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()