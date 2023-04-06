import pygame
import inits
from Button import Button
import time

class Tutorial(object):

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
        self.ButtonSprites = pygame.sprite.Group()                           # Group to hold Button Sprite
        self.start_button = Button(710, 542, self.ButtonSprites, "NEXT")     # Start Button
        self.start_button = Button(85, 542, self.ButtonSprites, "PREVIOUS") # Start Button
        
        # Music BG
        #pygame.mixer.music.load("./assets/sounds/bg_music.ogg")
        #pygame.mixer.music.play(-1, 0.0)    
        
        # Sound Effects
        self.hover_sound = pygame.mixer.Sound("./assets/sounds/hover.ogg")
        #self.select_sound = pygame.mixer.Sound("./assets/sounds/select.ogg")

        # Load images
        self.background_image = pygame.image.load("./assets/images/background.png")

        # Load tutorial images
        self.tutorial_images = [pygame.image.load(f"./assets/images/tutorial/tutorial_{i}.png") for i in range(1, 7)]
        self.current_tutorial_image = 0
     
        
    def main(self):
        
        while 1:
            
            self.clock.tick(30)    
            
            for event in pygame.event.get():

                # To exit the Program w/ either the exit button in the corner, or the escape key
                if event.type == pygame.QUIT:
                    return("exit")
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return("exit")

                for button in self.ButtonSprites.sprites():
                    button_value = button.handle_event(event)
                    
                    if button_value is not None:

                        # self.select_sound.play()
                        print(f'Button clicked with value: {button_value}')
                        self.choice = button_value

                        # Update the current tutorial image based on the clicked button
                        if button_value == "NEXT" and self.current_tutorial_image < len(self.tutorial_images) - 1:
                            self.current_tutorial_image += 1
                        elif button_value == "PREVIOUS":
                            if self.current_tutorial_image > 0:
                                self.current_tutorial_image -= 1
                            elif self.current_tutorial_image == 0:
                                time.sleep(0.2)  # Add a small delay before returning
                                return "back_to_menu"
            
            # Render Images 
            self.screen.fill((0, 0, 0)) 
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.tutorial_images[self.current_tutorial_image], (35, 35)) # Render the current tutorial image
            self.ButtonSprites.draw(self.screen)
            pygame.display.flip()

# Runs an instance of the Menu() class
if __name__ == "__main__":
    screen = inits.screen()
    pygame.display.set_caption("STONKERS")
    Tutorial(screen).main()
