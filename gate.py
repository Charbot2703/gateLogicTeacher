
class Gate():
    def __init__(self, pos, size, color, text, num_of_inputs, num_of_outputs, logic):
        self.pos = pos
        self.size = size
        self.color = color
        self.text = text
        self.inputs = [0]*num_of_inputs
        self.outputs = [0]*num_of_outputs
        self.logic = logic

    def setInput(self, value, index):
        self.inputs[index] = value

    def setInputs(self, inputs):
        self.inputs = inputs
    
    def evaluate(self):
        output = self.logic[int("".join([str(i) for i in self.inputs]), 2)]
        self.outputs = output