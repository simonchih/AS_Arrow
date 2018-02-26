import random, os
import time 
import pygame
import math
from pygame.locals import *
from sys import exit

s_capture = 'Sound/MOVE2.WAV'
s_win     = 'Sound/WIN.WAV'

background_image_filename = 'Image/Nostalgy.gif'
game_over_filename = 'Image/game_over.gif'
new_game_filename = 'Image/New_Game_logo.gif'
on_path  = 'Image/on.gif'
off_path = 'Image/off.gif'
win_path = 'Image/win.gif'
add_path = 'Image/add.gif'
sub_path = 'Image/sub.gif'
iP_1c = 'Image/01c.gif'
iP_1d = 'Image/01d.gif'
iP_1h = 'Image/01h.gif'
iP_1s = 'Image/01s.gif'
iP_2c = 'Image/02c.gif'
iP_2d = 'Image/02d.gif'
iP_2h = 'Image/02h.gif'
iP_2s = 'Image/02s.gif'
iP_3c = 'Image/03c.gif'
iP_3d = 'Image/03d.gif'
iP_3h = 'Image/03h.gif'
iP_3s = 'Image/03s.gif'
iP_4c = 'Image/04c.gif'
iP_4d = 'Image/04d.gif'
iP_4h = 'Image/04h.gif'
iP_4s = 'Image/04s.gif'
iP_5c = 'Image/05c.gif'
iP_5d = 'Image/05d.gif'
iP_5h = 'Image/05h.gif'
iP_5s = 'Image/05s.gif'
iP_6c = 'Image/06c.gif'
iP_6d = 'Image/06d.gif'
iP_6h = 'Image/06h.gif'
iP_6s = 'Image/06s.gif'
iP_7c = 'Image/07c.gif'
iP_7d = 'Image/07d.gif'
iP_7h = 'Image/07h.gif'
iP_7s = 'Image/07s.gif'
iP_8c = 'Image/08c.gif'
iP_8d = 'Image/08d.gif'
iP_8h = 'Image/08h.gif'
iP_8s = 'Image/08s.gif'
iP_9c = 'Image/09c.gif'
iP_9d = 'Image/09d.gif'
iP_9h = 'Image/09h.gif'
iP_9s = 'Image/09s.gif'
iP_10c = 'Image/10c.gif'
iP_10d = 'Image/10d.gif'
iP_10h = 'Image/10h.gif'
iP_10s = 'Image/10s.gif'
iP_11c = 'Image/11c.gif'
iP_11d = 'Image/11d.gif'
iP_11h = 'Image/11h.gif'
iP_11s = 'Image/11s.gif'
iP_12c = 'Image/12c.gif'
iP_12d = 'Image/12d.gif'
iP_12h = 'Image/12h.gif'
iP_12s = 'Image/12s.gif'
iP_13c = 'Image/13c.gif'
iP_13d = 'Image/13d.gif'
iP_13h = 'Image/13h.gif'
iP_13s = 'Image/13s.gif'

SCREEN_SIZE = (1280, 720) 
pygame.init()

pygame.display.set_icon(pygame.image.load("Image/as_arrow.png"))
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)#SCREEN_SIZE, FULLSCREEN, 32)
pygame.display.set_caption("AS Arrow")

capture_sound = pygame.mixer.Sound(s_capture)
win_sound     = pygame.mixer.Sound(s_win)

