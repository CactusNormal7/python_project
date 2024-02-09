import pygame



class Player:
    def __init__(self, x, y, size, color, scr):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.__screen = scr

    def display(self):
        pygame.draw.circle(self.__screen, self.color, (self.x, self.y), self.size)

