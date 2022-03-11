from time import time
import pygame
import time
import config.colors
#def main(self):
pygame.init()
screen = pygame.display.set_mode(size=(800, 480), flags=pygame.SCALED, depth=0, display=0)
selected = [0, 0] #[x, y]
working = True
display = 1
#vars for protest in software
flag_top_c = pygame.Color(0, 0, 250)
flag_bottom_c = pygame.Color(245, 245, 66)
def startup():
    pygame.draw.rect(screen, flag_top_c, pygame.Rect(0, 0, 800, 240))
    pygame.draw.rect(screen, flag_bottom_c, pygame.Rect(0, 240, 800, 240))
    display = 2
def main_menu():
    pygame.draw.rect(screen, config.colors.bg_color_main, pygame.Rect(0, 0, 800, 480))
while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP8:
                print("Key num 8 has been pressed")
            if event.key == pygame.K_KP5:
                print("Key num 5 has been pressed")
            if event.key == pygame.K_KP2:
                print("Key num 2 has been pressed")
    #octoklipperscreen startup screen. will bring this to a differnt file but
    #for now displays ukraine's flag with #standwithukraine
    if display == 1:
        startup()
    elif display == 2:
        pygame.draw.rect(screen, config.colors.bg_color_main, pygame.Rect(0, 0, 800, 480))
    pygame.display.flip()