background = pygame.image.load(background_image_filename).convert()
game_over_image = pygame.image.load(game_over_filename).convert()
new_game_image = pygame.image.load(new_game_filename).convert()
on_image = pygame.image.load(on_path).convert()
off_image = pygame.image.load(off_path).convert()
win_image = pygame.image.load(win_path).convert()
add_image = pygame.image.load(add_path).convert()
sub_image = pygame.image.load(sub_path).convert()
P1c = pygame.image.load(iP_1c).convert()
P1d = pygame.image.load(iP_1d).convert()
P1h = pygame.image.load(iP_1h).convert()
P1s = pygame.image.load(iP_1s).convert()
P2c = pygame.image.load(iP_2c).convert()
P2d = pygame.image.load(iP_2d).convert()
P2h = pygame.image.load(iP_2h).convert()
P2s = pygame.image.load(iP_2s).convert()
P3c = pygame.image.load(iP_3c).convert()
P3d = pygame.image.load(iP_3d).convert()
P3h = pygame.image.load(iP_3h).convert()
P3s = pygame.image.load(iP_3s).convert()
P4c = pygame.image.load(iP_4c).convert()
P4d = pygame.image.load(iP_4d).convert()
P4h = pygame.image.load(iP_4h).convert()
P4s = pygame.image.load(iP_4s).convert()
P5c = pygame.image.load(iP_5c).convert()
P5d = pygame.image.load(iP_5d).convert()
P5h = pygame.image.load(iP_5h).convert()
P5s = pygame.image.load(iP_5s).convert()
P6c = pygame.image.load(iP_6c).convert()
P6d = pygame.image.load(iP_6d).convert()
P6h = pygame.image.load(iP_6h).convert()
P6s = pygame.image.load(iP_6s).convert()
P7c = pygame.image.load(iP_7c).convert()
P7d = pygame.image.load(iP_7d).convert()
P7h = pygame.image.load(iP_7h).convert()
P7s = pygame.image.load(iP_7s).convert()
P8c = pygame.image.load(iP_8c).convert()
P8d = pygame.image.load(iP_8d).convert()
P8h = pygame.image.load(iP_8h).convert()
P8s = pygame.image.load(iP_8s).convert()
P9c = pygame.image.load(iP_9c).convert()
P9d = pygame.image.load(iP_9d).convert()
P9h = pygame.image.load(iP_9h).convert()
P9s = pygame.image.load(iP_9s).convert()
P10c = pygame.image.load(iP_10c).convert()
P10d = pygame.image.load(iP_10d).convert()
P10h = pygame.image.load(iP_10h).convert()
P10s = pygame.image.load(iP_10s).convert()
P11c = pygame.image.load(iP_11c).convert()
P11d = pygame.image.load(iP_11d).convert()
P11h = pygame.image.load(iP_11h).convert()
P11s = pygame.image.load(iP_11s).convert() 
P12c = pygame.image.load(iP_12c).convert()
P12d = pygame.image.load(iP_12d).convert()
P12h = pygame.image.load(iP_12h).convert()
P12s = pygame.image.load(iP_12s).convert() 
P13c = pygame.image.load(iP_13c).convert()
P13d = pygame.image.load(iP_13d).convert()
P13h = pygame.image.load(iP_13h).convert()
P13s = pygame.image.load(iP_13s).convert() 

P_1c = pygame.transform.rotate(P1c , -90)
P_1d = pygame.transform.rotate(P1d , -90)
P_1h = pygame.transform.rotate(P1h , -90)
P_1s = pygame.transform.rotate(P1s , -90)
P_2c = pygame.transform.rotate(P2c , -90)
P_2d = pygame.transform.rotate(P2d , -90)
P_2h = pygame.transform.rotate(P2h , -90)
P_2s = pygame.transform.rotate(P2s , -90)
P_3c = pygame.transform.rotate(P3c , -90)
P_3d = pygame.transform.rotate(P3d , -90)
P_3h = pygame.transform.rotate(P3h , -90)
P_3s = pygame.transform.rotate(P3s , -90)
P_4c = pygame.transform.rotate(P4c , -90)
P_4d = pygame.transform.rotate(P4d , -90)
P_4h = pygame.transform.rotate(P4h , -90)
P_4s = pygame.transform.rotate(P4s , -90)
P_5c = pygame.transform.rotate(P5c , -90)
P_5d = pygame.transform.rotate(P5d , -90)
P_5h = pygame.transform.rotate(P5h , -90)
P_5s = pygame.transform.rotate(P5s , -90)
P_6c = pygame.transform.rotate(P6c , -90)
P_6d = pygame.transform.rotate(P6d , -90)
P_6h = pygame.transform.rotate(P6h , -90)
P_6s = pygame.transform.rotate(P6s , -90)
P_7c = pygame.transform.rotate(P7c , -90)
P_7d = pygame.transform.rotate(P7d , -90)
P_7h = pygame.transform.rotate(P7h , -90)
P_7s = pygame.transform.rotate(P7s , -90)
P_8c = pygame.transform.rotate(P8c , -90)
P_8d = pygame.transform.rotate(P8d , -90)
P_8h = pygame.transform.rotate(P8h , -90)
P_8s = pygame.transform.rotate(P8s , -90)
P_9c = pygame.transform.rotate(P9c , -90)
P_9d = pygame.transform.rotate(P9d , -90)
P_9h = pygame.transform.rotate(P9h , -90)
P_9s = pygame.transform.rotate(P9s , -90)
P_10c= pygame.transform.rotate(P10c, -90)
P_10d= pygame.transform.rotate(P10d, -90)
P_10h= pygame.transform.rotate(P10h, -90)
P_10s= pygame.transform.rotate(P10s, -90)
P_11c= pygame.transform.rotate(P11c, -90)
P_11d= pygame.transform.rotate(P11d, -90)
P_11h= pygame.transform.rotate(P11h, -90)
P_11s= pygame.transform.rotate(P11s, -90)
P_12c= pygame.transform.rotate(P12c, -90)
P_12d= pygame.transform.rotate(P12d, -90)
P_12h= pygame.transform.rotate(P12h, -90)
P_12s= pygame.transform.rotate(P12s, -90)
P_13c= pygame.transform.rotate(P13c, -90)
P_13d= pygame.transform.rotate(P13d, -90)
P_13h= pygame.transform.rotate(P13h, -90)
P_13s= pygame.transform.rotate(P13s, -90)

