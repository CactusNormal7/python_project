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
        if self.speed > 500:
            self.speed = 500

    def on_collide_trap(self,difficulty):
        if difficulty == "easy":
            self.size = self.size // 2
        elif difficulty == "medium":
            self.size = self.size // 3
        else:
            self.size = self.size // 4

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


class Hud:
    def __init__(self, score, size, speed, difficulty):
        self.score = score
        self.size = size
        self.speed = speed
        self.difficulty = difficulty

    def display_hud(self,screen):
        font = pygame.font.Font(None, 24)
        text_color = (255, 255, 255)
        
        score_text = font.render("Score: {}".format(self.score), True, text_color)
        size_text = font.render("Size: {}".format(self.size), True, text_color)
        speed_text = font.render("Speed: {}".format(self.speed), True, text_color)
        difficulty_text = font.render("Difficulty: {}".format(self.difficulty), True, text_color)

        screen.blit(score_text, (10, 10))
        screen.blit(size_text, (10, 40))
        screen.blit(speed_text, (10, 70))
        screen.blit(difficulty_text, (10, 100))


class Trap:
    def __init__(self, size, color,x,y,screen):
        self.size = size
        self.color = color
        self.x = x
        self.y = y
        self.__screen = screen

    def display(self):
        pygame.draw.circle(self.__screen, self.color, (self.x, self.y), self.size)
