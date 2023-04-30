import pygame
from gate import Gate 
from levels import Level
from gate_info import *
from toolbox import ToolBox
from button import Button
from menu import MenuManager

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900


def insideGate(gate, x, y):
    return ((x >= gate.getX() and x < (gate.getX() + gate.getWidth())) and 
            (y >= gate.getY() and y < (gate.getY() + gate.getHeight())))

def insideNode(node, x, y):
    return ((x >= node.getX() - node.getRadius() and x < (node.getX() + node.getRadius())) and 
            (y >= node.getY() - node.getRadius() and y < (node.getY() + node.getRadius())))

def getGrabbedNode(nodes, mx, my):
    for node in nodes:
        if insideNode(node, mx, my):
            return node
    return None

def getGrabbedGate(gates, mx, my):
    for gate in gates:
        if insideGate(gate, mx, my):
            return gate
    return None

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
pause = True
inGame = False
running = True

l = Level(2, 1, [0, 1, 1, 0], "PASS")

toolbox = ToolBox(100)

game = MenuManager()

haveGate = False
haveNode = False
levelNode = False
draw_toolbox = False
while game.getMenuVars().getRunning():
    #================================================ Main Menu Loop
    while game.getMenuVars().getMain():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.quitGame()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game.resumeGame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in game.getMainMenuButtons():
                    if button.isMouseInside():
                        button.getFunction()()
        screen.fill("white")
        for button in game.getMainMenuButtons():
            button.draw(screen)
        clock.tick(144)
        pygame.display.flip()
        #============================================ End Main Menu

    #================================================ Pause Loop
    while game.getMenuVars().getPause():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.quitGame()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game.resumeGame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in game.getPauseButtons():
                    if button.isMouseInside():
                        button.getFunction()()
        screen.fill("white")
        for button in game.getPauseButtons():
            button.draw(screen)
        clock.tick(144)
        pygame.display.flip()
        #============================================ End Pause

    #================================================ Game loop
    while game.getMenuVars().getGame():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.quitGame()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game.pauseGame()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                draw_toolbox = not draw_toolbox
            if event.type == pygame.MOUSEBUTTONDOWN:
                if draw_toolbox:
                    grabbedGate = getGrabbedGate(toolbox.getTools(), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    if grabbedGate != None:
                        chosen_one = toolbox.createGate(grabbedGate)
                        chosen_one.setPos(WINDOW_WIDTH//2-chosen_one.getWidth()//2, WINDOW_HEIGHT//2-chosen_one.getHeight()//2)
                        l.addGate(chosen_one)
                        draw_toolbox = False
                        break
                grabbedNode = getGrabbedNode(l.getInputs(), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                if grabbedNode != None:
                    levelNode = True
                if not levelNode:
                    for gate in l.getGates():
                        grabbedNode = getGrabbedNode(gate.getOutputs(), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                        if grabbedNode != None:
                            haveNode = True
                            break
                if (not haveNode) and (not levelNode):
                    grabbedGate = getGrabbedGate(l.getGates(), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    if grabbedGate != None:
                        haveGate = True
            if event.type == pygame.MOUSEBUTTONUP:
                if levelNode:
                    if getGrabbedNode(l.getInputs(), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]) == grabbedNode:
                        grabbedNode.setValue(1 - grabbedNode.getValue())
                        grabbedNode = None
                        levelNode = False
                    else:
                        haveNode = True
                        levelNode = False
                if haveNode:
                    destNode = getGrabbedNode(l.getOutputs(), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    if destNode != None:
                        destNode.setPrevNode(grabbedNode)
                        haveNode = False
                    if haveNode:
                        for gate in l.getGates():
                            destNode = getGrabbedNode(gate.getInputs(), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                            if destNode != None:
                                destNode.setPrevNode(grabbedNode)
                                haveNode = False
                                break
                grabbedNode = None
                destNode = None
                grabbedGate = None
                haveGate = False
                haveNode = False
        
        if haveGate:
            grabbedGate.setX(pygame.mouse.get_pos()[0] - (grabbedGate.getWidth()/2))
            grabbedGate.setY(pygame.mouse.get_pos()[1] - (grabbedGate.getHeight()/2))

        screen.fill("white")
        for i in range(len(l.getInputs())):
            l.getInputs()[i].draw(screen)
        for i in range(len(l.getOutputs())):
            l.getOutputs()[i].setValue(l.getOutputs()[i].getPrevNodeValue())
            l.getOutputs()[i].draw(screen)
        for i in range(len(l.getGates()) - 1, -1, -1):
            l.getGates()[i].evaluate()
            l.getGates()[i].draw(screen)
        if draw_toolbox:
            screen.fill("white")
            toolbox.draw(screen, 8)

        clock.tick(144)
        pygame.display.flip()
        #========================================= End Game Loop

pygame.quit()