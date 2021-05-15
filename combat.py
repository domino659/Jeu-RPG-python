from os import system
from random import *
from dico import *
from math import floor
import pygame 
import sys 
import time

pygame.init() 
   
res = (1920,1080)  
screen = pygame.display.set_mode(res) 

color = (255,255,255) 
color_light = (170,170,170) 
color_grey = (100,100,100)
color_black = (0,0,0)

width = screen.get_width() 
height = screen.get_height() 

fond_combat = pygame.image.load('Assets/Backgrounds/fond_combat.jpg')
img_perso = pygame.image.load("Assets/Actor/Combat/persofou.png")
img_perso2 = pygame.image.load("Assets/Actor/Combat/persofou2.png")
contour = pygame.image.load("Assets/Backgrounds/contour.png")
contour_sprite = pygame.transform.scale(contour, (472, 835))
contour_tableau = pygame.transform.scale(contour,(480, 720))
perso1 = pygame.transform.scale(img_perso, (402, 745))
perso2 = pygame.transform.scale(img_perso2, (402, 745))
screen.blit(fond_combat , (0, 0))

smallfont = pygame.font.SysFont('Corbel',35)
font_phrase = pygame.font.SysFont('Corbel',30)

def Texte(texte) :
    text = smallfont.render(texte , True , color) 
    return text

class Joueur:

    def __init__(self):
        self.nom = ''
        self.pv_max = 20
        self.pv = self.pv_max
        self.phrase = []
        self.phrase_finie = False
        self.classe = ''
        self.etat = ''

    def Tour_joueur(self, tableau_mots):

        if self.phrase_finie == False :

            afficher_tableau(tableau_mots)
            choix_mot = False

            while choix_mot == False :

                ev = pygame.event.wait()

                while ev.type != pygame.MOUSEBUTTONDOWN:
                    ev = pygame.event.wait()

                if ev.type == pygame.MOUSEBUTTONDOWN: 

                    mouse = pygame.mouse.get_pos()
                    print (self.nom, self.phrase)
                    print (mouse)

                    if 720 <= mouse[0] <= 720+480 and 200 <= mouse[1] <= 200+72*10: 
                        selected_word = floor((mouse[1] - 200) / 72)
                        print(selected_word)
                        try:
                            if check_phrase(self.phrase, tableau_mots[selected_word]):
                                self.phrase.append(tableau_mots[selected_word])
                                del tableau_mots[selected_word]
                                choix_mot = True
                        except:
                            print("Pas de mot ici")

                    if 840 <= mouse[0] <= 840+240 and 955 <= mouse[1] <= 955+60:
                        self.phrase_finie = True
                        choix_mot = True 

def check_phrase(phrase, mot): #Vérifie si le mot choisit est logique par rapport au mot précédent
    indice = len(phrase)
    if dictionnaire[mot] == "sujet" :
        if indice == 0 :
            return True
        else :
            if dictionnaire[phrase[indice-1]] == "sujet" :
                return False
            elif dictionnaire[phrase[indice-1]] == "verbe" :
                return True
            elif dictionnaire[phrase[indice-1]] == "liaison" :
                return True
            else : print("le mot ne possede pas de type")

    if dictionnaire[mot] == "verbe" :
        if indice == 0 :
            return False
        else :
            if dictionnaire[phrase[indice-1]] == "sujet" :
                return True
            elif dictionnaire[phrase[indice-1]] == "verbe" :
                return False
            elif dictionnaire[phrase[indice-1]] == "liaison" :
                return True
            else : print("le mot ne possede pas de type")

    if dictionnaire[mot] == "liaison" :
        if indice == 0 :
            return False
        else :
            if dictionnaire[phrase[indice-1]] == "sujet" :
                return True
            elif dictionnaire[phrase[indice-1]] == "verbe" :
                return True
            elif dictionnaire[phrase[indice-1]] == "liaison" :
                return False
            else : print("le mot ne possede pas de type")


def creer_tableau(): #Crée et retourne le tableau des mots utilisables en combat en évitant de mettre deux fois les memes mots

    tableau_mots = []
    while len(tableau_mots) < 10 :
        if len(tableau_mots) <= 3 :
            mot = choice(list(dictionnaire.items()))
            if mot[1] == "sujet" :
                tableau_mots.append(mot[0])
        elif 3 < len(tableau_mots) <= 7 :
            mot = choice(list(dictionnaire.items()))
            if mot[1] == "verbe" :
                tableau_mots.append(mot[0])
        elif len(tableau_mots) > 7 :
            mot = choice(list(dictionnaire.items()))
            if mot[1] == "liaison" :
                tableau_mots.append(mot[0])
    return tableau_mots

