import pygame
import menu
import game
import time
import random


def sqrt(x):
    return x ** 0.5


# Initialize Pygame
pygame.init()

time_to_play = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)

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
is_gamer_over = False


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


def game_over():
    global is_gamer_over
    if is_gamer_over:
        is_gamer_over = False
    else:
        is_gamer_over = True


def add_cell(cells_list,screen):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    cells_list.append(game.Cells(x,y,screen,5,BLUE))

def add_trap(trap_list, screen):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    size = random.randint(40,150)
    trap_list.append(game.Trap(size,GREEN,x,y,screen))

def handle_collision_playerXcells(player, cells_list):
    for cell in cells_list:
        distance = sqrt((player.x - cell.x) ** 2 + (player.y - cell.y) ** 2)
        if distance <= player.size + cell.size:
            add_cell(cells_list, screen)
            cell.on_collide(cells_list)
            player.on_collide()

def handle_collision_playerXtraps(player, trap_list,difficuty):
    for trap in trap_list:
        distance = sqrt((player.x - trap.x) ** 2 + (player.y - trap.y) ** 2)
        if distance <= player.size + trap.size:
            if player.size > trap.size :
                player.on_collide_trap(difficuty)
            

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

def restart():
    game_over()
    start_stop()
    main()

def main():
    player = game.Player(screen_width // 2, screen_height // 2, cell_size, RED, screen, 5)
    hud = game.Hud(player.score, player.size, player.speed, difficulty)
    running = True
    start_time = None
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        if is_started:
            if is_gamer_over:
                main_menu.display_game_over(screen,player.score ,lambda : restart())
            else:
                if start_time is None:
                    start_time = time.time()
                elapsed_time = time.time() - start_time
                remaining_time = time_to_play - elapsed_time
                if remaining_time <= 0:
                    game_over()
                clock.tick(30)
                diviser = player.speed/12
                speed = player.speed / (diviser + 2)
                if player.x <= 10:
                    player.x = 770
                elif player.x >= 780:
                    player.x = 12
                if player.y >= 580:
                    player.y = 30
                elif player.y <= 20:
                    player.y = 570
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
                        player.x -= speed
                    if keys[pygame.K_d]:
                        player.x += speed
                    if keys[pygame.K_z]:
                        player.y -= speed
                    if keys[pygame.K_s]:
                        player.y += speed

                #-------------------
                handle_collision_playerXcells(player,cells_list)
                handle_collision_playerXtraps(player,traps_list,difficulty)
                #-------------------
                player.display()
                updateHud(player,hud)
                hud.timer = round(remaining_time)
                hud.display_hud(screen)
                for cell in cells_list:
                    cell.display()
                for trap in traps_list:
                    trap.display()
            
        else:
            clock.tick(18)
            main_menu.display(screen, lambda : start_stop())
            main_menu.display_control(screen, lambda : control_change())
            main_menu.display_difficulty(screen, lambda : diff_change())
            cells_list = []
            traps_list = []
            generate_cells(cells_list)
            generate_trap(traps_list)
        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    main()