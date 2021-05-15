from os import system
from random import *
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
screen.blit(fond_combat , (0, 0))

smallfont = pygame.font.SysFont('Corbel',35) 

def Texte(texte) :
    text = smallfont.render(texte , True , color) 
    return text

dictionnaire = {
    "ta mere" : "sujet",
    "ton pere" : "sujet",
    "ta soeur" : "sujet",
    "ton frere" : "sujet",
    "un chien" : "sujet",
    "un lama" : "sujet",
    "est moche" : "verbe",
    "pue" : "verbe",
    "suce" : "verbe",
    "mange" : "verbe",
    "et" : "liaison",
    "sur" : "liaison",
    "en string" : 'complement',
    "en slip" : 'complement',
}

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

        afficher_tableau(tableau_mots)

        if self.phrase_finie != True :

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
                    

                    # if 720 <= mouse[0] <= 720+480 and 200 <= mouse[1] <= 180+72:
                    #     if len(tableau_mots) >= 1 :
                    #         if check_phrase(self.phrase, tableau_mots[0]) :
                    #             self.phrase.append(tableau_mots[0])
                    #             del tableau_mots[0]
                    #             choix_mot = True
                    # if 720 <= mouse[0] <= 720+480 and 252 <= mouse[1] <= 252+72: 
                    #     if len(tableau_mots) >= 2 :
                    #         if check_phrase(self.phrase, tableau_mots[1]) :
                    #             self.phrase.append(tableau_mots[1])
                    #             del tableau_mots[1]
                    #             choix_mot = True
                    # if 720 <= mouse[0] <= 720+480 and 324 <= mouse[1] <= 324+72:
                    #     if len(tableau_mots) >= 3 :
                    #         if check_phrase(self.phrase, tableau_mots[2]) :
                    #             self.phrase.append(tableau_mots[2])
                    #             del tableau_mots[2]
                    #             choix_mot = True
                    # if 720 <= mouse[0] <= 720+480 and 396 <= mouse[1] <= 396+72:
                    #     if len(tableau_mots) >= 4 :
                    #         if check_phrase(self.phrase, tableau_mots[3]) :
                    #             self.phrase.append(tableau_mots[3])
                    #             del tableau_mots[3]
                    #             choix_mot = True
                    # if 720 <= mouse[0] <= 720+480 and 468 <= mouse[1] <= 468+72:
                    #     if len(tableau_mots) >= 5 :
                    #         if check_phrase(self.phrase, tableau_mots[4]) : 
                    #             self.phrase.append(tableau_mots[4])
                    #             del tableau_mots[4]
                    #             choix_mot = True
                    # if 720 <= mouse[0] <= 720+480 and 540 <= mouse[1] <= 540+72:
                    #     if len(tableau_mots) >= 6 :
                    #         if check_phrase(self.phrase, tableau_mots[5]) :
                    #             self.phrase.append(tableau_mots[5])
                    #             del tableau_mots[5]
                    #             choix_mot = True
                    # if 720 <= mouse[0] <= 720+480 and 612 <= mouse[1] <= 612+72: 
                    #     if len(tableau_mots) >= 7 :
                    #         if check_phrase(self.phrase, tableau_mots[6]) :
                    #             self.phrase.append(tableau_mots[6])
                    #             del tableau_mots[6]
                    #             choix_mot = True
                    # if 720 <= mouse[0] <= 720+480 and 684 <= mouse[1] <= 684+72: 
                    #     if len(tableau_mots) >= 8 :
                    #         if check_phrase(self.phrase, tableau_mots[7]) :
                    #             self.phrase.append(tableau_mots[7])
                    #             del tableau_mots[7]
                    #             choix_mot = True
                    # if 720 <= mouse[0] <= 720+480 and 756 <= mouse[1] <= 756+72:
                    #     if len(tableau_mots) >= 9 : 
                    #         if check_phrase(self.phrase, tableau_mots[8]) :
                    #             self.phrase.append(tableau_mots[8])
                    #             del tableau_mots[8]
                    #             choix_mot = True
                    # if 720 <= mouse[0] <= 720+480 and 828 <= mouse[1] <= 828+72: 
                    #     if len(tableau_mots) >= 10 :
                    #         if check_phrase(self.phrase, tableau_mots[9]) :
                    #             self.phrase.append(tableau_mots[9])
                    #             del tableau_mots[9]     
                    #             choix_mot = True                      
                    # if 840 <= mouse[0] <= 840+240 and 955 <= mouse[1] <= 955+60:
                    #     self.phrase_finie = True
                    #     choix_mot = True 

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
            elif dictionnaire[phrase[indice-1]] == "complement" :
                return False
            elif dictionnaire[phrase[indice-1]] == "liaison" :
                return False
            else : print("le mot ne possede pas de type")

    if dictionnaire[mot] == "verbe" :
        if indice == 0 :
            return False
        else :
            if dictionnaire[phrase[indice-1]] == "sujet" :
                return True
            elif dictionnaire[phrase[indice-1]] == "verbe" :
                return False
            elif dictionnaire[phrase[indice-1]] == "complement" :
                return False
            elif dictionnaire[phrase[indice-1]] == "liaison" :
                return True
            else : print("le mot ne possede pas de type")

    if dictionnaire[mot] == "complement" :
        if indice == 0 :
            return False
        else :
            if dictionnaire[phrase[indice-1]] == "sujet" :
                return False
            elif dictionnaire[phrase[indice-1]] == "verbe" :
                return True
            elif dictionnaire[phrase[indice-1]] == "complement" :
                return False
            elif dictionnaire[phrase[indice-1]] == "liaison" :
                return False
            else : print("le mot ne possede pas de type")

    if dictionnaire[mot] == "liaison" :
        if indice == 0 :
            return False
        else :
            if dictionnaire[phrase[indice-1]] == "sujet" :
                return True
            elif dictionnaire[phrase[indice-1]] == "verbe" :
                return True
            elif dictionnaire[phrase[indice-1]] == "complement" :
                return True
            elif dictionnaire[phrase[indice-1]] == "liaison" :
                return False
            else : print("le mot ne possede pas de type")


