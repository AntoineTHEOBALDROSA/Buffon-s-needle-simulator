import pygame
import math
import random as rd
pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aiguille de Buffon")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (102, 204, 0)
RED = (255, 51, 51)
DARK_PURPLE = (204, 0, 102)

FONT = pygame.font.SysFont("comicsans", 35)

LINES=9  #rentrer un nombre tel que WIDHT/(lines-1) est entier est mieux
SPACING_LINES = WIDTH/(LINES-1)

def background(win):
    for i in range(LINES):
        pygame.draw.line(win, BLACK, (i*SPACING_LINES, 0), (i*SPACING_LINES, HEIGHT), 4)


def draw_aiguilles(win, number, list_ct):
    for i in range(number):
        x1 = rd.randint(0,800)
        y1 = rd.randint(0,800)
        
        alpha = rd.uniform(0, 2*math.pi)

        x2 = x1 + SPACING_LINES * math.cos(alpha)
        y2 = y1 + SPACING_LINES * math.sin(alpha)

        #print((x1, y1), (x2, y2), math.sqrt((x2-x1)**2+(y2-y1)**2))
        print(x1, x2)
        if (x1<100 and x2>=100) or (x2<100 and x1>=100):
            pygame.draw.line(win, GREEN, (x1, y1), (x2, y2), 2)
            list_ct[0]+=1

        elif x2<=0 or ((int(str(x1)[0]) != int(str(x2)[0])) and x1>=100 and x2>=100 ):
            pygame.draw.line(win, GREEN, (x1, y1), (x2, y2), 2)
            list_ct[0]+=1

        else :
            pygame.draw.line(win, RED, (x1, y1), (x2, y2), 2)
            list_ct[1]+=1
    
    return list_ct


def main():
    run = True
    clock = pygame.time.Clock()    

    list_counter = [0, 0] #green, red
    pi_approx_text=0
    NUM_AIGUILLES = 50

    WIN.fill(WHITE)
    background(WIN)

    #draw_aiguilles(WIN, 100)

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    draw_aiguilles(WIN, NUM_AIGUILLES, list_counter)
                    background(WIN)
                    pi_approx_text = FONT.render(f"π ≈ {round(2/(list_counter[0]/(list_counter[0]+list_counter[1])), 6)}", 1, WHITE)
                    WIN.blit(pi_approx_text,  (690 - WIN.get_width() // 2,0))
                    

                if event.key == pygame.K_c:
                    WIN.fill(WHITE)
                    background(WIN)
                    list_counter = [0, 0] #green, red
                    pi_approx_text=0
                
                if event.key == pygame.K_b:
                    pi_approx_text = FONT.render(f"π ≈ {round(2/(list_counter[0]/(list_counter[0]+list_counter[1])), 6)}", 1, BLACK)
                    WIN.blit(pi_approx_text,  (690 - WIN.get_width() // 2,0))

                if event.key == pygame.K_n:
                    NUM_AIGUILLES = 10000


        pygame.display.update()

    print(list_counter, "approximation 2/pi (2/pi=0,636619772) :",list_counter[0]/(list_counter[0]+list_counter[1]))
    print("Soit pi approximé à :",2/(list_counter[0]/(list_counter[0]+list_counter[1])))
    pygame.quit()

main()

# Réglages 
# ESPACE : jeter des aiguilles
# C : effacer les aiguilles 
# B : afficher l'approximation en noir
# N : changer le nombre d'aiguilles jetés à 10000
