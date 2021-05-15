# import 

import os
import math
from pygame.locals import *


# générer fenêtre du jeu
pygame.font.init()

# assets / texte


# avoir les rect des boutons

# play button
play_button_rect = play_button.get_rect()
play_button_rect.x = 0
play_button_rect.y = math.ceil(screen.get_height() / 3)

# credits button
credits_button_rect = credits_button.get_rect()
credits_button_rect.x = 0
credits_button_rect.y = math.ceil(screen.get_height() / 2.2)

# exit button
exit_button_rect = exit_button.get_rect()
exit_button_rect.x = math.ceil(screen.get_width() / 1.085)
exit_button_rect.y = 10

# title
title_rect = title.get_rect()
title_rect.x = math.ceil(screen.get_width() / 2.45)
title_rect.y = math.ceil(screen.get_height() / 100)

# text
text_rect = text.get_rect()
text_rect.x = math.ceil(screen.get_width() / 2.1)
text_rect.y = math.ceil(screen.get_height() / 8)


# by
by_rect = by.get_rect()
by_rect.x = math.ceil(screen.get_width() / 60)
by_rect.y = math.ceil(screen.get_width() / 60)

# noms
noms_rect = noms.get_rect()
noms_rect.x = math.ceil(screen.get_width() / 3)
noms_rect.y = math.ceil(screen.get_width() / 8)


# Boucles de jeu

def game():
    running = True
    while running:
        screen.blit(background, (0, 0))
        screen.blit(exit_button, exit_button_rect )
        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        main_menu()
            elif event.type == MOUSEBUTTONDOWN:
                exit_button_rect.collidepoint(event.pos)
                main_menu()
            pygame.display.flip()

def main_menu():
    running = True
    while running:

        screen.blit(background, (0, 0))
        screen.blit(title, title_rect)
        screen.blit(play_button, play_button_rect)
        screen.blit(credits_button, credits_button_rect)
        screen.blit(text, text_rect)
        
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    game()
                elif credits_button_rect.collidepoint(event.pos):
                    credits()
            pygame.display.flip()            

def credits():
    running = True
    while running:
        screen.blit(credit_bg, (0, 0))
        screen.blit(exit_button, exit_button_rect)
        screen.blit(by, by_rect)
        screen.blit(noms, noms_rect)
        
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        main_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(event.pos):
                    main_menu()
        pygame.display.flip()
main_menu()
