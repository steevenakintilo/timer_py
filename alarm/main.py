#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## sd
## File description:
## d
##


import pygame
from random import randint
import pygame.freetype 

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)



def param_loop():
    red = (255,0,0)
    white = (255,255,255)
    pygame.init()
    mins = 0
    h = 0
    sec = 0
    i = 0
    stop = 0
    s = 0
    key = 0
    GAME_FONT = pygame.freetype.Font("f.ttf", 150)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[ord('1')]:
                    key = 1
                if pressed_keys[ord('2')]:
                    key = 2
                if pressed_keys[ord('3')]:
                    key = 3
                if key == 1 and  pressed_keys[K_UP] and h < 23:
                    h = h + 1
                if key == 1 and  pressed_keys[K_DOWN] and h > -1:
                    h = h - 1
                if key == 2 and  pressed_keys[K_UP] and mins < 59:
                    mins = mins + 1
                if key == 2 and  pressed_keys[K_DOWN] and mins > -1:
                    mins = mins - 1
                if key == 3 and  pressed_keys[K_UP] and sec < 60:
                    sec = sec + 1
                if key == 3 and  pressed_keys[K_DOWN] and sec > -1:
                    sec = sec - 1
                if pressed_keys[ord(' ')]:
                    main_loop(h,mins,sec)
                if pressed_keys[ord('x')]:
                    quit()
                if event.key == K_ESCAPE:
                    running = False
                if event.type == pygame.QUIT:
                    quit()
            elif event.type == QUIT:
                running = False
        screen.fill(red)
        GAME_FONT.render_to(screen, (230, 330), str(h) + " : " + str(mins) + " : " + str(sec) , (255, 255, 255))
        GAME_FONT.render_to(screen, (230, 330), str(h) + " : " + str(mins) + " : " + str(sec) , (255, 255, 255))
        pygame.display.flip()
def main_loop(h,mins,sec):
    red = (255,0,0)
    white = (255,255,255)
    pygame.init()
    #mins = 0
    #h = 0
    #sec = 1
    i = 0
    stop = 0
    s = 0
    GAME_FONT = pygame.freetype.Font("f.ttf", 150)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        i = i + 1
        if h == 0 and mins == 0 and sec == -1:
            stop = 2
            pygame.mixer.music.load("alarm.wav")
            pygame.mixer.music.play(-1)
            pygame.mixer.init()
        if stop != 1:
            if i % 800 == 0:
                sec = sec - 1
            if sec == -1 and mins == 0 and h != 0:
                h = h - 1
                mins = 59
                sec = 59
            if sec == -1 and (h != 0 or mins != 0):
                sec = 59
                mins = mins - 1
            if mins == 0 and h != 0 and sec == -1:
                mins = 59
                h = h - 1
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.type == pygame.QUIT:
                    quit()
            elif event.type == QUIT:
                running = False
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[ord('x')]:
            quit()
        screen.fill(red)
        if stop != 2:
            GAME_FONT.render_to(screen, (230, 330), str(h) + " : " + str(mins) + " : " + str(sec) , (255, 255, 255))
        if stop == 2:
            GAME_FONT = pygame.freetype.Font("f.ttf", 100)
            GAME_FONT.render_to(screen, (130, 330), "L'ALARME SONNE" , (255, 255, 255))
        pygame.display.flip()
param_loop()
