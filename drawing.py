import pygame
from gate import Gate 
from levels import Level

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
running = True

l = Level(2, 1, [0, 1, 1, 0], "PASS")

#Gate((x, y), color, text, in, out, dirs)
testGate = Gate((100, 100), "orange", "TESTGATE", 2, 1, [0, 1, 1, 0])
testGate2 = Gate((300, 100), "blue", "ANOTHERGATE", 4, 3, [0, 1, 1, 0])

l.addGate(testGate)
l.addGate(testGate2)


for gate in l.getGates():
    gate.setX(gate.getX())
    gate.setY(gate.getY())

haveGate = False
haveNode = False
levelNode = False
change = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            grabbedNode = getGrabbedNode(l.getInputs(), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            if grabbedNode != None:
                levelNode = True
            if not levelNode:
                for gate in l.getGates():
                    grabbedNode = getGrabbedNode(gate.getInputs() + gate.getOutputs(), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    if grabbedNode != None:
                        haveNode = True
                        break
            if (not haveNode) and (not levelNode):
                grabbedGate = getGrabbedGate(l.getGates(), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                if grabbedGate != None:
                    haveGate = True
        if event.type == pygame.MOUSEBUTTONUP:
            if levelNode:
                grabbedNode.setValue(1 - grabbedNode.getValue())
                grabbedNode = None
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
            change = True
    
    if haveGate:
        grabbedGate.setX(pygame.mouse.get_pos()[0] - (grabbedGate.getWidth()/2))
        grabbedGate.setY(pygame.mouse.get_pos()[1] - (grabbedGate.getHeight()/2))
        change = True

    if change:
        screen.fill("white")
        for i in range(len(l.getInputs())):
            l.getInputs()[i].draw(screen)
        for i in range(len(l.getOutputs())):
            l.getOutputs()[i].draw(screen)
        for i in range(len(l.getGates()) - 1, -1, -1):
            l.getGates()[i].draw(screen)

    clock.tick(144)
    pygame.display.flip()
    change = False

pygame.quit()