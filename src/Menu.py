import pygame
import inits
from Button import Button
from Tutorial import Tutorial
import time

class Menu(object):

    def __init__(self, screen):

        # initialize pygame for mixer, and save screen
        pygame.init()
        self.screen = screen
        
        # Var to keep track of highlighted positon
        self.current_pos = None
        self.choice = None
        
        # Var for Blinking function
        self.timer = 0
        self.up = True
        
        # Keeps the game 30 frames per second, used later
        self.clock = pygame.time.Clock()

        # Button Sprites
        self.ButtonSprites = pygame.sprite.Group()                        # Group to hold Button Sprite
        self.start_button = Button(396, 304, self.ButtonSprites, "START") # Start Button
        
        # Music BG
        pygame.mixer.music.load("./assets/sounds/bg_music.ogg")
        #pygame.mixer.music.play(-1, 0.0)    
        
        # Sound Effects
        self.hover_sound = pygame.mixer.Sound("./assets/sounds/hover.ogg")
        self.select_sound = pygame.mixer.Sound("./assets/sounds/select.ogg")

        # Load images
        self.background_image = pygame.image.load("./assets/images/background.png")
        self.title_image = pygame.image.load("./assets/images/STONKS_title.png")
     
        
    def main(self):
        
        while 1:
            
            self.clock.tick(30)    
            
            for event in pygame.event.get():

                # To exit the Program w/ either the exit button in the corner, or the escape key
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                
                for button in self.ButtonSprites.sprites():
                    button_value = button.handle_event(event)
                    
                    if button_value is not None:

                        self.select_sound.play()
                        print(f'Button clicked with value: {button_value}')
                        self.choice = button_value

            
            # Render Images 
            self.screen.fill((0, 0, 0)) 
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.title_image, (155, 30))
            self.ButtonSprites.draw(self.screen)
            pygame.display.flip()

            if self.choice:
                pygame.mixer.music.stop()
                return(Tutorial(self.screen).main())

# Runs an instance of the Menu() class
if __name__ == "__main__":
    screen = inits.screen()
    pygame.display.set_caption("STONKERS")
    Menu(screen).main()
