import pygame

class Menu:
    def __init__(self,control,difficulty):
        self.control = control 
        self.difficulty = difficulty

    def display(self, screen, button_start):
        button_font = pygame.font.Font(None, 36)
        button_text = button_font.render("Start", True, (255, 255, 255))
        button_rect = button_text.get_rect(center=screen.get_rect().center)
        screen.blit(button_text, button_rect)
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                button_start()


    def display_control(self, screen, action):
        button_font = pygame.font.Font(None, 36)
        button_text = button_font.render(self.control, True, (255, 255, 255))
        button_rect = button_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 50))
        screen.blit(button_text, button_rect)
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                action()

    def display_difficulty(self,screen, action):
        button_font = pygame.font.Font(None, 36)
        button_text = button_font.render(self.difficulty, True, (255, 255, 255))
        button_rect = button_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 100))
        screen.blit(button_text, button_rect)
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                action()

    def display_game_over(self, screen, score, button_action):
        game_over_font = pygame.font.Font(None, 48)
        score_font = pygame.font.Font(None, 36)

        game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
        score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
        
        game_over_rect = game_over_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 50))
        score_rect = score_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))

        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)

        button_font = pygame.font.Font(None, 36)
        button_text = button_font.render("Restart", True, (255, 255, 255))
        button_rect = button_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 100))
        screen.blit(button_text, button_rect)

        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                button_action()
