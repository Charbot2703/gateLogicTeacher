import pygame
from gate import Gate 
from levels import Level
from gate_info import *
from toolbox import ToolBox
from button import Button
from menu import MenuManager
from node import *

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900


def drawGrabbedNode(screen, grabbedNode):
    color = pygame.Color("red" if grabbedNode.val else "black")
    pygame.draw.line(screen, color, (grabbedNode.getX(), grabbedNode.getY()), (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]), 10)

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

l = Level(2, 1, [1, 1, 1, 0], "PASS")

mainMenuNode = Node(50, 450, 30)
mainNodes = [mainMenuNode]
startGameNode = InputNode(200, 350, 15)
quitGameNode = InputNode(200, 600, 15)
startGameFake = Node(550, 350, 15)
quitGameFake = Node(400, 600, 15)
startGameFake.setValue(1)
quitGameFake.setValue(1)
menuNodes = [startGameNode, quitGameNode, startGameFake, quitGameFake]
eduGame = Gate((900, 450-50), pygame.Color("#16A085"), "EduGate", 3, 2, lambda x: [1, 0])
fake_and = Gate((650, 200), pygame.Color("#2980B9"), "AND", 2, 1, all_gates[1])
fake_or = Gate((1350, 550), pygame.Color("#2C3E50"), "OR", 2, 1, all_gates[3])
fake_exor = Gate((600, 600), pygame.Color("#F1C40F"), "EXOR", 2, 1, all_gates[4])
fake_adder = Gate((1300, 150), pygame.Color("#E67E22"), "ADDER", 3, 2, all_gates[5])
fake_gates = [eduGame, fake_adder, fake_and, fake_exor, fake_or]
eduGame.getInputs()[1].setPrevNode(quitGameFake)
fake_exor.getInputs()[1].setPrevNode(quitGameFake)
fake_and.getInputs()[0].setPrevNode(startGameFake)
fake_and.getInputs()[1].setPrevNode(startGameFake)
fake_adder.getInputs()[2].setPrevNode(eduGame.getOutputs()[0])
fake_adder.getInputs()[0].setPrevNode(fake_and.getOutputs()[0])
fake_or.getInputs()[0].setPrevNode(eduGame.getOutputs()[1])
fake_or.getInputs()[1].setPrevNode(fake_exor.getOutputs()[0])
eduGame.getInputs()[0].setPrevNode(fake_and.getOutputs()[0])
eduGame.getInputs()[2].setPrevNode(fake_exor.getOutputs()[0])
for i in range(2):
    for gates in fake_gates:
        gates.setX(gates.getX())
        gates.evaluate()



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
                # for button in game.getMainMenuButtons():
                #     if button.isMouseInside():
                #         button.getFunction()()
                grabbedNode = getGrabbedNode(mainNodes, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                if grabbedNode != None:
                    levelNode = True
            if event.type == pygame.MOUSEBUTTONUP:
                if levelNode:
                    if getGrabbedNode(mainNodes, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]) == grabbedNode:
                        grabbedNode.setValue(1 - grabbedNode.getValue())
                        grabbedNode = None
                        levelNode = False
                    else:
                        levelNode = False
                destNode = getGrabbedNode(menuNodes, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                if destNode != None:
                    destNode.setPrevNode(grabbedNode)
                    grabbedNode = None
        startGameNode.setValue(startGameNode.getPrevNodeValue())
        if startGameNode.getValue():
            game.startGame()
        screen.fill(pygame.Color("#43455C"))
        try:
            if grabbedNode != None:
                drawGrabbedNode(screen, grabbedNode)
        except:
            pass
        mainMenuNode.draw(screen)
        for button in game.getMainMenuButtons():
            button.draw(screen)
        for nodes in menuNodes:
            nodes.draw(screen)
        for gates in fake_gates:
            gates.draw(screen)
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
        screen.fill((pygame.Color("#43455C")))
        for button in game.getPauseButtons():
            button.draw(screen)
        clock.tick(144)
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

        
        screen.fill((pygame.Color("#43455C")))
        if grabbedNode != None:
            drawGrabbedNode(screen, grabbedNode)
        for i in range(len(l.getInputs())):
            l.getInputs()[i].draw(screen)
        for i in range(len(l.getOutputs())):
            l.getOutputs()[i].setValue(l.getOutputs()[i].getPrevNodeValue())
            l.getOutputs()[i].draw(screen)
        for i in range(len(l.getGates()) - 1, -1, -1):
            l.getGates()[i].evaluate()
            l.getGates()[i].draw(screen)
        if draw_toolbox:
            toolbox.draw(screen, 8)

        clock.tick(144)
        pygame.display.flip()
        #========================================= End Game Loop

pygame.quit()