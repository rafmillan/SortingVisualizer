import pygame, sys, random
from quickSort import *
from bubbleSort import *
from mergeSort import *
from insertionSort import *
from selectionSort import *

WIDTH = 600
HEIGHT = 600

mainClock = pygame.time.Clock()
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
win.fill((0,0,0))
pygame.display.set_caption("Sorting Visualizer")
pygame.font.init() 
myfont = pygame.font.SysFont('Arial', 20)

click = False

class Array:
    def __init__(self):
        self.size = 100
        self.arr = list(range(0, 501, 5))
        random.shuffle(self.arr)

    def getSize(self):
        return len(self.arr)
    
    def getArr(self):
        return self.arr

    def draw(self):
        left = 0
        for item in self.arr:
            bar = pygame.Rect(left, HEIGHT-item, 6, item)
            pygame.draw.rect(win, (255, 255, 255), bar)
            left = left + 6

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def menu():
    while True:
        win.fill((0,0,0))
        draw_text('CHOSE ALGORITHM', myfont, (255, 255, 255), win, (WIDTH/2)-65, 20)
        
        mx, my = pygame.mouse.get_pos()
 
        button1 = pygame.Rect((WIDTH/2)-100, 100, 200, 50)
        button2 = pygame.Rect((WIDTH/2)-100, 160, 200, 50)
        button3 = pygame.Rect((WIDTH/2)-100, 220, 200, 50)
        button4 = pygame.Rect((WIDTH/2)-100, 280, 200, 50)
        button5 = pygame.Rect((WIDTH/2)-100, 340, 200, 50)

        if button1.collidepoint((mx, my)):
            if click:
                quickSort()
        if button2.collidepoint((mx, my)):
            if click:
                bubbleSort()
        if button3.collidepoint((mx, my)):
            if click:
                mergeSort()
        if button4.collidepoint((mx, my)):
            if click:
                insertionSort()
        if button5.collidepoint((mx, my)):
            if click:
                selectionSort()

        pygame.draw.rect(win, (255, 255, 255), button1)
        draw_text('QUICK SORT', myfont, (0,0,0), win, (WIDTH/2)-35, 115)

        pygame.draw.rect(win, (255, 255, 255), button2)
        draw_text('BUBBLE SORT', myfont, (0,0,0), win, (WIDTH/2)-40, 175)

        pygame.draw.rect(win, (255, 255, 255), button3)
        draw_text('MERGE SORT', myfont, (0,0,0), win, (WIDTH/2)-37, 235)

        pygame.draw.rect(win, (255, 255, 255), button4)
        draw_text('INSTERTION SORT', myfont, (0,0,0), win, (WIDTH/2)-55, 295)

        pygame.draw.rect(win, (255, 255, 255), button5)
        draw_text('SELECTION SORT', myfont, (0,0,0), win, (WIDTH/2)-53, 355)

 
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pyK_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)

def quickSort():
    run = True
    array = Array()
    sort = False
    while run:
        win.fill((0,0,0))
        draw_text('QUICK SORT', myfont, (255, 255, 255), win, (WIDTH/2)-35, 20)

        array.draw()

        if not sort:
            #pygame.time.delay(1000)
            runQuickSort(array, 0, array.getSize() - 1, win)
            sort = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        
        pygame.display.update()
        mainClock.tick(60)

def bubbleSort():
    run = True
    array = Array()
    sort = False
    while run:
        win.fill((0,0,0))

        array.draw()
        if not sort:
            #pygame.time.delay(1000)
            runBubbleSort(array.getArr())
            sort =  True

        draw_text('BUBBLE SORT', myfont, (255, 255, 255), win, (WIDTH/2)-40, 20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        
        pygame.display.update()
        mainClock.tick(60)

def mergeSort():
    run = True
    array = Array()
    sort = False
    while run:
        win.fill((0,0,0))
        array.draw()
        draw_text('MERGE SORT', myfont, (255, 255, 255), win, (WIDTH/2)-37, 20)

        array.draw()
        if not sort:
            runMergeSort(array.getArr(), 0, array.getSize() - 1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        
        pygame.display.update()
        mainClock.tick(60)

def insertionSort():
    run = True
    array = Array()
    sort = False
    while run:
        win.fill((0,0,0))
        array.draw()

        if not sort:
            runInsertionSort(array.getArr())
            sort = True

        draw_text('INSERTION SORT', myfont, (255, 255, 255), win, (WIDTH/2)-55, 20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        
        pygame.display.update()
        mainClock.tick(60)

def selectionSort():
    run = True
    array = Array()
    sort = False
    while run:
        win.fill((0,0,0))
        array.draw()
        if not sort:
            runSelectionSort(array.getArr())
            sort = True
            
        draw_text('SELECTION SORT', myfont, (255, 255, 255), win, (WIDTH/2)-53, 20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        
        pygame.display.update()
        mainClock.tick(60)

        


if __name__ == "__main__":
    menu()