def creer_tableau(): #Crée et retourne le tableau des mots utilisables en combat en évitant de mettre deux fois les memes mots

    tableau_mots = []
    dico = []
    for key, v in dictionnaire.items() :
        dico.append(key)
    while len(tableau_mots) < 10 :
        n_mot = randint(0, len(dico)-1)
        tableau_mots.append(dico[n_mot])  
    return tableau_mots

def afficher_tableau(tableau_mots):

    # for i in range(10) :
    #     pygame.draw.rect(screen,color_grey,[720,180+72*i,480,72]
    s = pygame.Surface((480,720))
    s.fill(color_black)
    s.set_alpha(200) 
    screen.blit(s, (720,180))

    for i in range(len(tableau_mots)) :
        screen.blit(Texte(tableau_mots[i]) , (760, 200+72*i)) 

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
        elif dictionnaire[joueur1.phrase[len(joueur1.phrase)-1]] == "complément" :
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
        screen.blit(Texte(phrase), (50, 500))
    else : 
        for i in range(len(joueur.phrase)) :
            phrase += str(joueur.phrase[i])
        phrase = list(phrase)
        try:
            phrase[0] = phrase[0].upper()
        except:
            print("Pas encore de phrase")
        phrase = "".join(phrase)
        screen.blit(Texte(phrase), (1500+50, 500))
def redraw():
        screen.blit(fond_combat , (0, 0))
        pygame.draw.rect(screen,color_grey,[81,64,240,60]) #Nom 1
        # pygame.draw.rect(screen,color_black,[81,180,472,835]) #Sprite 1
        s = pygame.Surface((472,835))
        s.fill(color_black)
        s.set_alpha(200) 
        screen.blit(s, (81,180))
        pygame.draw.rect(screen,color_grey,[1599,64,240,60]) #Nom 2
        # pygame.draw.rect(screen,color_black,[1367,180,472,835]) #Sprite 2 
        s = pygame.Surface((472,835))
        s.fill(color_black)
        s.set_alpha(200)
        screen.blit(s, (1367,180))
        pygame.draw.rect(screen,color_grey,[840,955,240,60]) #Bouton finir phrase

        screen.blit(Texte("Nom 1") , (81, 64)) #Nom 1
        screen.blit(Texte("Nom 2") , (1599, 64)) #Nom 2
        screen.blit(Texte("Finir phrase"), (840, 955)) #Finir phrase
def combat(joueur1, joueur2):

    tableau_mots = creer_tableau()

    while joueur1.pv > 0 and joueur2.pv >0 :
        while (len(tableau_mots) > 0 and (joueur1.phrase_finie == False and joueur2.phrase_finie == False)):       
            joueur1.Tour_joueur(tableau_mots)
            redraw()
            afficher_phrase(joueur1, 1)
            afficher_phrase(joueur2, 2)
            joueur2.Tour_joueur(tableau_mots)
            redraw()
            afficher_phrase(joueur1, 1)
            afficher_phrase(joueur2, 2) 

        calcul_degats(joueur1,joueur2)
        calcul_degats(joueur2,joueur1)
        tableau_mots = creer_tableau()

        joueur1.phrase = []
        joueur2.phrase = []

J1 = Joueur()
J1.classe = 'humain'
J1.nom = "zeubiumaru"

J2 = Joueur()
J2.nom="conarman"

mouse = pygame.mouse.get_pos() 

redraw()     
combat(J1,J2)
