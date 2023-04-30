import pygame
from node import *

class Gate():
    def __init__(self, pos, color, text, num_of_inputs, num_of_outputs, logic):
        self.pos = pos
        self.size = (200 + (len(text) - 4) * 25, 50 + 30*max(num_of_inputs, num_of_outputs))
        self.color = color
        self.text = text
        self.textobject = pygame.font.SysFont("adobegothicstdkalin", 70).render(self.text, False, (0, 0, 0))
        self.inputs = [InputNode(0, 0, 15) for i in range(num_of_inputs)]
        self.outputs = [Node(0, 0, 15) for i in range(num_of_outputs)]
        self.logic = logic

    def getX(self):
        return self.pos[0]
    
    def setX(self, val):
        self.pos = (val, self.pos[1])
        for i in range(len(self.inputs)):
            self.inputs[i].setPos(self.pos[0], self.pos[1]+(self.size[1]/(len(self.inputs)+1)*(i+1)))
        for i in range(len(self.outputs)):
           self.outputs[i].setPos(self.pos[0]+self.size[0], self.pos[1]+(self.size[1]/(len(self.outputs)+1)*(i+1)))

    def getY(self):
        return self.pos[1]
    
    def setY(self, val):
        self.pos = (self.pos[0], val)

    def getWidth(self):
        return self.size[0]
    
    def getHeight(self):
        return self.size[1]

    def setInput(self, value, index):
        self.inputs[index].setValue(value)

    def setInputs(self, inputs):
        for index in range(len(self.inputs)):
            self.inputs[index].setValue(inputs[index])
    
    def getInputs(self):
        return self.inputs
    
    def getOutputs(self):
        return self.outputs

    def evaluate(self):
        for node in self.inputs:
            node.setValue(node.getPrevNodeValue())
        output = self.logic[int("".join([str(i.getValue()) for i in self.inputs]), 2)]
        for i in range(len(output)):
            self.outputs[i].setValue(output[i])

    def draw(self, screen):
        text_size = self.textobject.get_size()
        pygame.draw.rect(screen, self.color, (self.pos, self.size))
        screen.blit(self.textobject, (self.pos[0] + (self.size[0] - text_size[0])//2, self.pos[1] + (self.size[1] - text_size[1])//2))
        for iNode in self.inputs:
            iNode.draw(screen)
        for oNode in self.outputs:
            oNode.draw(screen)
