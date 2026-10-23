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
    def move(self, x, y):
        """Přesune tlačítko na novou pozici (x, y)."""
        self.rect.x = x
        self.rect.y = y

    def delete(self):
        """Odstraní tlačítko z obrazovky tím, že nastaví jeho obrázek na None."""
        self.image = None

    def draw(self, surface):
        """Vykreslí aktuální obrázek tlačítka na zadané plátno."""
        surface.blit(self.image, self.rect)

class Character:
    def __init__(self, x, y, path_normal, path_pressed):        
        self.img_normal = pygame.image.load(path_normal).convert_alpha()
        self.img_pressed = pygame.image.load(path_pressed).convert_alpha()
        
        self.image = self.img_normal
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

def character_selection():
    btn_dezo = Button(90, 80, "images/characters/dezo.png", "images/characters/dezo.png")
    character = None
    charSelected = False
    if btn_dezo.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
        print("Vybrána postava Dežo!")
        character = btn_dezo  # Přiřadí vybranou postavu do proměnné character

        # character = Character(10, 10, "images/characters/dezo.png", "images/characters/dezo_pressed.png")
        charSelected = True

    if charSelected:
        btn_dezo = None
        # character.draw(display)  # Vykreslí postavu na pozici (90, 80)

    return character
    
def main():
    try:
        background_img = pygame.image.load("images/still/background.png").convert()
    except FileNotFoundError:
        print("Obrázek pozadí nebyl nalezen. Používám čistou barvu.")
        background_img = None

    # --- MENU 1: Úvodní Obrazovka ---
    btn_start = Button(90, 80, "images/buttons_main/start.png", "images/buttons_main/start.png")
    btn_konec = Button(190, 80, "images/buttons_main/konec.png", "images/buttons_main/konec.png")

    # --- MENU 2: Výběr Postavy ---
    btn_dezo = Button(90, 80, "images/characters/dezo.png", "images/characters/dezo.png")
    selected_character = None

    # --- MENU 3: Hlavní Rozcestník Her (Nový stav) ---
    # Ukázková tlačítka pro jednotlivé hry v kasínu (Uprav si cesty k obrázkům)
    # btn_ruleta = Button(40, 60, "images/buttons_games/ruleta.png", "images/buttons_games/ruleta.png")
    # btn_automaty = Button(130, 60, "images/buttons_games/automaty.png", "images/buttons_games/automaty.png")
    # btn_blackjack = Button(220, 60, "images/buttons_games/blackjack.png", "images/buttons_games/blackjack.png")

    # Stavy hry: 'intro_menu', 'char_select', 'game_hub'
    game_state = "intro_menu"

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        pixel_mouse_pos = (mouse_pos[0] // 4, mouse_pos[1] // 4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # --- 1. KRESLENÍ POZADÍ (Vždy první) ---
        if background_img:
            display.blit(background_img, (0, 0))
        else:
            display.fill((40, 40, 40)) # Výchozí tmavá barva

        # --- 2. LOGIKA A KRESLENÍ PODLE STAVU ---
        if game_state == "intro_menu":
            if btn_start.update(pixel_mouse_pos, mouse_click):
                game_state = "char_select"
            if btn_konec.update(pixel_mouse_pos, mouse_click):
                running = False

            btn_start.draw(display)
            btn_konec.draw(display)

        elif game_state == "char_select":
            btn_konec.move(270, 150)  # Přesune tlačítko "Konec" na nové souřadnice
            character =character_selection()  # Vykreslí výběr postavy
                
            # Update univerzálního tlačítka ukončení hry
            if btn_konec.update(pixel_mouse_pos, mouse_click):
                running = False

            if character:
                selected_character = character
                game_state = "game_hub"  # Přepne stav hry na hlavní rozcestník her'
            else:
                # Pokud nebyla vybrána žádná postava, zůstáváme ve stavu výběru postavy
                game_state = "char_select"

            # Vykreslení elementů výběru postavy
            btn_dezo.draw(display)
            btn_konec.draw(display)

            

        # --- 3. PROMIZÁNÍ NA OBRAZOVKU ---
        scaled_display = pygame.transform.scale(display, (WINDOW_W, WINDOW_H))
        screen.blit(scaled_display, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    pygame.display.quit()
    sys.exit()

if __name__ == '__main__':
    main()
