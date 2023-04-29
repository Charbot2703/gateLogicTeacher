import pygame


class Gate():
    def __init__(self, pos, color, text, num_of_inputs, num_of_outputs, logic):
        self.pos = pos
        self.size = (200 + (len(text) - 4) * 25, 50 + 30*max(num_of_inputs, num_of_outputs))
        self.color = color
        self.text = text
        self.textobject = pygame.font.SysFont("adobegothicstdkalin", 70).render(self.text, False, (0, 0, 0))
        self.inputs = [0]*num_of_inputs
        self.outputs = [0]*num_of_outputs
        self.logic = logic

    def setInput(self, value, index):
        self.inputs[index] = value

    def setInputs(self, inputs):
        self.inputs = inputs
    
    def evaluate(self):
        output = self.logic[int("".join([str(i) for i in self.inputs]), 2)]
        self.outputs = output

    def draw(self, screen):
        text_size = self.textobject.get_size()
        pygame.draw.rect(screen, self.color, (self.pos, self.size))
        screen.blit(self.textobject, (self.pos[0] + (self.size[0] - text_size[0])//2, self.pos[1] + (self.size[1] - text_size[1])//2))
        for i in range(len(self.inputs)):
            pygame.draw.circle(screen, "red" if self.inputs[i] else "black", (self.pos[0], self.pos[1]+(self.size[1]/(len(self.inputs)+1)*(i+1))), 10)
        for i in range(len(self.outputs)):
            pygame.draw.circle(screen, "red" if self.outputs[i] else "black", (self.pos[0]+self.size[0], self.pos[1]+(self.size[1]/(len(self.outputs)+1)*(i+1))), 10)
        
