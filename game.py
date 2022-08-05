import pygame
import random

pygame.init()

HEIGHT = 600
WIDTH = 600
FPS = 60

win = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('Dont tap')

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 100
        self.h = 100

    def draw(self, win):
        self.tile = pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.w, self.h))
    
    def getrect(self):
        return self.tile

def drawWindow(win, tile_list, scoreCount, timeLeft):
    win.fill((255, 255, 255))
    for tile in tile_list:
        tile.draw(win)
    win.blit(scoreCount, (0, 0))
    win.blit(timeLeft, (0, 34))
    pygame.display.update()

def gameover(win, text):
    win.fill((255, 255, 255))
    win.blit(text, (0, 300))
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    tile_list = [Tile(250, 250)]
    font = pygame.font.SysFont(None, 50)
    score = 0 
    timer = 30
    dt = 0
    while run: 
        pos = mousex, mousey = pygame.mouse.get_pos()
        if timer <= 0:
            gameover(win, font.render(f'Your score is {score} press SPACE to retry', True, (255, 0, 0)))
            for event in pygame.event.get():
                if event.type == pygame.QUIT: run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: 
                        timer = 30
                        score = 0
        else: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: run = False
                if event.type == pygame.MOUSEBUTTONDOWN and tile_list[0].tile.collidepoint(pos):
                    tile_list.pop()
                    tile_list.append(Tile(random.randint(0, 500), random.randint(0, 500)))
                    score += 1
            scoreCount = font.render(f'Score: {score}', True, (255, 0, 0))
            timeLeft = font.render(f'Time left: {int(timer)}', True, (255, 0, 0))
            drawWindow(win, tile_list, scoreCount, timeLeft)

        timer -= dt
        dt = clock.tick(60) / 1000
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
