from node import *
 
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900

class Level:
    def __init__(self, numInputs, numOutputs, directions, title, pastLevel):
        self.gates = []
        self.directions = directions
        self.title = title
        self.pastLevel = pastLevel 
        self.inputs = [Node(50, (WINDOW_HEIGHT/(numInputs+1)*(i+1)), 30) for i in range(numInputs)]
        self.outputs = [InputNode(WINDOW_WIDTH - 50, (WINDOW_HEIGHT/(numOutputs+1)*(i+1)), 30) for i in range(numOutputs)]

    def getTitle(self):
        return self.title

    def addGate(self, gate):
        self.gates.append(gate)

    def getGates(self):
        return self.gates
    
    def removeGate(self, gate):
        self.gates.remove(gate)

    def setInputs(self, input):
        inputBinStr = bin(input)[2:]
        while len(inputBinStr) < len(self.inputs):
            inputBinStr = "0" + inputBinStr
        for i in range(len(self.inputs)):
            self.inputs[i].setValue(int(inputBinStr[i]))

    def getInputs(self):
        return self.inputs
    
    def getInputValues(self):
        out = []
        for o in self.inputs:
            out.append(o.getValue())
        return out

    def getOutputs(self):
        return self.outputs
    
    def getOutputValues(self):
        out = []
        for o in self.outputs:
            out.append(o.getValue())
        return out

    def makeTruthTable(self):
        outputList = []
        output = ""
        for i in range (len(self.inputs)):
            output += "i" + str(i) + " "
        output += " | "
        for i in range (len(self.outputs)):
            output += "o" + str(i) + " "
        outputList.append(output) 
        output = ""
        output += '-'*(len(self.inputs)*3+len(self.outputs)*3+3)
        outputList.append(output) 
        output = ""
        for i in range (len(self.directions)):
            binaryVal = bin(i)[2:]
            binaryVal = [str(c) for c in binaryVal]
            while len(binaryVal) < len(self.inputs):
                binaryVal.insert(0, "0")  
            for j in binaryVal:             
                output += j + "  "
            output += " | "
            for k in range(len(self.directions[i])):
                output += str(self.directions[len(self.directions) - (i + 1)][k])
            outputList.append(output) 
            output = "" 
        return outputList
     