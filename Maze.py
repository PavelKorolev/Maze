"""Импорт необходимыых библиотек"""
import pygame
from Classes.Player import Player
from Classes.Wall import Wall
from Classes.Coin import Coin
from Classes.Enemy import Enemy
from Classes.Menu import Menu

'''Основные константы'''
WHITE = (255, 255, 255)
BLUE = (29, 32, 76)
MENU_BACKGROUND = (35, 178, 239)
TIMER_COLOR = (37, 255, 168)
TIMER_SECONDS = 120

'''Параметры окна игры'''
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

'''Настройки главного героя'''
HERO_SPEED = 16

'''Музыка'''
pygame.mixer.init()
bg_music = pygame.mixer.Sound("Sources/sound.mp3")
award_sound = pygame.mixer.Sound("Sources/game-award.mp3")
dolphin_sound = pygame.mixer.Sound("Sources/dolphin-sound.mp3")
bg_music.play(100)

'''Пауза'''
pause = False

"""Описание классов"""

'''Инициализация игры'''
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
menu = pygame.Surface([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Maze")

all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

'Создание стен'
wall_positions = [
    # Borders
    [0, 0, 10, 800],
    [1190, 0, 10, 800],
    [10, 0, 1190, 10],
    [10, 790, 1190, 10],

    # In Game
    [10, 80, 265, 10],
    [133, 80, 10, 80],
    [10, 240, 265, 10],
    [133, 250, 10, 70],
    [133, 320, 133, 10],
    [10, 400, 133, 10],
    [133, 490, 10, 230],
    [133, 490, 133, 10],
    [10, 640, 265, 10],

    [533, 80, 10, 80],
    [275, 160, 133, 10],
    [400, 10, 10, 60],
    [400, 160, 10, 470],
    [400, 710, 265, 10],
    [400, 480, 133, 10],
    [400, 320, 133, 10],
    [533, 240, 10, 90],
    [533, 410, 10, 310],

    [533, 240, 133, 10],
    [533, 630, 133, 10],

    [665, 10, 10, 160],
    [665, 410, 10, 230],
    [665, 160, 133, 10],
    [685, 320, 240, 10],
    [665, 480, 133, 10],

    [800, 10, 10, 80],
    [800, 240, 10, 400],
    [800, 240, 143, 10],
    [800, 720, 270, 10],
    [940, 400, 10, 320],
    [1070, 400, 10, 330],
    [940, 10, 10, 80],
    [940, 80, 133, 10],
    [940, 160, 133, 10],
    [940, 160, 10, 90],
    [1070, 240, 10, 80],
    [1070, 240, 133, 10],
]
for coord in wall_positions:
    wall = Wall(coord[0], coord[1], coord[2], coord[3], BLUE)
    wall_list.add(wall)
    all_sprite_list.add(wall)

'Создание монет'
coins_list = pygame.sprite.Group()
coins_coord = [
    [700, 30],
    [30, 440],
    [160, 515],
    [30, 667],
    [700, 515],
    [830, 350],
    [30, 270],
    [1100, 700],
    [1100, 415],
    [700, 360],
]

for coord in coins_coord:
    coin = Coin(coord[0], coord[1], "Sources/shell2.jpg")
    coins_list.add(coin)
    all_sprite_list.add(coin)

'Создание врагов'
enemies_list = pygame.sprite.Group()
enemies_positions = [
    [295, 200, (0, 13), 0, 450],
    [970, 193, (0, 8), 0, 350],
    [300, 73, (4, 0), 120, 0],
    [30, 170, (6, 0), 120, 0],
]
for coord in enemies_positions:
    enemy = Enemy(coord[0], coord[1], coord[2], coord[3], coord[4], "Sources/shell3.jpg")
    enemies_list.add(enemy)
    all_sprite_list.add(enemy)


'Создание игрока'
player = Player(430, 350, "Sources/main-hero-right.png", award_sound)
player.walls = wall_list
all_sprite_list.add(player)

player.coins = coins_list

player.enemies = enemies_list

font = pygame.font.SysFont("Ink Free", 90, True)
fontArial = pygame.font.SysFont("Arial", 90, True)
text = font.render("GAME OVER", True, WHITE)
text_win = font.render("YOU WIN", True, WHITE)

'''Создание пунктов меню'''
menu_options = [
    ((440, 250), (300, 100), " Game", (250, 250, 30), (250, 30, 30), 0),
    ((440, 350), (300, 100), "  Quit", (250, 250, 30), (250, 30, 30), 1)
]
game_menu = Menu(menu_options)
game_menu.start(menu, screen, MENU_BACKGROUND)
done = False

clock = pygame.time.Clock()
counter, text1 = TIMER_SECONDS, str(TIMER_SECONDS).rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            if not pause:
                counter -= 1
                text1 = str(counter).rjust(3) if counter > 0 else '0'
                if counter <= 0:
                    player.alive = False
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
            if event.key == pygame.K_ESCAPE:
                pause = not pause

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.change_x = -HERO_SPEED
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.change_x = HERO_SPEED
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                player.change_y = -HERO_SPEED
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.change_y = HERO_SPEED

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.change_x = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.change_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                player.change_y = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.change_y = 0

    screen.blit(pygame.image.load("Sources/bg1.png"), (0, 0))

    if not player.alive:
        screen.blit(text, (290, 280))
    elif player.collected_coins >= len(coins_coord):
        screen.blit(text_win, (350, 280))
    else:
        if not pause:
            all_sprite_list.update()
        all_sprite_list.draw(screen)
        screen.blit(fontArial.render(text1, True, TIMER_COLOR), (1050, 45))

    print(pygame.mouse.get_pos())
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
