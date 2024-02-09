import pygame
import menu
import game


def sqrt(x):
    return x ** 0.5


# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Screen size
screen_width = 800
screen_height = 600
speed = 6
cell_size = 20

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simplified Agar.io")

clock = pygame.time.Clock()

is_mouse = True
is_started = False

def start_stop():
    global is_started
    if is_started:
        is_started = False
    else:
        is_started = True

# Main function
def main():
    main_menu = menu.Menu()
    player = game.Player(screen_width // 2, screen_height // 2, cell_size, RED, screen)

    running = True
    
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                

        if is_started:
            if is_mouse:
                mouse_pos = pygame.mouse.get_pos()
                dx = mouse_pos[0] - player.x
                dy = mouse_pos[1] - player.y
                distance = sqrt(dx ** 2 + dy ** 2)
                if distance > 0:
                    if mouse_pos[0] >= (player.x + 8) or mouse_pos[0] <= (player.x - 8):
                        ratio = speed / distance
                        player.x += dx * ratio
                        player.y += dy * ratio
            else:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_Z]:
                    player.x -= 5
                if keys[pygame.K_Q]:
                    player.x += 5
                if keys[pygame.K_S]:
                    player.y -= 5
                if keys[pygame.K_D]:
                    player.y += 5
            player.display()
            
        else:
            main_menu.display(screen, lambda : start_stop())
            
            
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()