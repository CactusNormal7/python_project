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
cell_amout = 0
trap_amout = 0

difficulty = "easy"

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simplified Agar.io")
main_menu = menu.Menu("mouse", "easy")

clock = pygame.time.Clock()

is_mouse = True
is_started = False

def updateHud(player, hud):
    hud.score = player.score
    hud.size = player.size
    hud.speed = player.speed
    hud.difficulty = difficulty

def diff_change():
    global difficulty
    if difficulty == "easy":
        difficulty = "medium"
        main_menu.difficulty = "medium"
    elif difficulty == "medium":
        difficulty = "hard"
        main_menu.difficulty = "hard"
    else:
        difficulty = "easy"
        main_menu.difficulty = "easy"


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

def add_trap(trap_list, screen):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    trap_list.append(game.Trap(30,RED,x,y,screen))

def handle_collision(player, cells_list):
    for cell in cells_list:
        distance = sqrt((player.x - cell.x) ** 2 + (player.y - cell.y) ** 2)
        if distance <= player.size + cell.size:
            add_cell(cells_list, screen)
            cell.on_collide(cells_list)
            player.on_collide()

def generate_cells(cells_list):
    if difficulty == 'easy':
        cell_amout = 5
    elif difficulty == 'medium':
        cell_amout = 3
    else:
        cell_amout = 2

    for _ in range(cell_amout):
        add_cell(cells_list, screen)

def generate_trap(trap_list):
    global trap_amout
    if difficulty == 'easy':
        trap_amout = 2
    elif difficulty == 'medium':
        trap_amout = 3
    else:
        trap_amout = 4
    for _ in range(trap_amout):
        add_trap(trap_list, screen)

# Main function
def main():
    player = game.Player(screen_width // 2, screen_height // 2, cell_size, RED, screen, 5)
    hud = game.Hud(player.score, player.size, player.speed, difficulty)
    running = True
    
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                

        if is_started:
            diviser = player.speed/12
            speed = player.speed / (diviser + 2)
            print(speed)
            if is_mouse:
                mouse_pos = pygame.mouse.get_pos()
                dx = mouse_pos[0] - player.x
                dy = mouse_pos[1] - player.y
                distance = sqrt(dx ** 2 + dy ** 2)
                if distance > 0:
                    if mouse_pos[0] >= (player.x + 10) or mouse_pos[0] <= (player.x - 10):
                        ratio = (speed) / distance
                        player.x += dx * ratio
                        player.y += dy * ratio
            else:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:
                    player.x -= player.speed / diviser
                if keys[pygame.K_d]:
                    player.x += player.speed/ diviser
                if keys[pygame.K_z]:
                    player.y -= player.speed/ diviser
                if keys[pygame.K_s]:
                    player.y += player.speed/ diviser
            #collide section
            handle_collision(player,cells_list)

            #display section
            player.display()
            updateHud(player,hud)
            hud.display_hud(screen)
            for cell in cells_list:
                cell.display()
            for trap in traps_list:
                trap.display()
            
        else:
            main_menu.display(screen, lambda : start_stop())
            main_menu.display_control(screen, lambda : control_change())
            main_menu.display_difficulty(screen, lambda : diff_change())
            cells_list = []
            traps_list = []
            generate_cells(cells_list)
            generate_trap(traps_list)
            
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()