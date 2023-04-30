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

def compareOutputs(outputsA, outputsB):
    if len(outputsA) != len(outputsB):
        return False
    for i in range(len(outputsA)):
        if len(outputsB[i]) > 1:
            for j in range(len(outputsB)):
                if outputsA[i][j] != outputsB[i][j]:
                    return False
        if outputsA[i][0] != outputsB[i][0]:
            return False
    return True

def fix_output(l, padding):
    l = [0]*(padding-len(l)) + l
    l.append(l.pop(0))
    return l

def compareAdderOutputs(outputsA, padding, input):
    iB = [int(k) for k in bin(input)[2:]]
    for i in range(len(outputsA)):
        if outputsA[i] != fix_output(iB, padding)[i]:
            return False
        return True


pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
pause = True
inGame = False
running = True

levels = [Level(2, 1, all_gates[3], "CREATE  NAND", "PASS"),
          Level(2, 1, all_gates[4], "CREATE  OR", "PASS"),
          Level(2, 1, all_gates[5], "CREATE  EXOR", "PASS"),
          Level(3, 2, all_gates[6], "CREATE  HALF ADDER", "PASS"),
          Level(9, 5, all_gates[7], "CREATE  FULL ADDER", "PASS")]
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



n = Node(50, 450, 50)

toolbox = ToolBox(100)

game = MenuManager()

levelNum = 0

testInput = 0
testOutputs = []
haveGate = False
haveNode = False
levelNode = False
draw_toolbox = False
drawTruthTable = False
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
            startGameNode.setValue(0)
            mainMenuNode.setValue(0)
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                drawTruthTable = not drawTruthTable
            if event.type == pygame.MOUSEBUTTONDOWN:
                if draw_toolbox:
                    grabbedGate = getGrabbedGate(toolbox.getTools(), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    if grabbedGate != None:
                        chosen_one = toolbox.createGate(grabbedGate)
                        chosen_one.setPos(WINDOW_WIDTH//2-chosen_one.getWidth()//2, WINDOW_HEIGHT//2-chosen_one.getHeight()//2)
                        levels[levelNum].addGate(chosen_one)
                        draw_toolbox = False
                        break
                for button in game.getGameButtons():
                    if button.isMouseInside():
                        testInput = 0
                        testOutputs = []
                        button.getFunction()()
                        break
                grabbedNode = getGrabbedNode(levels[levelNum].getInputs(), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                if grabbedNode != None:
                    levelNode = True
                if not levelNode:
                    for gate in levels[levelNum].getGates():
                        grabbedNode = getGrabbedNode(gate.getOutputs(), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                        if grabbedNode != None:
                            haveNode = True
                            break
                if (not haveNode) and (not levelNode):
                    grabbedGate = getGrabbedGate(levels[levelNum].getGates(), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    if grabbedGate != None:
                        haveGate = True
            if event.type == pygame.MOUSEBUTTONUP:
                if levelNode:
                    if getGrabbedNode(levels[levelNum].getInputs(), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]) == grabbedNode:
                        grabbedNode.setValue(1 - grabbedNode.getValue())
                        grabbedNode = None
                        levelNode = False
                    else:
                        haveNode = True
                        levelNode = False
                if haveNode:
                    destNode = getGrabbedNode(levels[levelNum].getOutputs(), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    if destNode != None:
                        destNode.setPrevNode(grabbedNode)
                        haveNode = False
                    if haveNode:
                        for gate in levels[levelNum].getGates():
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
        try:
            if grabbedNode != None:
                drawGrabbedNode(screen, grabbedNode)
        except:
            pass
        for button in game.getGameButtons():
            button.draw(screen)
        for i in range(len(levels[levelNum].getInputs())):
            levels[levelNum].getInputs()[i].draw(screen)
        for i in range(len(levels[levelNum].getOutputs())):
            levels[levelNum].getOutputs()[i].setValue(levels[levelNum].getOutputs()[i].getPrevNodeValue())
            levels[levelNum].getOutputs()[i].draw(screen)
        for i in range(len(levels[levelNum].getGates()) - 1, -1, -1):
            levels[levelNum].getGates()[i].evaluate()
            levels[levelNum].getGates()[i].draw(screen)  
        text = pygame.font.SysFont("adobegothicstdkalin", 100).render(levels[levelNum].getTitle(), False, pygame.Color("#3BBA9C"))
        text2 = pygame.font.SysFont("adobegothicstdkalin", 100).render(levels[levelNum].getTitle(), False, "black")
        screen.blit(text2, (((1600-text.get_size()[0])//2)+7,50+7))
        screen.blit(text, ((1600-text.get_size()[0])//2,50))      
        # if drawTruthTable:
        #     screen.fill((pygame.Color("#43455C")))
        #     for i in range(len(levels[levelNum].makeTruthTable())):
        #         text = pygame.font.SysFont("adobegothicstdkalin", 70).render(levels[levelNum].makeTruthTable()[i], False, pygame.Color("#3BBA9C"))
        #         screen.blit(text, ((1600-text.get_size()[0])//2,(450 + (50 * (i - len(levels[levelNum].makeTruthTable())//2)))))
        if draw_toolbox:
            toolbox.draw(screen, (levelNum + 2))

        clock.tick(144)
        pygame.display.flip()
        #========================================= End Game Loop

    #============================================= Start Level Test
    while game.getMenuVars().getLevelTest():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.quitGame()

        screen.fill("tan")

        if(testInput > 2**(len(levels[levelNum].getInputs())) - 1):
            game.getMenuVars().setLevelTest(False)
            game.getMenuVars().setGame(True)
            testInput = 0
            levels[levelNum].setInputs(0)
            if levelNum < 3:
                passLevel = compareOutputs(testOutputs, all_gates[levelNum + 2])
            if passLevel :
                levelNum += 1
                testOutputs = []

        levels[levelNum].setInputs(testInput)
        testInput += 1

        for i in range(len(levels[levelNum].getGates()) - 1, -1, -1):
            levels[levelNum].getGates()[i].evaluate()
            for j in range(len(levels[levelNum].getGates())):
                levels[levelNum].getGates()[j].evaluate()
            levels[levelNum].getGates()[i].draw(screen)
        for i in range(len(levels[levelNum].getInputs())):
            levels[levelNum].getInputs()[i].draw(screen)
        for i in range(len(levels[levelNum].getOutputs())):
            levels[levelNum].getOutputs()[i].setValue(levels[levelNum].getOutputs()[i].getPrevNodeValue())
            levels[levelNum].getOutputs()[i].draw(screen)

        testOutputs.append(levels[levelNum].getOutputValues())

        if(levelNum >= 3):
                passLevel = compareAdderOutputs(levels[levelNum].getOutputValues(),2, sum(levels[levelNum].getInputValues()))
                if not passLevel:
                    game.getMenuVars().setLevelTest(False)
                    game.getMenuVars().setGame(True)
                    testInput = 0


        clock.tick(1)
        pygame.display.flip()
        

pygame.quit()