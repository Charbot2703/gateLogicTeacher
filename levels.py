class Level:
    def __init__(self, numInputs, numOutputs, directions, pastLevel):
        self.node_list = []
        self.directions = directions
        self.pastLevel = pastLevel 
        self.inputs = [0]*numInputs
        self.outputs = [0]*numOutputs

    def addNode(self, node):
        self.node_list.append(node)

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



     