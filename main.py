import pygame
import sys
import bg_menu
import json
import random
import math


ticker = pygame.time.Clock()
from pygame.locals import *
from pygame import mixer

# pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
#https://opengameart.org/content/scrolling-loopable-parallax-backgrounds
#https://opengameart.org/content/bg-layers



pygame.init()
mixer.init()
pygame.display.set_caption('CrazyExtremeFishing')
size = (900, 600)
font = pygame.font.Font("Minecraft.ttf", 50)
infoObject = pygame.display.Info()

ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
mixer.music.load("Assets/Songs/littleidea.mp3")
button_sound = mixer.Sound("Assets/Songs/button_sound.wav")
cash_sound = mixer.Sound("Assets/Songs/Cash.mp3")
catch_sound = mixer.Sound("Assets/Songs/catch_fish.mp3")
hook_sound = mixer.Sound("Assets/Songs/hook.mp3")

volume = 0.1
mixer.music.set_volume(volume)
button_sound.set_volume(volume)
cash_sound.set_volume(volume*2)
catch_sound.set_volume(volume*2)
hook_sound.set_volume(volume*2)
mixer.music.play(-1)
coeff_fps = 1
player_scale_x = 240
player_scale_y = 110
Player = [[pygame.transform.scale(pygame.image.load("Assets/Character/Boat1_withFishingRod1.png").convert_alpha(),
                                 (player_scale_x, player_scale_y)),
          pygame.transform.scale(pygame.image.load("Assets/Character/Boat1_withFishingRod2.png").convert_alpha(),
                                 (player_scale_x, player_scale_y)),
          pygame.transform.scale(pygame.image.load("Assets/Character/Boat1_withFishingRod3.png").convert_alpha(),
                                 (player_scale_x, player_scale_y)),
          pygame.transform.scale(pygame.image.load("Assets/Character/Boat1_withFishingRod4.png").convert_alpha(),
                                 (player_scale_x, player_scale_y))],
          [pygame.transform.scale(pygame.image.load(f"Assets/Character/Boat1_withFishingRod_green1.png").convert_alpha(),
                                 (player_scale_x, player_scale_y)),
          pygame.transform.scale(pygame.image.load("Assets/Character/Boat1_withFishingRod_green2.png").convert_alpha(),
                                 (player_scale_x, player_scale_y)),
          pygame.transform.scale(pygame.image.load("Assets/Character/Boat1_withFishingRod_green3.png").convert_alpha(),
                                 (player_scale_x, player_scale_y)),
          pygame.transform.scale(pygame.image.load("Assets/Character/Boat1_withFishingRod_green4.png").convert_alpha(),
                                 (player_scale_x, player_scale_y))],
          [pygame.transform.scale(pygame.image.load("Assets/Character/bateaupirate1.png").convert_alpha(),
                                 (player_scale_x+48, player_scale_y+95)),
          pygame.transform.scale(pygame.image.load("Assets/Character/bateaupirate2.png").convert_alpha(),
                                 (player_scale_x+48, player_scale_y+95)),
           pygame.transform.scale(pygame.image.load("Assets/Character/bateaupirate1.png").convert_alpha(),
                                 (player_scale_x+48, player_scale_y+95)),
          pygame.transform.scale(pygame.image.load("Assets/Character/bateaupirate2.png").convert_alpha(),
                                 (player_scale_x+48, player_scale_y+95))]]

Hook = [pygame.image.load("Assets/Hook.png"),pygame.image.load("Assets/Hook_magic.png")]
Hook_store = pygame.transform.scale(pygame.image.load("Assets/Hook_magic_store.png").convert_alpha(), (250, 250))
pirate_flag = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/pirateflag.png").convert_alpha(), (250, 250))
shop_cane = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/cane1.png").convert_alpha(), (250, 250))
shop_cane_2 = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/cane2.png").convert_alpha(), (250, 250))
shop_cane_3 = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/cane3.png").convert_alpha(), (250, 250))
shop_cane_4 = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/cane4.png").convert_alpha(), (250, 250))

black_square = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/black square.png").convert_alpha(),
                                      (254, 254))
logo = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/logo.png").convert_alpha(), (175, 65))
logo_pressed = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/logo_pressed.png").convert_alpha(),
                                      (175, 65))
reduce_logo_plus = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/reduce_logo_plus.png").convert_alpha(),
                                          (65, 65))
reduce_logo_plus_pressed = pygame.transform.scale(
    pygame.image.load("Assets/Start_Menu/reduce_logo_plus_pressed.png").convert_alpha(),
    (65, 65))
reduce_logo_minus = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/reduce_logo_minus.png").convert_alpha(),
                                           (65, 65))
reduce_logo_minus_pressed = pygame.transform.scale(
    pygame.image.load("Assets/Start_Menu/reduce_logo_minus_pressed.png").convert_alpha(),
    (65, 65))
logo_pause = pygame.transform.scale(
    pygame.image.load("Assets/Start_Menu/logo_pause.png").convert_alpha(),
    (65, 65))
logo_pause_pressed = pygame.transform.scale(
    pygame.image.load("Assets/Start_Menu/logo_pause_pressed.png").convert_alpha(),
    (65, 65))
logo_interrogation_pressed = pygame.transform.scale(
    pygame.image.load("Assets/Start_Menu/logo_interrogation_pressed.png").convert_alpha(), (65, 65))
logo_interrogation = pygame.transform.scale(
    pygame.image.load("Assets/Start_Menu/logo_interrogation.png").convert_alpha(), (65, 65))

logo_dollar_pressed = pygame.transform.scale(
    pygame.image.load("Assets/Start_Menu/logo_dollar_pressed.png").convert_alpha(), (65, 65))
logo_dollar = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/logo_dollar.png").convert_alpha(), (65, 65))

logo_night = pygame.transform.scale(
    pygame.image.load("Assets/Start_Menu/logo_night.png").convert_alpha(), (65, 65))

logo_sun = pygame.transform.scale(
    pygame.image.load("Assets/Start_Menu/logo_sun.png").convert_alpha(), (65, 65))

