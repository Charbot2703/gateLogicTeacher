
import pygame
from gate import Gate
from gate_info import *

class ToolBox():


    def __init__(self, height):
        self.all_gate_logic = all_gates
        self.not_gate = Gate((800, 450), pygame.Color("#27AE60"), "NOT", 1, 1, all_gates[0])
        self.and_gate = Gate((800, 450), pygame.Color("#2980B9"), "AND", 2, 1, all_gates[1])
        self.nand_gate = Gate((800, 450), pygame.Color("#8E44AD"), "NAND", 2, 1, all_gates[2])
        self.or_gate = Gate((800, 450), pygame.Color("#2C3E50"), "OR", 2, 1, all_gates[3])
        self.exor_gate = Gate((800, 450), pygame.Color("#F1C40F"), "EXOR", 2, 1, all_gates[4])
        self.adder_gate = Gate((800, 450), pygame.Color("#E67E22"), "ADDER", 3, 2, all_gates[5])
        self.four_gate = Gate((800, 450), pygame.Color("#E74C3C"), "4-BIT ADDER", 9, 5, all_gates[6])
        self.eight_gate = Gate((800, 450), pygame.Color("#ECF0F1"), "8-BIT ADDER", 9, 7, all_gates[7])
        self.tool_list = [self.not_gate,
                          self.and_gate,
                          self.nand_gate,
                          self.or_gate,
                          self.exor_gate,
                          self.adder_gate,
                          self.four_gate]
        self.height = 900 - height
        self.define_something()

    def sumWidths(self, gates):
        sum = 0
        for i in gates:
            sum += i.getWidth()
        return sum

    def define_something(self):
        self.gapU = (1600-self.sumWidths(self.tool_list[:4]))/5
        self.gapL = (1600-self.sumWidths(self.tool_list[4:]))/5
        self.upperY = 900/3
        self.lowerY = self.upperY*2

    def draw(self, screen, gates):
        screen.fill((pygame.Color("#43455C")))
        text = pygame.font.SysFont("adobegothicstdkalin", 100).render("TOOLBOX", False, pygame.Color("#3BBA9C"))
        text2 = pygame.font.SysFont("adobegothicstdkalin", 100).render("TOOLBOX", False, "black")
        screen.blit(text2, (((1600-text.get_size()[0])//2)+7,100+7))
        screen.blit(text, ((1600-text.get_size()[0])//2,100))
        for i in range(gates):
            if i < 4:
                self.tool_list[i].setPos((self.gapU*(i+1)+self.sumWidths(self.tool_list[:i])), self.upperY-self.tool_list[i].getHeight()//2)
            else:
                self.tool_list[i].setPos((self.gapL*(i-3)+self.sumWidths(self.tool_list[4:i])), self.lowerY-self.tool_list[i].getHeight()//2)
            self.tool_list[i].draw(screen)

    def getTools(self):
        return self.tool_list
        
    def createGate(self, gate):
        output = Gate((gate.getX(), gate.getY()), gate.getColor(), gate.getText(), len(gate.getInputs()), len(gate.getOutputs()), gate.getLogic())
        return output

    