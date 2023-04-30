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
        pygame.draw.circle(screen, "red" if self.val else "black", (self.x, self.y), self.radius)

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