max_of_card = 12

screen_width, screen_height = SCREEN_SIZE

#all card 0 to 51, -1 is deleted, last exist_card must -1
# 4 2 1
# 5 3
# 6
exist1_card = [-1] * (max_of_card + 1)
exist2_card = [-1] * (max_of_card + 1)
exist3_card = [-1] * (max_of_card + 1)
exist4_card = [-1] * (max_of_card + 1)
exist5_card = [-1] * (max_of_card + 1)
exist6_card = [-1] * (max_of_card + 1)
all_card    = [x for x in range(52)]
# 0: can't connect card, 1: can connect card, -1: ini
connect_mark = [-1, -1, -1, 1, 1, 1]
connect_xy = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]

card1_position = (screen_width-P_1c.get_width()-1, (screen_height - P_1c.get_height())//2)
card2_position = (screen_width-P_1c.get_width()-P_1c.get_width()//2-1, (screen_height - P_1c.get_height())//2 - 2*P_1c.get_height()//3)
card3_position = (screen_width-P_1c.get_width()-P_1c.get_width()//2-1, (screen_height - P_1c.get_height())//2 + 2*P_1c.get_height()//3)
card4_position = (screen_width-P_1c.get_width()-P_1c.get_width()-1, (screen_height - P_1c.get_height())//2 - 4*P_1c.get_height()//3)
card5_position = (screen_width-P_1c.get_width()-P_1c.get_width()-1, (screen_height - P_1c.get_height())//2)
card6_position =(screen_width-P_1c.get_width()-P_1c.get_width()-1, (screen_height - P_1c.get_height())//2 + 4*P_1c.get_height()//3)

cardp = 0
dock_xy = (50, (screen_height//2 + 3*P_1c.get_height()))
select_card_xy = dock_xy
selected = False
game_over = False
new_game = True
switch_on = 1
win = 0

def display_all_card():
    global selected
    global switch_on

    cor = [0] * 2
    fill_background()
    
    if exist1_card[0] != -1:
        screen.blit(num_to_cards(exist1_card[0]),card1_position)
        if 1 == switch_on and 1 == connect_mark[0]:
            screen.blit(add_image, (card1_position[0]+40, card1_position[1]-24))
        i = 1
        while exist1_card[i] != -1:
            screen.blit(num_to_cards(exist1_card[i]), (card1_position[0]  - i*P_1c.get_width(), card1_position[1]))
            if 1 == switch_on:
                if 1 == i%2:
                    screen.blit(sub_image, (card1_position[0]  - i*P_1c.get_width()+40, card1_position[1]-24))
                else:
                    screen.blit(add_image, (card1_position[0]  - i*P_1c.get_width()+40, card1_position[1]-24))
            i += 1       
        
    if exist2_card[0] != -1:
        screen.blit(num_to_cards(exist2_card[0]),card2_position)
        if 1 == switch_on and 1 == connect_mark[1]:
            screen.blit(add_image, (card2_position[0]+40, card2_position[1]-24))
        i = 1
        while exist2_card[i] != -1:
            screen.blit(num_to_cards(exist2_card[i]), (card2_position[0]  - i*P_1c.get_width(), card2_position[1]))
            if 1 == switch_on:
                if 1 == i%2:
                    screen.blit(sub_image, (card2_position[0]  - i*P_1c.get_width()+40, card2_position[1]-24))
                else:
                    screen.blit(add_image, (card2_position[0]  - i*P_1c.get_width()+40, card2_position[1]-24))
            i += 1
            
    if exist3_card[0] != -1:
        screen.blit(num_to_cards(exist3_card[0]),card3_position)
        if 1 == switch_on and 1 == connect_mark[2]:
            screen.blit(add_image, (card3_position[0]+40, card3_position[1]-24))
        i = 1
        while exist3_card[i] != -1:
            screen.blit(num_to_cards(exist3_card[i]), (card3_position[0]  - i*P_1c.get_width(), card3_position[1]))
            if 1 == switch_on:
                if 1 == i%2:
                    screen.blit(sub_image, (card3_position[0]  - i*P_1c.get_width()+40, card3_position[1]-24))
                else:
                    screen.blit(add_image, (card3_position[0]  - i*P_1c.get_width()+40, card3_position[1]-24))
            i += 1
            
    if exist4_card[0] != -1:
        screen.blit(num_to_cards(exist4_card[0]),card4_position)
        if 1 == switch_on and 1 == connect_mark[3]:
            screen.blit(add_image, (card4_position[0]+40, card4_position[1]-24))
        i = 1
        while exist4_card[i] != -1:
            screen.blit(num_to_cards(exist4_card[i]), (card4_position[0]  - i*P_1c.get_width(), card4_position[1]))
            if 1 == switch_on:
                if 1 == i%2:
                    screen.blit(sub_image, (card4_position[0]  - i*P_1c.get_width()+40, card4_position[1]-24))
                else:
                    screen.blit(add_image, (card4_position[0]  - i*P_1c.get_width()+40, card4_position[1]-24))
            i += 1
            
    if exist5_card[0] != -1:
        screen.blit(num_to_cards(exist5_card[0]),card5_position)
        if 1 == switch_on and 1 == connect_mark[4]:
            screen.blit(add_image, (card5_position[0]+40, card5_position[1]-24))
        i = 1
        while exist5_card[i] != -1:
            screen.blit(num_to_cards(exist5_card[i]), (card5_position[0]  - i*P_1c.get_width(), card5_position[1]))
            if 1 == switch_on:
                if 1 == i%2:
                    screen.blit(sub_image, (card5_position[0]  - i*P_1c.get_width()+40, card5_position[1]-24))
                else:
                    screen.blit(add_image, (card5_position[0]  - i*P_1c.get_width()+40, card5_position[1]-24))
            i += 1
            
    if exist6_card[0] != -1:
        screen.blit(num_to_cards(exist6_card[0]),card6_position)
        if 1 == switch_on and 1 == connect_mark[5]:
            screen.blit(add_image, (card6_position[0]+40, card6_position[1]-24))
        i = 1
        while exist6_card[i] != -1:
            screen.blit(num_to_cards(exist6_card[i]), (card6_position[0]  - i*P_1c.get_width(), card6_position[1]))
            if 1 == switch_on:
                if 1 == i%2:
                    screen.blit(sub_image, (card6_position[0]  - i*P_1c.get_width()+40, card6_position[1]-24))
                else:
                    screen.blit(add_image, (card6_position[0]  - i*P_1c.get_width()+40, card6_position[1]-24))
            i += 1
    
    screen.blit(write("Cheat"),(screen_width -250, screen_height - 150))
    
    if 1 == switch_on:
        screen.blit(on_image, (screen_width - 160, screen_height - 200))
        screen.blit(write("ON", (230,225,121)),(screen_width -50,screen_height - 150))
    else:
        screen.blit(off_image, (screen_width - 160, screen_height - 200))
        screen.blit(write("OFF"),(screen_width -50,screen_height - 150))
    
    screen.blit(new_game_image, ((screen_width - new_game_image.get_width())//2,screen_height - 150))
    
    if True == selected:
        if cardp < 51:
            screen.blit(num_to_cards(all_card[cardp+1]), dock_xy)
            screen.blit(num_to_cards(all_card[cardp]), select_card_xy)
        elif 51 == cardp:
            screen.blit(num_to_cards(all_card[cardp]), select_card_xy)
    elif False == selected and cardp < 52:
        screen.blit(num_to_cards(all_card[cardp]), dock_xy)
        
def num_to_cards(num):
    if 0==num:
        return P_1c
    if 1==num:
        return P_1d
    if 2==num:
        return P_1h
    if 3==num:
        return P_1s
    if 4==num:
       return P_2c
    if 5==num:
       return P_2d
    if 6==num:
       return P_2h
    if 7==num:
       return P_2s
    if 8==num:
       return P_3c
    if 9==num:
       return P_3d 
    if 10==num:
       return P_3h
    if 11==num:
       return P_3s
    if 12==num:
       return P_4c
    if 13==num:
        return P_4d
    if 14==num:
        return P_4h
    if 15==num:
        return P_4s
    if 16==num:
        return P_5c
    if 17==num:
        return P_5d
    if 18==num:
        return P_5h
    if 19==num:
        return P_5s
    if 20==num:
        return P_6c
    if 21==num:
        return P_6d
    if 22==num:
        return P_6h
    if 23==num:
        return P_6s
    if 24==num:
        return P_7c
    if 25==num:
        return P_7d
    if 26==num:
        return P_7h
    if 27==num:
        return P_7s
    if 28==num:
        return P_8c
    if 29==num:
        return P_8d
    if 30==num:
        return P_8h
    if 31==num:
        return P_8s
    if 32==num:
        return P_9c
    if 33==num:
        return P_9d
    if 34==num:
        return P_9h
    if 35==num:
        return P_9s
    if 36==num:
        return P_10c
    if 37==num:
        return P_10d
    if 38==num:
        return P_10h
    if 39==num:
        return P_10s
    if 40==num:
        return P_11c
    if 41==num:
        return P_11d
    if 42==num:
        return P_11h
    if 43==num:
        return P_11s
    if 44==num:
        return P_12c
    if 45==num:
        return P_12d
    if 46==num:
        return P_12h
    if 47==num:
        return P_12s
    if 48==num:
        return P_13c
    if 49==num:
        return P_13d
    if 50==num:
        return P_13h
    if 51==num:
        return P_13s


def write(msg="pygame is cool", color= (0,0,0)):    
    myfont = pygame.font.Font("FreeSansBold.ttf",24)
    mytext = myfont.render(msg, True, color)
    mytext = mytext.convert_alpha()
    return mytext        

def fill_background():
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))

def assign_card():
    global all_card
    global cardp
    
    cardp += 1
    
    if cardp > 52:
        game_over = True
    else:
        return all_card[cardp-1]
            
def move(x, y):
    (mouseX, mouseY) = pygame.mouse.get_pos()
    dx = mouseX - x
    dy = mouseY - y
    dx -= P_1c.get_size()[0]//2
    dy -= P_1c.get_size()[1]//2
    angle = 0.5*math.pi + math.atan2(dy, dx)
    speed = math.hypot(dx, dy) * 0.1
    x += math.sin(angle) * speed
    y -= math.cos(angle) * speed
    return (x, y)

def index_to_exist_card(index):
    if 0 == index:
        return exist1_card, card1_position
    elif 1 == index:
        return exist2_card, card2_position
    elif 2 == index:
        return exist3_card, card3_position
    elif 3 == index:
        return exist4_card, card4_position
    elif 4 == index:
        return exist5_card, card5_position
    elif 5 == index:
        return exist6_card, card6_position
        
def check_xy(index):
    global connect_xy

    exist_card, card_position = index_to_exist_card(index)
    (temp_x, temp_y) = card_position
    
    i = 1
    while exist_card[i] != -1:
        (temp_x, temp_y) = (card_position[0]  - i*P_1c.get_width(), card_position[1])
        i += 1
    
    temp_x -= P_1c.get_width()
    connect_xy[index] = (temp_x, temp_y)
    
    return i

def op_connect_mark(deleted_i):
    global connect_mark
    global win
    
    if 5 == deleted_i:
        connect_mark[5] = 0
        if 0 == connect_mark[4]:
            connect_mark[2] = 1
    elif 4 == deleted_i:
        connect_mark[4] = 0
        if 0 == connect_mark[5]:
            connect_mark[2] = 1
        if 0 == connect_mark[3]:
            connect_mark[1] = 1
    elif 3 == deleted_i:
        connect_mark[3] = 0
        if 0 == connect_mark[4]:
            connect_mark[1] = 1
    elif 2 == deleted_i:
        connect_mark[2] = 0
        if 0 == connect_mark[1]:
            connect_mark[0] = 1
    elif 1 == deleted_i:
        connect_mark[1] = 0
        if 0 == connect_mark[2]:
            connect_mark[0] = 1
    elif 0 == deleted_i:
        win = 1
    
def check_card_sum(index):
    global game_over
    
    exist_card, card_position = index_to_exist_card(index)
    
    i = 1
    sum = (exist_card[0]//4 + 1)
    while exist_card[i] != -1:
        if 0 == i%2 :
            sum += (exist_card[i]//4 + 1)
        else:
            sum -= (exist_card[i]//4 + 1)
        i += 1
    
    if 0 == sum:
        capture_sound.play()
        op_connect_mark(index)
        exist_card[0] = -1
        exist_card[i-1] = -1
    elif cardp > 51:
        game_over = True
    elif exist_card[max_of_card - 1] != -1:
        game_over = True
    elif 1 == switch_on:
        screen.blit(write("%d" % sum, (24,132,74)),(card_position[0] + 40, card_position[1] + 24))
    
def main():
    global all_card
    global exist1_card
    global exist2_card
    global exist3_card
    global exist4_card
    global exist5_card
    global exist6_card
    global selected
    global select_card_xy
    global connect_xy
    global connect_mark
    global game_over
    global new_game
    global cardp
    global dock_xy
    global select_card_xy
    global selected
    global switch_on
    global win
    
    while True:
        if True == new_game:
            exist1_card = [-1] * (max_of_card + 1)
            exist2_card = [-1] * (max_of_card + 1)
            exist3_card = [-1] * (max_of_card + 1)
            exist4_card = [-1] * (max_of_card + 1)
            exist5_card = [-1] * (max_of_card + 1)
            exist6_card = [-1] * (max_of_card + 1)
            all_card    = [x for x in range(52)]
        
            cardp = 0
            
            random.shuffle(all_card)
            exist1_card[0] = assign_card()
            exist2_card[0] = assign_card()
            exist3_card[0] = assign_card()
            exist4_card[0] = assign_card()
            exist5_card[0] = assign_card()
            exist6_card[0] = assign_card()
            
            # Test to win
            #all_card[cardp]   = exist4_card[0]
            #all_card[cardp+1] = exist5_card[0]
            #all_card[cardp+2] = exist2_card[0]
            #all_card[cardp+3] = exist6_card[0]
            #all_card[cardp+4] = exist3_card[0]
            #all_card[cardp+5] = exist1_card[0]
            # End test to win
            
            # 0: can't connect card, 1: can connect card, -1: ini
            connect_mark = [-1, -1, -1, 1, 1, 1]
            connect_xy = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
            
            win = 0
            dock_xy = (50, (screen_height//2 + 3*P_1c.get_height()))
            select_card_xy = dock_xy
            selected = False
            game_over = False
            new_game = False
    
        if selected == True:
            select_card_xy = move(select_card_xy[0], select_card_xy[1])
        
        display_all_card()
    
        if True == game_over:
            screen.blit(game_over_image, ((screen_width - game_over_image.get_width())//2, (screen_height - game_over_image.get_height())//2))
            new_game = True
            pygame.display.update()
            time.sleep(5)
        elif 1 == win:
            screen.blit(win_image, ((screen_width - win_image.get_width())//2, (screen_height - win_image.get_height())//2))
            new_game = True
            pygame.display.update()
            win_sound.play()
            time.sleep(5)
        
        for i in range(6):
            if 1 == connect_mark[i]:
                check_card_sum(i)
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if dock_xy[0] < mouseX < dock_xy[0] + P_1c.get_width() and dock_xy[1] < mouseY < dock_xy[1] + P_1c.get_height():
                    selected = True
                elif (screen_width - new_game_image.get_width())//2 < mouseX < (screen_width + new_game_image.get_width())//2 and screen_height - 150 < mouseY < screen_height - 150 + new_game_image.get_height():
                    new_game = True
                elif screen_width - 160 < mouseX < screen_width - 160 + on_image.get_width() and screen_height - 200 < mouseY < screen_height - 200 + on_image.get_height():
                    switch_on = 1 - switch_on
            elif event.type == MOUSEBUTTONUP:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if True == selected:
                    for i in range(6):
                        if 1 == connect_mark[i]:
                            p = check_xy(i)
                            (cx, cy) = connect_xy[i]
                            if cx < mouseX < cx + P_1c.get_width() and cy < mouseY < cy + P_1c.get_height():    
                                exist_card, card_position = index_to_exist_card(i)
                                exist_card[p] = assign_card()
                                break
                selected = False                        
                    
    exit()
		
if __name__ == "__main__":
    main()
    