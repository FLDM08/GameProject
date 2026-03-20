#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, MENU_OPTIONS, C_WHITE, C_YELLOW, C_BROWN
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Menu:
    def __init__(self, window):
        self.window = window
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('MenuBg'))


    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            #DRAW IMAGES
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            self.menu_text(60, "WASTELAND", C_BROWN, ((WIN_WIDTH / 2), 70))
            self.menu_text(60, "Shooter", C_BROWN, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTIONS[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(30, MENU_OPTIONS[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()


            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Close window
                    quit() # Close pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # DOWN KEY
                        if menu_option < len(MENU_OPTIONS) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTIONS) - 1
                    if event.key == pygame.K_RETURN: # ENTER
                        return MENU_OPTIONS[menu_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucinda Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
