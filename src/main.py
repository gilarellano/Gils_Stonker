import pygame
import inits
from Menu import Menu
from Tutorial import Tutorial
import time  # Add this import at the beginning of the file

if __name__ == "__main__":
    screen = inits.screen()
    pygame.display.set_caption("STONKERS")

    # Initialize the menu and tutorial instances
    menu_instance = Menu(screen)
    tutorial_instance = Tutorial(screen)

    # Main loop to show the menu and tutorial based on user input
    current_screen = "menu"
    while True:
        if current_screen == "menu":

            print("WERE IN MENU")
            menu_result = menu_instance.main()
            print("WE JUST GOT MENU INSTANCE")
            if menu_result == "start_tutorial":
                current_screen = "tutorial"
                time.sleep(0.2)  # Add a small delay after handling the event
            elif menu_result == "exit":
                break

    
        elif current_screen == "tutorial":
            print("WERE IN TUTORIAL")
            tutorial_result = tutorial_instance.main()
            print("WE JUST GOT TUTORIAL INSTANCE")

            if tutorial_result == "back_to_menu":
                current_screen = "menu"
                time.sleep(0.2)  # Add a small delay after handling the event
            elif tutorial_result == "exit":
                break

        else:
            break
