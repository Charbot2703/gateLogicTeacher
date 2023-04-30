import pygame

class Button:

    def __init__(self, x, y, text, color, function):
        self.x = x
        self.y = y
        self.text = text
        self.textobject = pygame.font.SysFont("adobegothicstdkalin", 70).render(self.text, False, (0, 0, 0))
        self.width = 200 + (len(text) - 4) * 25
        self.height = 100
        self.color = color
        self.function = function
    
    def isMouseInside(self):
        return ((pygame.mouse.get_pos()[0] >= self.x and pygame.mouse.get_pos()[0] <= self.x + self.width) and
                (pygame.mouse.get_pos()[1] >= self.y and pygame.mouse.get_pos()[1] <= self.y + self.height))
    
    def getFunction(self):
        return self.function

    def draw(self, screen):
        text_size = self.textobject.get_size()
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        screen.blit(self.textobject, (self.x + (self.width - text_size[0])//2, self.y + (self.height - text_size[1])//2))
        
