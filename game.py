import pygame



class Player:
    def __init__(self, x, y, size, color, scr, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.color = color
        self.__screen = scr
        self.score = 0


    def display(self):
        pygame.draw.circle(self.__screen, self.color, (self.x, self.y), self.size)

    def on_collide(self):
        self.size += 2
        self.speed += 5
        self.score += 1

class Cells:
    def __init__(self,x,y,scr,size,color):
        self.x = x
        self.y = y
        self.__screen = scr
        self.size = size
        self.color = color

    def display(self):
        pygame.draw.circle(self.__screen, self.color, (self.x, self.y), self.size)

    def on_collide(self, cell_list):
        cell_list.remove(self)