def afficher_tableau(tableau_mots):

    screen.blit(contour_tableau, (720,180))

    for i in range(len(tableau_mots)) :
        screen.blit(Texte(tableau_mots[i]) , (770, 200+72*i)) 

    pygame.display.update()

def calcul_degats(joueur1, joueur2): #Calcule et applique les dégats aux deux joueurs / si la fin de phrase n'est pas logique -1 dégats (ou 0?)

    degats_j1 = 0
    check_v = False
    for mots in joueur1.phrase:
        degats_j1 += 1
    if (joueur1.classe == 'humain' and degats_j1 >= 5): 
        degats_j1 += 2

    if len(joueur1.phrase) > 1 :
        if dictionnaire[joueur1.phrase[len(joueur1.phrase)-1]] == "sujet" :
            for mot in joueur1.phrase :
                if dictionnaire[mot] == "verbe" :
                    check_v = True
            if check_v == False :
                joueur2.pv -= degats_j1
            else :
                joueur2.pv -= degats_j1 - 1
        elif dictionnaire[joueur1.phrase[len(joueur1.phrase)-1]] == "verbe" :
            joueur2.pv -= degats_j1
        else :
            joueur2.pv -= degats_j1 - 1

def afficher_phrase(joueur, nombre) : #Affiche les phrases des deux joueurs
    # Mise en forme du texte, concatenaion de la liste, ajout d'une majuscule en début de phrase
    phrase = ''
    if nombre == 1 :
        for i in range(len(joueur.phrase)) :
            phrase += str(joueur.phrase[i] + " ")
        phrase = list(phrase)
        try:
            phrase[0] = phrase[0].upper()
        except:
            print("Pas encore de phrase")
        phrase = "".join(phrase)
        screen.blit(font_phrase.render(phrase , True , color) , (100, 950))
    else : 
        for i in range(len(joueur.phrase)) :
            phrase += str(joueur.phrase[i] + " ")
        phrase = list(phrase)
        try:
            phrase[0] = phrase[0].upper()
        except:
            print("Pas encore de phrase")
        phrase = "".join(phrase)

        screen.blit(font_phrase.render(phrase , True , color) , (1400, 950))

def redraw(joueur1, joueur2):

    screen.blit(fond_combat , (0, 0))
    #pygame.draw.rect(screen,color_grey,[81,64,240,60]) #Nom 1
    s = pygame.Surface((472,60))
    s.fill(color_black)
    s.set_alpha(200)
    screen.blit(s, (81,64))
    # pygame.draw.rect(screen,color_black,[81,180,472,835]) #Sprite 1
    screen.blit(contour_sprite, (81,180))
    #pygame.draw.rect(screen,color_grey,[1599,64,240,60]) #Nom 2
    s = pygame.Surface((472,60))
    s.fill(color_black)
    s.set_alpha(200)
    screen.blit(s, (1367,64))
    # pygame.draw.rect(screen,color_black,[1367,180,472,835]) #Sprite 2 
    screen.blit(contour_sprite, (1367,180))
    #pygame.draw.rect(screen,color_grey,[840,955,240,60]) #Bouton finir phrase
    s = pygame.Surface((240,60))
    s.fill(color_black)
    s.set_alpha(200)
    screen.blit(s, (840,955))

    pv = str(joueur1.pv)
    screen.blit(Texte(joueur1.nom+" > "+pv+" hp") , (101, 74)) #Nom 1
    pv = str(joueur2.pv)
    screen.blit(Texte(joueur2.nom+" > "+pv+" hp") , (1387, 74)) #Nom 2
    screen.blit(Texte("Finir phrase"), (840, 955)) #Finir phrase

    afficher_phrase(joueur1, 1)
    afficher_phrase(joueur2, 2)

    screen.blit(perso1 , (121, 200))
    screen.blit(pygame.transform.flip(perso2, True, False), (1407,200))


def combat(joueur1, joueur2):

    tableau_mots = creer_tableau()

    while joueur1.pv > 0 and joueur2.pv >0 :
        while (len(tableau_mots) > 0 and (joueur1.phrase_finie == False or joueur2.phrase_finie == False)):       
            joueur1.Tour_joueur(tableau_mots)
            redraw(joueur1, joueur2)
            joueur2.Tour_joueur(tableau_mots)
            redraw(joueur1, joueur2)

        calcul_degats(joueur1,joueur2)
        calcul_degats(joueur2,joueur1)
        tableau_mots = creer_tableau()

        joueur1.phrase = []
        joueur1.phrase_finie = False
        joueur2.phrase = []
        joueur2.phrase_finie = False
        redraw(joueur1, joueur2)