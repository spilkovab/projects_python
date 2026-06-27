from pdb import run
import sys
from unittest import runner
import pygame

pygame.init()

GAME_W, GAME_H = 320, 180

WINDOW_W, WINDOW_H = GAME_W * 4, GAME_H * 4
screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption('Kasíno Rojál')

display = pygame.Surface((GAME_W, GAME_H))

clock = pygame.time.Clock()
FPS = 60

class Button:
    def __init__(self, x, y, path_normal, path_pressed):        
        self.img_normal = pygame.image.load(path_normal).convert_alpha()
        self.img_pressed = pygame.image.load(path_pressed).convert_alpha()
        
        # Výchozí stav je normální obrázek
        self.image = self.img_normal
        
        # Vytvoření obdélníku (Rect) podle velikosti načteného obrázku
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.clicked = False

    def update(self, mouse_pos, mouse_click):
        """Aktualizuje stav tlačítka a vrátí True, pokud na něj hráč kliknul."""
        action = False
        
        # Kontrola, zda myš ukazuje na tlačítko
        if self.rect.collidepoint(mouse_pos):
            # Kontrola kliknutí (levé tlačítko myši)
            if mouse_click[0] == 1:
                self.image = self.img_pressed
                if not self.clicked:
                    self.clicked = True
                    action = True
            else:
                self.image = self.img_normal
        else:
            self.image = self.img_normal # Návrat k původnímu obrázku

        if mouse_click[0] == 0:
            self.clicked = False
            
        return action

    def draw(self, surface):
        """Vykreslí aktuální obrázek tlačítka na zadané plátno."""
        surface.blit(self.image, self.rect)
    
def main():
    try:
            background_img = pygame.image.load("images/still/background.png").convert()
    except FileNotFoundError:
            print("Obrázek pozadí nebyl nalezen. Používám čistou barvu.")
            background_img = None

    btn_start = Button(80, 80, "images/buttons_main/start.png", "images/buttons_main/start.png")
    btn_konec = Button(180, 80, "images/buttons_main/konec.png", "images/buttons_main/konec.png")

    # Uložíme je do seznamu pro snadnou hromadnou správu
    buttons = [btn_start, btn_konec]

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        pixel_mouse_pos = (mouse_pos[0] // 4, mouse_pos[1] // 4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # pygame.quit()
                # sys.exit()
                
        if btn_start.update(pixel_mouse_pos, mouse_click):
            print("Spouštím hru!")
            
        if btn_konec.update(pixel_mouse_pos, mouse_click):
            print("Ukončuji hru.")
            running = False

        if background_img:
            # Pokud obrázek existuje, vykreslíme ho na pozici [0, 0]
            display.blit(background_img, (0, 0))

        for button in buttons:
            button.draw(display)

        scaled_display = pygame.transform.scale(display, (WINDOW_W, WINDOW_H))
        screen.blit(scaled_display, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
