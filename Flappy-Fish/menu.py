from time import time

from main import main, retourner_temps
import pygame

from constantes import *

pygame.init()

# genere une fenetre pour notre jeu où le jeu sera appelé "Flappy Fish"
pygame.display.set_caption("Flappy Némo")
screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)  # permet de génerer l'ecran autrement dit l'arriere plan
# importation de l'image de l'arriere plan
background = pygame.image.load("./ressources/ciel.png")

# importer l'image du bouton play
play_button = pygame.image.load("./ressources/play.png")
play_button_rect = (
    play_button.get_rect()
)  # pour placer l'image du bouton play dans un rectangle

play_button_rect.x = screen.get_width() // 2 - play_button_rect.w // 2
play_button_rect.y = screen.get_height() // 2 - play_button_rect.h // 2

quit_button = pygame.image.load("./ressources/quit.png")
quit_button_rect = quit_button.get_rect()  # boutton pour quitter le jeu
quit_button_rect.x = screen.get_width() // 2 - quit_button_rect.w // 2
quit_button_rect.y = screen.get_height() // 2 - quit_button_rect.h // 2 + 70


def afficher_menu():
    # pour appliquer la fenetre du jeu et réajustement de l'arriere plan
    screen.blit(background, (0, 0))

    screen.blit(play_button, play_button_rect)
    screen.blit(quit_button, quit_button_rect)

    pygame.display.flip()  # met à jour l'écran


def menu():
    jeu = True

    afficher_menu()

    while jeu:
        # va piocher parmis pleins d'evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jeu = False
                pygame.quit()

            if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(*pygame.cursors.diamond)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # pour quitter la partie
                    jeu = False
                    pygame.quit()

            elif play_button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(*pygame.cursors.diamond)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                    score, temps = main()
                    minutes, secondes = retourner_temps(time() - temps)

                    pygame.font.init()

                    titre = pygame.font.Font(None, 69)
                    sout_titre = pygame.font.Font(None, 42)

                    game_over = titre.render(
                        'Game Over !',
                        True, (0, 0, 0)
                    )
                    game_over_rect = game_over.get_rect()

                    score_text = sout_titre.render(
                        f'Score: {score}',
                        True, (0, 0, 0)
                    )
                    score_text_rect = score_text.get_rect()

                    temps_text = sout_titre.render(
                        f'Temps: {minutes}m {secondes}s',
                        True, (0, 0, 0)
                    )
                    temps_text_rect = temps_text.get_rect()

                    afficher_menu()

                    game_over_rect.center = (
                            screen.get_width() // 2,
                            screen.get_height() // 2 - game_over_rect.h // 2 - 150
                    )
                    score_text_rect.center = (
                        screen.get_width() // 2,
                        screen.get_height() // 2 - score_text_rect.h // 2 - 100
                    )
                    temps_text_rect.center = (
                        screen.get_width() // 2,
                        screen.get_height() // 2 - temps_text_rect.h // 2 - 75
                    )

                    screen.blit(game_over, game_over_rect)
                    screen.blit(score_text, score_text_rect)
                    screen.blit(temps_text, temps_text_rect)

                    pygame.display.flip()

            else:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)


if __name__ == '__main__':
    menu()
