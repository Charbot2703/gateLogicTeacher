from node import *
 
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900

class Level:
    def __init__(self, numInputs, numOutputs, directions, pastLevel):
        self.gates = []
        self.directions = directions
        self.pastLevel = pastLevel 
        self.inputs = [Node(50, (WINDOW_HEIGHT/(numInputs+1)*(i+1)), 30) for i in range(numInputs)]
        self.outputs = [InputNode(WINDOW_WIDTH - 50, (WINDOW_HEIGHT/(numOutputs+1)*(i+1)), 30) for i in range(numOutputs)]

    def addGate(self, gate):
        self.gates.append(gate)

    def getGates(self):
        return self.gates
    
    def getInputs(self):
        return self.inputs
    
    def getOutputs(self):
        return self.outputs

    def makeTruthTable(self):
        output = ""
        for i in range (len(self.inputs)):
            output += "i" + str(i) + " "
        output += " | "
        for i in range (len(self.outputs)):
            output += "o" + str(i) + " "
        output += "\n"  
        output += '-'*(len(self.inputs)*3+len(self.outputs)*3+3) + "\n"
        for i in range (len(self.directions)):
            binaryVal = bin(i)[2:]
            binaryVal = [str(c) for c in binaryVal]
            while len(binaryVal) < len(self.inputs):
                binaryVal.insert(0, "0")  
            for j in binaryVal:             
                output += j + "  "
            output += " | " + str(self.directions[i]) + "\n"  
        return output



     