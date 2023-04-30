from button import Button
import pygame

class MenuVars:
    def __init__(self):
        self.main = True
        self.pause = False
        self.game = False
        self.running = True

    def setMain(self, val):
        self.main = val

    def getMain(self):
        return self.main
    
    def setPause(self, val):
        self.pause = val

    def getPause(self):
        return self.pause
    
    def setGame(self, val):
        self.game = val

    def getGame(self):
        return self.game
    
    def setRunning(self, val):
        self.running = val

    def getRunning(self):
        return self.running
    
class MenuManager:

    def __init__(self):
        self.menuVars = MenuVars()
        self.pauseMenuButtons = [Button(100, 100, "Resume", "aqua", self.resumeGame),
                            Button(100, 250, "Return to Main Menu", "orange", self.exitToMenu),
                            Button(100, 400, "Quit", "red", self.quitGame)]

        self.mainMenuButtons = [Button(200, 450 - 100 - 50, "Start Game", pygame.Color("#2ECC71"), self.do_nothing),
                            Button(200, 450 + 100, "Quit", pygame.Color("#C0392B"), self.quitGame)]
        
    def do_nothing(self):
        pass

    def getMenuVars(self):
        return self.menuVars

    def getPauseButtons(self):
        return self.pauseMenuButtons
    
    def getMainMenuButtons(self):
        return self.mainMenuButtons

    def startGame(self):
        self.menuVars.setMain(False)
        self.menuVars.setGame(True)

    def exitToMenu(self):
        self.menuVars.setMain(True)
        self.menuVars.setGame(False)
        self.menuVars.setPause(False)

    def pauseGame(self):
        self.menuVars.setGame(False)
        self.menuVars.setPause(True)

    def resumeGame(self):
        self.menuVars.setGame(True)
        self.menuVars.setPause(False)

    def quitGame(self):
        self.menuVars.setMain(False)
        self.menuVars.setGame(False)
        self.menuVars.setPause(False)
        self.menuVars.setRunning(False)
