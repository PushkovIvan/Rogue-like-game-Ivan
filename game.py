import pgzrun
import pygame
import random
import math

class AnimatedSprite:
    def __init__(self, x, y, frames, frame_duration):
        self.x = x
        self.y = y
        self.frames = frames  
        self.frame_index = 0  
        self.frame_duration = frame_duration  
        self.frame_timer = 0  

    def update(self):
        self.frame_timer += 1
        if self.frame_timer >= self.frame_duration:
            self.frame_timer = 0
            self.frame_index += 1
            if self.frame_index >= len(self.frames):
                self.frame_index = 0

    def draw(self):
        current_frame = self.frames[self.frame_index]
        screen.blit(current_frame, (self.x, self.y))

WIDTH = 850
HEIGHT = 600
TITLE = "Hungry cat"
game_started = False
game_lose = 0
result = 0
music_flag = 0

target = Actor("kitecat")

hero_frame1 = pygame.image.load('images/cat/up11.png')
hero_frame2 = pygame.image.load('images/cat/up22.png')
hero_frame3 = pygame.image.load('images/cat/up33.png')

hero_frame4 = pygame.image.load('images/cat/down11.png')
hero_frame5 = pygame.image.load('images/cat/down22.png')
hero_frame6 = pygame.image.load('images/cat/down33.png')

hero_frame7 = pygame.image.load('images/cat/left11.png')
hero_frame8 = pygame.image.load('images/cat/left22.png')
hero_frame9 = pygame.image.load('images/cat/left33.png')

hero_frame10 = pygame.image.load('images/cat/right11.png')
hero_frame11 = pygame.image.load('images/cat/right22.png')
hero_frame12 = pygame.image.load('images/cat/right33.png')

enemy_frame1 = pygame.image.load('images/dog/up11.png')
enemy_frame2 = pygame.image.load('images/dog/up22.png')
enemy_frame3 = pygame.image.load('images/dog/up33.png')

enemy_frame4 = pygame.image.load('images/dog/down11.png')
enemy_frame5 = pygame.image.load('images/dog/down22.png')
enemy_frame6 = pygame.image.load('images/dog/down33.png')

enemy_frame7 = pygame.image.load('images/dog/left11.png')
enemy_frame8 = pygame.image.load('images/dog/left22.png')
enemy_frame9 = pygame.image.load('images/dog/left33.png')

enemy_frame10 = pygame.image.load('images/dog/right11.png')
enemy_frame11 = pygame.image.load('images/dog/right22.png')
enemy_frame12 = pygame.image.load('images/dog/right33.png')

hero_frames = [[hero_frame1, hero_frame2, hero_frame3], [hero_frame4, hero_frame5, hero_frame6], [hero_frame7, hero_frame8, hero_frame9], [hero_frame10, hero_frame11, hero_frame12]]

player = AnimatedSprite(400, 300, hero_frames[1], 20)

enemy_frames = [[enemy_frame1, enemy_frame2, enemy_frame3],[enemy_frame4, enemy_frame5, enemy_frame6],[enemy_frame7, enemy_frame8, enemy_frame9],[enemy_frame10, enemy_frame11, enemy_frame12]]

enemy1 = AnimatedSprite(800, 100, enemy_frames[1], 20)
enemy2 = AnimatedSprite(700, 200, enemy_frames[1], 20)

start_button = Rect(300, 200, 230, 50)
sound_button = Rect(300, 300, 230, 50)
exit_button = Rect(300, 400, 230, 50)
quit_button = Rect(300, 250, 230, 50)

