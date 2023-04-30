import pygame

class Node:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.val = 0

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def getValue(self):
        return self.val
    
    def setValue(self, val):
        self.val = val

    def getRadius(self):
        return self.radius

    def draw(self, screen):
        color = pygame.Color("red" if self.val else "black")
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)
        if self.isMouseInside():
            bright = lambda c: min(255, c+50)
            pygame.draw.circle(screen, (bright(color.r), bright(color.g+50), bright(color.b+50)), (self.x, self.y), self.radius)

    def isMouseInside(self):
        return ((pygame.mouse.get_pos()[0] >= self.x - self.radius and pygame.mouse.get_pos()[0] <= self.x + self.radius) and
                (pygame.mouse.get_pos()[1] >= self.y - self.radius and pygame.mouse.get_pos()[1] <= self.y + self.radius))


class InputNode(Node):
    def __init__(self, x, y, radius):
        super(InputNode, self).__init__(x, y, radius)
        self.prevNode = None

    def getPrevNodeValue(self):
        if self.prevNode:
            return self.prevNode.getValue()
        return 0
    
    def setPrevNode(self, node):
        self.prevNode = node

    def draw(self, screen):
        super().draw(screen)
        if self.prevNode:
            pygame.draw.line(screen,  "red" if self.prevNode.getValue() else "black", (self.x, self.y), (self.prevNode.getX(), self.prevNode.getY()), 10)
