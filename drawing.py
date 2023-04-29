import pygame

def inside(gate, x, y):
    return ((x >= gate.getX() and x < (gate.getX() + gate.getW())) and 
            (y >= gate.getY() and y < (gate.getY() + gate.getH())))

def getGrabbedGate(gates, mx, my):
    for gate in gates:
        if inside(gate, mx, my):
            return gate
    return None

pygame.init()
screen = pygame.display.set_mode((1600, 900))
clock = pygame.time.Clock()
running = True

l = None #Level(2, 1, "")

testGate = None #Gate(100, 200, 200, 300, 2, 3)

l.addGate(testGate)

haveGate = False
change = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            grabbedGate = getGrabbedGate(l.getGates(), pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            if grabbedGate != None:
                haveGate = True
        if event.type == pygame.MOUSEBUTTONUP:
            grabbedGate = None
            haveGate = False
    
    if haveGate:
        grabbedGate.setX(pygame.mouse.get_pos()[0] - (grabbedGate.getW()/2))
        grabbedGate.setY(pygame.mouse.get_pos()[1] - (grabbedGate.getH()/2))
        change = True

    if change:
        screen.fill("white")
        for gate in l.getGates():
            pygame.draw.rect(screen, (108, 204, 234), (gate.getX(), gate.getY(), gate.getW(), gate.getH()))
            for i in range(len(gate.getInputs())):
                pygame.draw.circle(screen, "black", (gate.getX(), gate.getY() + (25 * i) + 20), 10)
            for i in range(len(gate.getOutputs())):
                pygame.draw.circle(screen, "black", (gate.getX() + gate.getW(), gate.getY() + (25 * i) + 20), 10)

    clock.tick(144)
    pygame.display.flip()
    change = False

pygame.quit()