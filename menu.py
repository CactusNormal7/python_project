import pygame

class Menu:
    def display(self, screen, button_start):
        button_font = pygame.font.Font(None, 36)
        button_text = button_font.render("Start", True, (255, 255, 255))
        button_rect = button_text.get_rect(center=screen.get_rect().center)
        screen.blit(button_text, button_rect)
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                button_start()