renard_loading = pygame.transform.scale(pygame.image.load("Assets/Start_Menu/Renard.png").convert_alpha(), (50, 41))
logo_game = pygame.image.load("Assets/Main/Logo_the fox fishing.png").convert_alpha()
cursor = pygame.transform.scale(pygame.image.load("Assets/Main/cursor.png").convert_alpha(), (50, 50))
BG_mainmenu = bg_menu.Background()
font2 = pygame.font.Font("Minecraft.ttf", 20)

data = {
    'money':500,
    'score':0,
    'magic_hook':0,
    'charac':0
}
d_intro = 0
try:
    with open('savegame.txt') as score_file:
        data = json.load(score_file)
except:
    print("Création d'un fichier score")
    d_intro = 1



class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, text):
        ecran.blit(self.image, (self.rect.x, self.rect.y))
        font = pygame.font.Font("Minecraft.ttf", 40)
        text_render = font.render(text, 1, (255, 255, 255))
        ecran.blit(text_render, (self.rect.x, self.rect.y))

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
                #button_sound.play()
            else:
                if self.clicked:
                    self.clicked = False
            return self.clicked


class Fishs(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.images = [[pygame.transform.scale(pygame.image.load("Assets/Character/Fish1.1.png"), (36, 20)),
                        pygame.transform.scale(pygame.image.load("Assets/Character/Fish1.2.png"), (36, 20))],
                       [pygame.transform.scale(pygame.image.load("Assets/Character/Fish2.1.png"), (36, 20)),
                        pygame.transform.scale(pygame.image.load("Assets/Character/Fish2.2.png"), (36, 20))],
                       [pygame.transform.scale(pygame.image.load("Assets/Character/Fish3.1.png"), (40, 24)),
                        pygame.transform.scale(pygame.image.load("Assets/Character/Fish3.2.png"), (40, 24))],
                       [pygame.transform.scale(pygame.image.load("Assets/Character/Fish4.1.png"), (60, 48)),
                        pygame.transform.scale(pygame.image.load("Assets/Character/Fish4.2.png"), (60, 48))],
                       [pygame.transform.scale(pygame.image.load("Assets/Character/Fish_malus_1.png"), (45, 33)),
                        pygame.transform.scale(pygame.image.load("Assets/Character/Fish_malus_1.png"), (45, 33))],
                       [pygame.transform.scale(pygame.image.load("Assets/Character/shark_1.png"), (175, 89)),
                        pygame.transform.scale(pygame.image.load("Assets/Character/shark_3.png"), (175, 89))]]
        self.choose = 0
        self.cc = 0
        self.x = x
        self.y = y
        self.velocity = random.randint(2, 5)
        self.direction = random.randrange(-1, 2, 2)
        self.image = random.randint(0, 5)
        self.bool = True
        self.hook = pygame.image.load("Assets/Hook.png")
        self.hookx = 0
        self.hooky = 0
        self.catched = []
        self.tosale = []
        self.money = 0
        self.inboated = False
        self.score = 0

    def spawn(self):
        if self.bool == True and self.direction == 1:
            ecran.blit(self.images[self.image][self.anim()], (self.x, self.y))
        elif self.bool == True and self.direction == -1:
            ecran.blit(pygame.transform.flip(self.images[self.image][self.anim()], True, False), (self.x, self.y))
        elif self.bool == False and self.direction == 1:
            ecran.blit(self.images[self.image][self.anim()], (self.x, self.y))
        elif self.bool == False and self.direction == -1:
            ecran.blit(pygame.transform.flip(self.images[self.image][self.anim()], True, False), (self.x, self.y))

    def move(self):
        if self not in self.catched and self not in self.tosale:
            self.x += self.velocity * self.direction

    def anim(self):
        self.cc += 0.2
        if self.cc > 1:
            self.choose += 1
            self.cc = 0

        if self.choose > 1:
            self.choose = 0
        return self.choose



    def catch(self, hookx, hooky, poisson,shoot,magic_hook,charac):
        coco = 0
        if self.x < hookx + 20 and self.x > hookx - 20 and self.y < hooky + 20 and self.y > hooky - 20 and poisson == False :
            print("Catch")
            if charac != 2 and self.image == 5:
                return poisson,shoot
            else:
                self.catched.append(self)
                poisson = True
                if magic_hook == 1:
                    shoot = False
                    time = False
        if coco == 1:
            self.text(hookx,hooky)
        else:
            self.stuckhook(hookx, hooky)

        return poisson,shoot

    def stuckhook(self, hookx, hooky):

        if self.catched != []:
            for e in self.catched:
                e.x = hookx
                e.y = hooky + 20

    def hookreturn(self, hookx, hooky, shoot, time, poisson, movex, movey,moving):
        if poisson == True and self.catched != [] and movex + 200 > hookx > movex - 20 and movey + 100 > hooky > movey - 20:
            shoot = False
            time = False
            poisson = False
            hookx = movex + 151
            hooky = movey + 37
            self.inboated = True
            self.tosale.append(self.catched[0])
            self.catched.clear()
            moving = False
            catch_sound.play()
        self.inboat(movex, movey,False)
        return hookx, hooky, poisson, shoot, time, moving

    def inboat(self, movex, movey,bool):
        if self.tosale :
            self.x = movex + 5
            self.y = movey + 37
        elif bool == True:
            self.x = 1000
            self.y = 1000

    def sold(self, argent, score,char):
        if self.inboated:
            if self.image == 0:
                self.money = random.randint(8, 12)
                self.score = 100
            elif self.image == 1:
                self.money = random.randint(13, 17)
                self.score = 150
            elif self.image == 2:
                self.money = random.randint(18, 22)
                self.score = 200
            elif self.image == 3:
                self.money = random.randint(22, 55)
                self.score = 500
            elif self.image == 4:
                self.money = random.randint(-50,-25)
            elif self.image == 5 and char == 2:
                self.money = random.randint(90, 120)
                self.score = 1000
            self.inboated = False

        argent += self.money
        score += self.score
        self.money = 0
        self.score = 0
        return argent, score




    """    def particles_sold(texte):
        text = pygame.font.Font("Minecraft.ttf", 18).render(f"{texte}$", 1, (127,255,0))
        textPos = (movex+200,movey)
        ecran.blit(text, textPos)"""




click = False


class Button_option:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, text):
        ecran.blit(self.image, (self.rect.x, self.rect.y))
        font = pygame.font.Font("Minecraft.ttf", 40)
        text_render = font.render(text, 1, (255, 255, 255))
        ecran.blit(text_render, (self.rect.x, self.rect.y + 15))

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
                button_sound.play()
            else:
                if self.clicked:
                    self.clicked = False
                    return True