def draw():
    screen.clear()
    if not game_started:
        update()
        screen.draw.text("Главное меню", (270, 100), color="white", fontsize=60)
        screen.draw.filled_rect(start_button, "green")
        screen.draw.filled_rect(sound_button, "green")
        screen.draw.filled_rect(exit_button, "green")
        screen.draw.text("Начать игру", (364, 218), color="black", align='middle')
        screen.draw.text("Вкл/выкл музыку и звуки", (318, 320), color="black")
        screen.draw.text("Выход", (381, 420), color="black")
    elif game_started:
        update()
        screen.blit("background", (0,0))
        target.draw()
        player.draw()
        enemy1.draw()
        enemy2.draw()
        screen.draw.text("Результат игры "+str(result), (320, 20), color="white", fontsize=30)
        if game_lose:
            screen.draw.text("Игра окончена", (330, 150), color="white", fontsize=30)
            screen.draw.filled_rect(quit_button, "green")
            screen.draw.text("Выйти в главное меню", (325, 268), color="black", align='middle')
    
def update():
    if game_lose == 0:
        if keyboard.left and player.x > 0:
            player.x -= 2
            player.frames = hero_frames[2]
        elif keyboard.right and player.x < 850:
            player.x += 2
            player.frames = hero_frames[3]
        elif keyboard.up and player.y > 20:
            player.y -= 2
            player.frames = hero_frames[0]
        elif keyboard.down and player.y < 600:
            player.y += 2
            player.frames = hero_frames[1]

        if enemy1.x == 800 and enemy1.y < 500:
            enemy1.y += 1
            enemy1.frames = enemy_frames[1]
        elif enemy1.y == 500 and enemy1.x > 100:
            enemy1.x -= 1
            enemy1.frames = enemy_frames[2]
        elif enemy1.x == 100 and enemy1.y > 100:
            enemy1.y -= 1
            enemy1.frames = enemy_frames[0]
        elif enemy1.y == 100 and enemy1.x < 800:
            enemy1.x += 1
            enemy1.frames = enemy_frames[3]
        
        if enemy2.x == 700 and enemy2.y < 400:
            enemy2.y += 1
            enemy2.frames = enemy_frames[1]
        elif enemy2.y == 400 and enemy2.x > 200:
            enemy2.x -= 1
            enemy2.frames = enemy_frames[2]
        elif enemy2.x == 200 and enemy2.y > 200:
            enemy2.y -= 1
            enemy2.frames = enemy_frames[0]
        elif enemy2.y == 200 and enemy2.x < 700:
            enemy2.x += 1
            enemy2.frames = enemy_frames[3]
        if (abs(player.x + 25 - target.x) <= 40) and (abs(player.y + 50 - target.y) <= 40):
            global result
            result += 1
            target.pos = (random.randrange(20, 800, 10),random.randrange(20, 550, 10))
        if ((abs(player.x - enemy1.x) <= 40) and (abs(player.y - enemy1.y) <= 40)) or ((abs(player.x - enemy2.x) <= 40) and (abs(player.y - enemy2.y) <= 40)):
            end_game()
        player.update()
        enemy1.update()
        enemy2.update() 

def end_game():
    global game_lose
    game_lose = 1
    print("End of game...")

def quit_game():
    print("Quit to menu...")
    global game_started 
    game_started = False
    global game_lose
    game_lose = 0
    global result
    result = 0
    player.x = 400
    player.y = 300
    enemy1.x = 800
    enemy1.y = 100
    enemy2.x = 700
    enemy2.y = 200

def on_mouse_down(pos):
    if not game_started and not game_lose:
        if start_button.collidepoint(pos):
            start_game()
            
        elif sound_button.collidepoint(pos):
            sound_on()
        elif exit_button.collidepoint(pos):
            print("Exit from game")
            music.play_once('button')
            exit()
    if game_lose:
        if quit_button.collidepoint(pos):
            quit_game()
            global music_flag
            if music_flag == 0:
                music.play_once('button')

def start_game():
    print("Starting the game...")
    global game_started 
    game_started = True

def sound_on():
    global music_flag
    if music_flag == 0:
        print("Starting sound...")
        music.play('back_sound')
        music_flag = 1
    elif music_flag == 1:
        print("Make a quite")
        music.stop()
        music_flag = 0

pgzrun.go()





