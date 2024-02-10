import pygame
import menu
import game
import random


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
cell_size = 20
cell_amout = 10

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simplified Agar.io")
main_menu = menu.Menu("mouse", "easy")

clock = pygame.time.Clock()

is_mouse = True
is_started = False

def control_change():
    global is_mouse
    if is_mouse:
        main_menu.control = "Keyboard"
        is_mouse = False
    else:
        main_menu.control = "Mouse"
        is_mouse = True

def start_stop():
    global is_started
    if is_started:
        is_started = False
    else:
        is_started = True

def add_cell(cells_list,screen):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    cells_list.append(game.Cells(x,y,screen,5,RED))


def handle_collision(player, cells_list):
    for cell in cells_list:
        distance = sqrt((player.x - cell.x) ** 2 + (player.y - cell.y) ** 2)
        if distance <= player.size + cell.size:
            add_cell(cells_list, screen)
            cell.on_collide(cells_list)
            player.on_collide()



# Main function
def main():
    player = game.Player(screen_width // 2, screen_height // 2, cell_size, RED, screen, 5)
    cells_list = []
    for _ in range(cell_amout):
        add_cell(cells_list, screen)
    running = True
    
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                

        if is_started:
            #command section
            if is_mouse:
                mouse_pos = pygame.mouse.get_pos()
                dx = mouse_pos[0] - player.x
                dy = mouse_pos[1] - player.y
                distance = sqrt(dx ** 2 + dy ** 2)
                if distance > 0:
                    if mouse_pos[0] >= (player.x + 10) or mouse_pos[0] <= (player.x - 10):
                        ratio = player.speed / distance
                        player.x += dx * ratio
                        player.y += dy * ratio
            else:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:
                    player.x -= player.speed
                if keys[pygame.K_d]:
                    player.x += player.speed
                if keys[pygame.K_z]:
                    player.y -= player.speed
                if keys[pygame.K_s]:
                    player.y += player.speed
            #collide section
            handle_collision(player,cells_list)

            #display section
            player.display()
            for cell in cells_list:
                cell.display()
            
        else:
            main_menu.display(screen, lambda : start_stop())
            main_menu.display_control(screen, lambda : control_change())
            
            
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()