click = False

clock = pygame.time.Clock()


def main_menu(volume):
    global ran
    clac = 0
    width = 800
    i = 0
    j = 0
    k = 0
    count = 0
    nat_count = 0
    ran = True
    def fadein():
        fade = pygame.Surface((infoObject.current_w,infoObject.current_h))
        fade.fill((0,0,0))
        for alpha in range(0,50):
            fade.set_alpha(alpha)
            ecran.blit(fade,(0,0))
            pygame.display.update()
            pygame.time.delay(5)
        return 0

    while ran:
        # update position

        ecran.fill((99, 155, 255))

        ecran.blit(BG_mainmenu.sky_bg, (i, 0))
        ecran.blit(BG_mainmenu.sky_bg, (width + i, 0))
        ecran.blit(BG_mainmenu.sky_bg, (width * 2 + i, 0))
        ecran.blit(BG_mainmenu.sky_bg, (width * 3 + i, 0))

        ecran.blit(BG_mainmenu.mountain_bg, (i, -100))
        ecran.blit(BG_mainmenu.mountain_bg, (width + i, -100))
        ecran.blit(BG_mainmenu.mountain_bg, (width * 2 + i, -100))
        ecran.blit(BG_mainmenu.mountain_bg, (width * 3 + i, -100))

        if i < -width:
            i = 0
        if j < -width:
            j = 0
        if k < -width:
            k = 0
        i -= 1
        j -= 10
        k -= 3
        ecran.blit(BG_mainmenu.forest_bg, (j, -90))
        ecran.blit(BG_mainmenu.forest_bg, (width + j, -90))
        ecran.blit(BG_mainmenu.forest_bg, (width * 2 + j, -90))
        ecran.blit(BG_mainmenu.forest_bg, (width * 3 + j, -90))
        ecran.blit(BG_mainmenu.forest_fg2, (k, 200))
        ecran.blit(BG_mainmenu.forest_fg2, (width + k, 200))
        ecran.blit(BG_mainmenu.forest_fg2, (width * 2 + k, 200))
        ecran.blit(BG_mainmenu.forest_fg2, (width * 3 + k, 200))
        ecran.blit(BG_mainmenu.forest_fg, (j, 280))
        ecran.blit(BG_mainmenu.forest_fg, (width + j, 280))
        ecran.blit(BG_mainmenu.forest_fg, (width * 2 + j, 280))
        ecran.blit(BG_mainmenu.forest_fg, (width * 3 + j, 280))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 2 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 3 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 4 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 5 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 6 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 7 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 8 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 9 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 10 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 11 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 12 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 13 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 14 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 15 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 16 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 17 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 18 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 19 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 20 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 21 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 22 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 23 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 24 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 25 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 26 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 27 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 28 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 29 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 30 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 31 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 32 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 33 + j, 437))
        ecran.blit(BG_mainmenu.nature_fg[nat_count], (width / 10 * 34 + j, 437))
        ecran.blit(font.render("IPS :" + str(int(clock.get_fps()) * coeff_fps), 1, (1, 1, 1)),
                   (infoObject.current_w * 1 - 200, infoObject.current_h * (1 / 54)))

        if count > 11:
            count = 0
        if nat_count > 7:
            nat_count = 0
        nat_count += 1
        p_x=150
        ecran.blit(BG_mainmenu.boat[count], (p_x, 600))
        count += 1

        play_button = Button(infoObject.current_w * (2 / 6), infoObject.current_h * (43 / 54), logo)
        options_button = Button(infoObject.current_w * (3 / 6), infoObject.current_h * (43 / 54), logo)
        quit_button = Button(infoObject.current_w * (4 / 6), infoObject.current_h * (43 / 54), logo)
        play_button_pressed = Button(infoObject.current_w * (2 / 6), infoObject.current_h * (43 / 54), logo_pressed)
        options_button_pressed = Button(infoObject.current_w * (3 / 6), infoObject.current_h * (43 / 54), logo_pressed)
        quit_button_pressed = Button(infoObject.current_w * (4 / 6), infoObject.current_h * (43 / 54), logo_pressed)

        if play_button.draw(" Jouer"):
            mixer.music.set_volume(0)
            button_sound.play()
            play_button_pressed.draw(" Jouer")
            a=1
            a=fadein()
            if a == 0:
                ran = False
                loading(volume)

        if options_button.draw(" Options"):
            button_sound.play()
            options_button_pressed.draw(" Options")
            volume2 = options(volume)
            volume = volume2

        if quit_button.draw(" Quitter"):
            button_sound.play()
            quit_button_pressed.draw(" Quitter")
            sys.exit()

        ecran.blit(logo_game, (infoObject.current_w * (2 / 5), infoObject.current_h * (2.5 / 4)))

        for event in pygame.event.get():
            if event.type == QUIT:
                with open('savegame.txt','w') as score_file:
                    json.dump(data,score_file)
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        ticker.tick(30)
        clock.tick()



