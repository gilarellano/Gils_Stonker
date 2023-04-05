import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite_group=None, value=None):
        super().__init__()
        self.x = x
        self.y = y
        self.button_pos = (self.x, self.y)
        self.value = value

        self.image_normal = pygame.image.load("./assets/images/buttons/%s.png" % (self.value))
        self.image_hover = pygame.image.load("./assets/images/buttons/%s_hover.png" % (self.value))
        self.rect_normal = pygame.Rect((self.button_pos), self.image_normal.get_size())
        self.rect_hover = pygame.Rect((self.button_pos), self.image_hover.get_size())

        self.image = self.image_normal
        self.rect = self.rect_normal

        if sprite_group is not None:
            sprite_group.add(self)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def handle_event(self, event):
        # Check if the mouse is within the button's bounds
        mouse_x, mouse_y = pygame.mouse.get_pos()
        is_hover = self.x <= mouse_x <= self.x + self.rect.width and self.y <= mouse_y <= self.y + self.rect.height

        # Change the button image on hover
        if is_hover:
            self.image = self.image_hover
            self.rect = self.rect_hover
        else:
            self.image = self.image_normal
            self.rect = self.rect_normal

        # Return the button value when clicked
        if event.type == pygame.MOUSEBUTTONDOWN and is_hover:
            return self.value
        return None