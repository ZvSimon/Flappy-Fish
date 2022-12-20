from math import sin

from constantes import *


# def vitesse_x(vitesse, angle): 
# return vitesse * cos(angle)


def vitesse_y(t,vitesse, angle):
    return GRAVITE * t - vitesse * sin(angle) #les y positifs sont vers le bas d'où le changement de signe(par rapport aux équations horraires)


def retourner_temps(temps): 
    minutes, secondes = divmod(temps, 60) 

    return int(minutes), round(secondes, 1) #afficher le temps.