def options(volume):
    global coeff_fps
    running = True
    volume *= 100
    ecran.fill((255, 125, 0))
    text = font.render("Options", 1, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (infoObject.current_w // 2, infoObject.current_h * (1 / 10))

    ecran.blit(text, textRect)
    ecran.blit(font.render(str(int(volume)), 1, (255, 255, 255)),
               (infoObject.current_w * (86 / 240), infoObject.current_h * (16 / 54)))
    ecran.blit(font.render("Musique", 1, (255, 255, 255)),
               (infoObject.current_w * (2 / 24), infoObject.current_h * (16 / 54)))


    play_button1 = Button(infoObject.current_w * (1 / 2) - 87.5, infoObject.current_h * (49 / 54), logo)
    play_button1_pressed = Button(infoObject.current_w * (1 / 2) - 87.5, infoObject.current_h * (49 / 54), logo_pressed)

    sound_plus_button = Button_option(infoObject.current_w * (100 / 240), infoObject.current_h * (15 / 54),
                                      reduce_logo_plus)
    sound_plus_button_pressed = Button_option(infoObject.current_w * (100 / 240), infoObject.current_h * (15 / 54),
                                              reduce_logo_plus_pressed)
    sound_minus_button = Button_option(infoObject.current_w * (70 / 240), infoObject.current_h * (15 / 54),
                                       reduce_logo_minus)
    sound_minus_button_pressed = Button_option(infoObject.current_w * (70 / 240), infoObject.current_h * (15 / 54),
                                               reduce_logo_minus_pressed)



    while running:

        if sound_plus_button.draw(""):
            button_sound.play()
            sound_plus_button_pressed.draw("")
            if volume < 100:
                volume += 1
                mixer.music.set_volume(volume / 100)
                button_sound.set_volume(volume / 100)
                pygame.draw.rect(ecran, (255, 125, 0),
                                 pygame.Rect(infoObject.current_w * (86 / 240), infoObject.current_h * (16 / 54), 75,
                                             70))
                ecran.blit(font.render(str(int(volume)), 1, (255, 255, 255)),
                           (infoObject.current_w * (86 / 240), infoObject.current_h * (16 / 54)))

        if sound_minus_button.draw(""):
            button_sound.play()
            sound_minus_button_pressed.draw("")
            if volume > 0:
                volume -= 1
                mixer.music.set_volume(volume / 100)
                button_sound.set_volume(volume / 100)
                pygame.draw.rect(ecran, (255, 125, 0),
                                 pygame.Rect(infoObject.current_w * (86 / 240), infoObject.current_h * (16 / 54), 75,
                                             70))
                ecran.blit(font.render(str(int(volume)), 1, (255, 255, 255)),
                           (infoObject.current_w * (86 / 240), infoObject.current_h * (16 / 54)))

        if play_button1.draw("  Quitter"):
            button_sound.play()
            play_button1_pressed.draw("  Quitter")
            running = False


        for event in pygame.event.get():
            if event.type == QUIT:
                with open('savegame.txt','w') as score_file:
                    json.dump(data,score_file)
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        ticker.tick(20)
    volume /= 100
    return volume


def game(volume,d_intro):
    nuit = True
    c_nuit = 0
    background = [pygame.transform.scale(pygame.image.load("Assets/Map/map ile paradisiaque.png"), (infoObject.current_w, infoObject.current_h)).convert_alpha(), pygame.transform.scale(pygame.image.load("Assets/Map/map ile paradisiaque_nuit.png"), (infoObject.current_w, infoObject.current_h)).convert_alpha()]
    tuto_image = [pygame.image.load("Assets/Main/tuto fox fishing.png"),pygame.image.load("Assets/Main/tuto fox fishing 2.png"),pygame.image.load("Assets/Main/tuto fox fishing 3.png")]
    anim = 0
    p_count = 0
    f_count = 0
    movex = 0
    movey = 220
    flip = 0
    moving_right = False
    moving_left = False
    echap = False
    magasin = False
    aides = False
    run = True
    font2 = pygame.font.Font("Minecraft.ttf", 20)

    prix_canne_1, prix_canne_2, prix_canne_3, prix_canne_4 = 100, 250, 500, 1000
    cane_buy_1, cane_buy_2, cane_buy_3, cane_buy_4 = False, False, False, False
    Hookx = movex + 151
    Hooky = movey + 37


    time = 0
    shoot = False
    power = 0
    angle = 0
    poissonattrape = False
    moving = False
    launch = True
    battle_ship = False
    a=1
    b=1


    def playy(charac,flip, right, left):
        if right == False and left == False and flip == 0:
            if charac == 2:
                ecran.blit(Player[charac][p_count], (movex, movey-66))
            else:
                ecran.blit(Player[charac][p_count], (movex, movey))
        elif right == True and left == False and flip == 0:
            if charac == 2:
                ecran.blit(Player[charac][p_count], (movex, movey - 66))
            else:
                ecran.blit(Player[charac][p_count], (movex, movey))
        elif right == False and left == True and flip == 1:
            if charac == 2:
                ecran.blit(pygame.transform.flip(Player[charac][p_count], True, False), (movex, movey-66))
            else:
                ecran.blit(pygame.transform.flip(Player[charac][p_count], True, False), (movex, movey))

        elif right == False and left == False and flip == 1:
            if charac == 2:
                ecran.blit(pygame.transform.flip(Player[charac][p_count], True, False), (movex, movey - 66))
            else:
                ecran.blit(pygame.transform.flip(Player[charac][p_count], True, False), (movex, movey))

    def findAngle(pos):
        sX = Hookx
        sY = Hooky
        try:
            angle = math.atan((sY - pos[1]) / (sX - pos[0]))
        except:
            angle = math.pi / 2

        if pos[1] < sY and pos[0] > sX:
            angle = abs(angle)
        elif pos[1] < sY and pos[0] < sX:
            angle = math.pi - angle
        elif pos[1] > sY and pos[0] < sX:
            angle = math.pi + abs(angle)
        elif pos[1] > sY and pos[0] > sX:
            angle = (math.pi * 2) - angle

        return angle



    def ballPath(startx, starty, power, ang, time):
        angle = ang
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        distX = velx * time
        distY = (vely * time) + ((-4.9 * (time ** 2)) / 2)

        newx = round(distX + startx)
        newy = round(starty - distY)

        return newx, newy

    def hookcomeback(Hookx,Hooky,movex,movey):

        if Hookx > movex+100:
            if Hookx / movex < 0.02:
                Hookx -= (Hookx / movex) * 0.01
            elif Hookx / movex < 0.01:
                Hookx -= (Hookx / movex) * 0.001
            else:
                Hookx -= (Hookx / movex) * 0.02

        elif Hookx < movex+50:

            if movex / Hookx < 0.02:
                Hookx += (movex / Hookx)*0.03
            else:
                Hookx +=(movex / Hookx)*0.1

        if Hooky > movey + 99:
            Hooky -= (Hooky / movey)*0.02


        return Hookx, Hooky

    def spawn_fishs(num,enemies):
        enemies.clear()
        enemies = []
        for i in range(num):
            enemies.append(Fishs(random.randint(100, infoObject.current_w - 25), random.randint(500, infoObject.current_h - 100)))
        return enemies





    enemies = []
    splashs = []





    while run:


        ecran.blit(background[c_nuit], (0, 0))

        if nuit == True:
            enemies = spawn_fishs(50,enemies)
            nuit = False
        line = [(Hookx, Hooky), (movex + 160, movey + 40)]
        pygame.draw.line(ecran, (255, 255, 255), line[0], line[1], 3)

        for e in enemies:
            e.move()
            e.spawn()
            if e.x > infoObject.current_w - 15 or e.x < -100:
                e.direction *= -1
                e.y += random.randrange(-60, 60, 10)
                e.bool = not e.bool

            if e.y > infoObject.current_h:

                e.y -= 100
            elif e.y < 410:
                e.y += 100

            poissonattrape,shoot = e.catch(Hookx, Hooky, poissonattrape, shoot,data['magic_hook'],data['charac'])
            Hookx, Hooky, poissonattrape, shoot, time, moving = e.hookreturn(Hookx, Hooky, shoot, time, poissonattrape, movex,movey,moving)
            data['money'], data['score'] = e.sold(data['money'], data['score'],data['charac'])


            if poissonattrape == True and data['magic_hook'] == 1:

                text = font2.render("Appuyez sur E pour tirer le poisson", 0.8, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (infoObject.current_w // 2, infoObject.current_h * (1 / 4))
                ecran.blit(text, (movex-70,movey+260))


            if moving == True:
                Hookx,Hooky = hookcomeback(Hookx, Hooky, movex, movey)


        if infoObject.current_h-80 >= Hooky > movey + 200 and shoot != False:
            splashs.append([[Hookx, Hooky], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])
            if launch==True:
                hook_sound.play()
            launch = False
            time -= 0.03

            for splash in splashs:
                splash[0][0] += splash[1][0]
                splash[0][1] += splash[1][1]
                splash[2] -= 0.1
                splash[1][1] += 0.1
                pygame.draw.circle(ecran, (173, 216, 240), [int(splash[0][0]), int(splash[0][1])], int(splash[2]))

                if splash[2] < 0:
                    splashs.remove(splash)
        else:
            launch = True
            splashs.clear()

        playy(data['charac'],flip, False, False)
        f_count += 0.2
        if f_count > 1:
            p_count += 1
            f_count = 0
            anim += 1
        if p_count > 3:
            p_count = 0
        if anim > 1:
            anim = 0
        ecran.blit(Hook[data['magic_hook']], (Hookx, Hooky))

        if shoot:
            if Hooky < infoObject.current_h - 50:

                time += 0.1
                po = ballPath(x, y, power, angle, time)
                Hookx = po[0]
                Hooky = po[1]
            else:

                shoot = False
                time = False
                Hooky = Hooky - 5

        scoreText = font.render(str(data['score']) + " pts ", True, (255, 255, 255))
        scrRect = scoreText.get_rect()
        scrRect.center = (infoObject.current_w * 1 - 105, infoObject.current_h * (1.6 / 54))
        ecran.blit(scoreText, scrRect)

        argentText = font.render(str(data['money']) + " $ ", True, (255, 255, 255))
        argentRect = argentText.get_rect()
        argentRect.center = (infoObject.current_w * 1 - 80, infoObject.current_h * (4.5 / 54))
        ecran.blit(argentText, argentRect)

        pause = Button(infoObject.current_w * (0.1 / 15), infoObject.current_h * (0.1 / 10), logo_pause)
        pause_pressed = Button(infoObject.current_w * (0.1 / 15), infoObject.current_h * (0.1 / 10), logo_pause_pressed)

        shop = Button(infoObject.current_w * (0.7 / 15), infoObject.current_h * (0.1 / 10), logo_dollar)
        shop_pressed = Button(infoObject.current_w * (0.7 / 15), infoObject.current_h * (0.1 / 10), logo_dollar_pressed)

        helps = Button(infoObject.current_w * (1.3 / 15), infoObject.current_h * (0.1 / 10), logo_interrogation)
        helps_pressed = Button(infoObject.current_w * (1.3 / 15), infoObject.current_h * (0.1 / 10),
                               logo_interrogation_pressed)

        night = Button(infoObject.current_w * (1.9 / 15), infoObject.current_h * (0.1 / 10), logo_night)

        day = Button(infoObject.current_w * (2.5 / 15), infoObject.current_h * (0.1 / 10), logo_sun)




        if pause.draw("") and d_intro == 0:
            button_sound.play()
            pause_pressed.draw("")
            echap = True
        if shop.draw("") and d_intro == 0:
            button_sound.play()
            shop_pressed.draw("")
            magasin = True
        if helps.draw("") and d_intro == 0:
            button_sound.play()
            helps_pressed.draw("")
            aides = True

        if night.draw("") and d_intro == 0:
            button_sound.play()
            if c_nuit == 0 :
                nuit = True
                c_nuit = 1
                loading_g(volume)
                Hookx = movex + 151
                Hooky = movey + 37
                shoot = False
                time = False
        if day.draw("") and d_intro == 0:
            button_sound.play()
            if c_nuit == 1 :
                nuit = True
                c_nuit = 0
                loading_g(volume)
                Hookx = movex + 151
                Hooky = movey + 37
                shoot = False
                time = False


        for event in pygame.event.get():
            if event.type == QUIT:
                with open('savegame.txt','w') as score_file:
                    json.dump(data,score_file)
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and d_intro == 0 :
                if event.key == pygame.K_RIGHT:
                    flip = 0
                    moving_right = True
                elif event.key == pygame.K_LEFT:
                    flip = 1
                    moving_left = True
                elif event.key == K_ESCAPE:
                    if echap and d_intro == 0:
                        echap = False
                    else:
                        if magasin and d_intro == 0:
                            magasin = False
                        else:
                            echap = True
                elif event.key == K_m:
                    if magasin and d_intro == 0:
                        magasin = False
                    else:
                        if echap and d_intro == 0:
                            magasin = False
                        else:
                            magasin = True
                elif event.key == K_e and poissonattrape == True and data['magic_hook'] == 1:
                    moving = True
                elif event.key == K_SPACE:
                    data['money'] = 1000
            if event.type == pygame.MOUSEBUTTONDOWN and echap == False and magasin == False and aides == False and d_intro == 0 and (poissonattrape == False  or data['magic_hook'] == 0 ) :

                if not shoot:
                    shoot = True
                    x = Hookx
                    y = Hooky
                    pos = pygame.mouse.get_pos()
                    power = math.sqrt((line[1][1] - line[0][1]) ** 2 + (line[1][0] - line[0][1]) ** 2) / 8
                    angle = findAngle(pos)


            elif event.type == KEYUP:
                moving_right = False
                moving_left = False

        if moving_right:
            playy(data['charac'],flip, True, False)
            movex += 5
            if poissonattrape == False:
                Hookx += 5
        if moving_left:
            playy(data['charac'],flip, False, True)
            movex -= 5
            if poissonattrape == False:
                Hookx -= 5

        if movex < 10:
            movex = 10
        elif movex > infoObject.current_w - 220:
            movex = infoObject.current_w - 220

        if Hookx < 10:
            Hookx = 10
        elif Hookx > infoObject.current_w - 10:
            Hookx = infoObject.current_w - 10

        if Hooky < 0:
            Hooky = 0

        if d_intro == 1:

            draw_rect_alpha(ecran, (50, 50, 50, 180), (0, 0, infoObject.current_w, infoObject.current_h))
            ecran.blit(tuto_image[0],(infoObject.current_w/10,infoObject.current_h/4))
            quit_button = Button(infoObject.current_w * (41 / 53), infoObject.current_h * (42 / 53), logo)
            quit_button_pressed = Button(infoObject.current_w * (41 / 53), infoObject.current_h * (42 / 53),
                                         logo_pressed)
            if quit_button.draw("  Allez !"):
                button_sound.play()
                quit_button_pressed.draw("  Allez !")
                d_intro = 0
            pygame.display.update()

        if echap:
            Hookx = movex + 151
            Hooky = movey + 37
            shoot = False
            time = False
            draw_rect_alpha(ecran, (50, 50, 50, 180), (0, 0, infoObject.current_w, infoObject.current_h))
            draw_rect_alpha(ecran, (180, 100, 0, 255), (0, 0, infoObject.current_w // 3, infoObject.current_h))
            draw_rect_alpha(ecran, (230, 125, 0, 200),
                            (5, 5, infoObject.current_w // 3 - 10, infoObject.current_h - 10))

            text = font.render("Menu", 1, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (infoObject.current_w // 6, infoObject.current_h * (1 / 10))
            ecran.blit(text, textRect)

            resume_button = Button(infoObject.current_w // 8, infoObject.current_h * (3 / 10), logo)
            options_button = Button(infoObject.current_w // 8, infoObject.current_h * (5 / 10), logo)
            quit_button = Button(infoObject.current_w // 8, infoObject.current_h * (7.5 / 10), logo)

            resume_button_pressed = Button(infoObject.current_w // 8, infoObject.current_h * (3 / 10), logo_pressed)
            options_button_pressed = Button(infoObject.current_w // 8, infoObject.current_h * (5 / 10), logo_pressed)
            quit_button_pressed = Button(infoObject.current_w // 8, infoObject.current_h * (7.5 / 10), logo_pressed)

            if resume_button.draw("Continuer"):
                button_sound.play()
                resume_button_pressed.draw("Continuer")
                echap = False

            if options_button.draw(" Options"):
                button_sound.play()
                options_button_pressed.draw(" Options")
                volume2 = options(volume)
                volume = volume2

            if quit_button.draw(" Quitter"):
                button_sound.play()
                quit_button_pressed.draw(" Quitter")
                with open('savegame.txt','w') as score_file:
                    json.dump(data,score_file)
                sys.exit()
        if magasin:
            Hookx = movex + 151
            Hooky = movey + 37
            shoot = False
            time = False
            draw_rect_alpha(ecran, (50, 50, 50, 180), (0, 0, infoObject.current_w, infoObject.current_h))
            draw_rect_alpha(ecran, (180, 100, 0, 255),
                            (infoObject.current_w * (3 / 53) - 10, infoObject.current_h * (3 / 53) - 10,
                             infoObject.current_w - infoObject.current_w * (6 / 53) + 20,
                             infoObject.current_h - infoObject.current_h * (6 / 53) + 20))
            draw_rect_alpha(ecran, (230, 125, 0, 200),
                            (infoObject.current_w * (3 / 53), infoObject.current_h * (3 / 53),
                             infoObject.current_w - infoObject.current_w * (6 / 53),
                             infoObject.current_h - infoObject.current_h * (6 / 53)))

            quit_button = Button(infoObject.current_w * (42 / 53), infoObject.current_h * (43 / 53), logo)
            quit_button_pressed = Button(infoObject.current_w * (42 / 53), infoObject.current_h * (43 / 53),
                                         logo_pressed)

            if quit_button.draw("  Sortir"):
                button_sound.play()
                quit_button_pressed.draw("  Sortir")
                magasin = False

            caneText = font.render("Cannes à Pêche :", 1, (255, 255, 255))
            caneRect = caneText.get_rect()
            caneRect.center = (infoObject.current_w // 5, infoObject.current_h * (7 / 53))
            ecran.blit(caneText, caneRect)

            cane1 = Button(infoObject.current_w * (8 / 50), infoObject.current_h * (10 / 50), shop_cane)
            cane2 = Button(infoObject.current_w * (16 / 50), infoObject.current_h * (10 / 50), shop_cane_2)
            cane3 = Button(infoObject.current_w * (24 / 50), infoObject.current_h * (10 / 50), shop_cane_3)
            cane4 = Button(infoObject.current_w * (32 / 50), infoObject.current_h * (10 / 50), shop_cane_4)
            magic_h = Button(infoObject.current_w * (8 / 50), infoObject.current_h * (25 / 50), Hook_store)
            ship2 = Button(infoObject.current_w * (16 / 50), infoObject.current_h * (25 / 50), pirate_flag)

            bs1 = Button(infoObject.current_w * (8 / 50) - 2, infoObject.current_h * (10 / 50) - 2, black_square)
            bs1.draw("")


            prix1Text = font.render(str(prix_canne_1) + "$", True, (255, 255, 255))
            prix1Rect = prix1Text.get_rect()
            prix1Rect.center = (infoObject.current_w * (8 / 50) + 125, infoObject.current_h * (10 / 50) + 280)
            ecran.blit(prix1Text, prix1Rect)

            bs2 = Button(infoObject.current_w * (16 / 50) - 2, infoObject.current_h * (10 / 50) - 2, black_square)
            bs2.draw("")
            prix2Text = font.render(str(prix_canne_2) + "$", True, (255, 255, 255))
            prix2Rect = prix2Text.get_rect()
            prix2Rect.center = (infoObject.current_w * (16 / 50) + 125, infoObject.current_h * (10 / 50) + 280)
            ecran.blit(prix2Text, prix2Rect)

            bs3 = Button(infoObject.current_w * (24 / 50) - 2, infoObject.current_h * (10 / 50) - 2, black_square)
            bs3.draw("")
            prix3Text = font.render(str(prix_canne_3) + "$", True, (255, 255, 255))
            prix3Rect = prix3Text.get_rect()
            prix3Rect.center = (infoObject.current_w * (24 / 50) + 125, infoObject.current_h * (10 / 50) + 280)
            ecran.blit(prix3Text, prix3Rect)

            bs4 = Button(infoObject.current_w * (32 / 50) - 2, infoObject.current_h * (10 / 50) - 2, black_square)
            bs4.draw("")
            prix4Text = font.render(str(prix_canne_4) + "$", True, (255, 255, 255))
            prix4Rect = prix4Text.get_rect()
            prix4Rect.center = (infoObject.current_w * (32 / 50) + 125, infoObject.current_h * (10 / 50) + 280)
            ecran.blit(prix4Text, prix4Rect)

            bs5 = Button(infoObject.current_w * (8 / 50) - 2, infoObject.current_h * (25 / 50) - 2, black_square)
            bs5.draw("")
            prix5Text = font.render("Free", True, (255, 255, 255))
            prix5Rect = prix5Text.get_rect()
            prix5Rect.center = (infoObject.current_w * (8 / 50) + 125, infoObject.current_h * (25 / 50) + 280)
            ecran.blit(prix5Text, prix5Rect)

            bs6 = Button(infoObject.current_w * (16/ 50) - 2, infoObject.current_h * (25 / 50) - 2, black_square)
            bs6.draw("")
            prix6Text = font.render("100 $", True, (255, 255, 255))
            prix6Rect = prix6Text.get_rect()
            prix6Rect.center = (infoObject.current_w * (16 / 50) + 125, infoObject.current_h * (25 / 50) + 280)
            ecran.blit(prix6Text, prix6Rect)

            if cane1.draw(""):
                if data['money'] >= 100 and not cane_buy_1:
                    data['money'] -= 100
                    cane_buy_1 = True
                    cash_sound.play()
                    data['charac'] = 1

            if cane2.draw("") and not cane_buy_2:
                if data['money'] >= 250:
                    data['money'] -= 250
                    cane_buy_2 = True
                    cash_sound.play()

            if cane3.draw("") and not cane_buy_3:
                if data['money'] >= 500:
                    data['money'] -= 500
                    cane_buy_3 = True
                    cash_sound.play()

            if cane4.draw("") and not cane_buy_4:
                if data['money'] >= 1000:
                    data['money'] -= 1000
                    cane_buy_4 = True
                    cash_sound.play()

            if magic_h.draw(""):
                if data['money'] >= 0 and not data['magic_hook']:
                    data['money'] -= 0
                    data['magic_hook'] = 1
                    cash_sound.play()

            if ship2.draw(""):
                if data['money'] >= 100 and not battle_ship:
                    data['money'] -= 100
                    battle_ship = True
                    cash_sound.play()
                    data['charac'] = 2


            text = font.render("Magasin", 1, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (infoObject.current_w // 2, infoObject.current_h * (3 / 53))
            ecran.blit(text, textRect)

            argentText = font.render(str(data['money']) + " $", True, (255, 255, 255))
            argentRect = argentText.get_rect()
            argentRect.center = (
                infoObject.current_w - infoObject.current_w * (6 / 53) - 25, infoObject.current_h * (5 / 53))
            ecran.blit(argentText, argentRect)

        if aides:
            Hookx = movex + 151
            Hooky = movey + 37
            shoot = False
            time = False
            font2 = pygame.font.Font("Minecraft.ttf", 20)
            draw_rect_alpha(ecran, (50, 50, 50, 180), (0, 0, infoObject.current_w, infoObject.current_h))
            draw_rect_alpha(ecran, (180, 100, 0, 255),
                            (infoObject.current_w * (3 / 53) - 10, infoObject.current_h * (3 / 53) - 10,
                             infoObject.current_w - infoObject.current_w * (6 / 53) + 20,
                             infoObject.current_h - infoObject.current_h * (6 / 53) + 20))
            draw_rect_alpha(ecran, (230, 125, 0, 200),
                            (infoObject.current_w * (3 / 53), infoObject.current_h * (3 / 53),
                             infoObject.current_w - infoObject.current_w * (6 / 53),
                             infoObject.current_h - infoObject.current_h * (6 / 53)))

            quit_button = Button(infoObject.current_w * (42 / 53), infoObject.current_h * (43 / 53), logo)
            quit_button_pressed = Button(infoObject.current_w * (42 / 53), infoObject.current_h * (43 / 53),
                                         logo_pressed)

            if quit_button.draw("  Sortir"):
                button_sound.play()
                quit_button_pressed.draw("  Sortir")
                aides = False

            text = font.render("AIDE", 1, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (infoObject.current_w // 2, infoObject.current_h * (3 / 53))
            ecran.blit(text, textRect)

            text1 = font2.render("-Pour lancer l’hameçon, utilisez votre souris pour cliquer à l’endroit souhaité." , 1, (255, 255, 255))
            text2 = font2.render("Si votre hameçon ne touche aucun poisson, pas de panique, il vous suffit juste de recliquer à l’endroit", 1,(255, 255, 255))
            text3 = font2.render("souhaité avec votre souris quand il cessera de bouger mais attention, cela n’est pas si facile.",1,(255, 255, 255))
            text4 = font2.render("-Vous avez attrapé un poisson ? Bien joué ! Maintenant il vous suffit de cliquer avec votre souris au ",1,(255, 255, 255))
            text5 = font2.render("niveau du bateau pour que l’hameçon et le poisson puisse remonter et toucher votre bateau et ainsi être  ",1,(255, 255, 255))
            text6 = font2.render("vendu. N’hésitez pas à bouger votre bateau en même temps pour faciliter la capture.",1,(255, 255, 255))
            text7 = font2.render("-Vous avez capturé tous les poissons de la zone ? Pas de panique, ils reviendront la nuit donc faites une petite ",1, (255, 255, 255))
            text8 = font2.render("sieste et ils reviendront. N’hésitez pas à faire un tour dans le magasin en appuyant sur ‘’M’’ pour améliorer votre look. ",1, (255, 255, 255))
            textRect1 = text1.get_rect()
            textRect2 = text2.get_rect()
            textRect3 = text3.get_rect()
            textRect4 = text4.get_rect()
            textRect5 = text5.get_rect()
            textRect6 = text6.get_rect()
            textRect7 = text7.get_rect()
            textRect8 = text8.get_rect()
            textRect1.center = (infoObject.current_w // 2, infoObject.current_h * (12 / 53))
            textRect2.center = (infoObject.current_w // 2, infoObject.current_h * (15 / 53))
            textRect3.center = (infoObject.current_w // 2, infoObject.current_h * (18 / 53))
            textRect4.center = (infoObject.current_w // 2, infoObject.current_h * (21 / 53))
            textRect5.center = (infoObject.current_w // 2, infoObject.current_h * (24 / 53))
            textRect6.center = (infoObject.current_w // 2, infoObject.current_h * (27 / 53))
            textRect7.center = (infoObject.current_w // 2, infoObject.current_h * (30 / 53))
            textRect8.center = (infoObject.current_w // 2, infoObject.current_h * (33 / 53))
            ecran.blit(text1, textRect1)
            ecran.blit(text2, textRect2)
            ecran.blit(text3, textRect3)
            ecran.blit(text4, textRect4)
            ecran.blit(text5, textRect5)
            ecran.blit(text6, textRect6)
            ecran.blit(text7, textRect7)
            ecran.blit(text8, textRect8)


        clock.tick(60)
        pygame.display.update()


def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)


def loading(volume):
    running = True
    angle = 0
    count = 0
    clock = 0
    important = 0
    time = 15
    mixer.music.set_volume(0)
    intro = pygame.image.load("histoire du jeu.png")
    while running:
        ecran.fill((0, 0, 0))
        if d_intro == 1:
            ecran.blit(intro, (500, 200))
            time = 35
        angle += 1
        clock += 0.05
        important += 0.05
        if clock > 1:
            count += 1
            clock = 0
        msg_loading = ["Loading", "Loading.", "Loading..", "Loading..."]
        rota_rena = pygame.transform.rotate(renard_loading, angle)
        new_rect = rota_rena.get_rect(center=renard_loading.get_rect(
            topleft=(infoObject.current_w * (8 / 9) + 50, infoObject.current_h * (8 / 9))).center)
        ecran.blit(rota_rena, new_rect)
        font = pygame.font.Font("Minecraft.ttf", 25)
        if count > len(msg_loading) - 1:
            count = 0
        text = font.render(msg_loading[count], 1, (255, 255, 255))

        ecran.blit(text, (infoObject.current_w * (8 / 9) + 25, infoObject.current_h * (8 / 9) + 50))

        pygame.display.update()
        ticker.tick(60)
        if important > time:

            running = False
            mixer.music.set_volume(volume)
            mixer.music.play(-1)
            game(volume,d_intro)


def loading_g(volume):
    running = True
    angle = 0
    count = 0
    clock = 0
    important = 0

    mixer.music.set_volume(0)
    while running:
        ecran.fill((0, 0, 0))
        angle += 1
        clock += 0.05
        important += 0.05
        if clock > 1:
            count += 1
            clock = 0
        msg_loading = ["Loading", "Loading.", "Loading..", "Loading..."]
        rota_rena = pygame.transform.rotate(renard_loading, angle)
        new_rect = rota_rena.get_rect(center=renard_loading.get_rect(
            topleft=(infoObject.current_w * (8 / 9) + 50, infoObject.current_h * (8 / 9))).center)
        ecran.blit(rota_rena, new_rect)
        font = pygame.font.Font("Minecraft.ttf", 25)
        if count > len(msg_loading) - 1:
            count = 0
        text = font.render(msg_loading[count], 1, (255, 255, 255))

        ecran.blit(text, (infoObject.current_w * (8 / 9) + 25, infoObject.current_h * (8 / 9) + 50))

        pygame.display.update()
        ticker.tick(60)
        if important > 4:
            running = False
            mixer.music.set_volume(volume)
            mixer.music.play(-1)

main_menu(volume)
