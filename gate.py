
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
    
    def evaluate(self):
        index =  self.logic[ int( "".join( [str(i) for i in self.inputs] ), 2 ) ]
        print(index)

and_logic = [0, 0, "test", 1]


if __name__ == "__main__":
    g = Gate(1, 1, 1, 1, 2, 1, and_logic)
    g.setInput(1, 0)
    g.evaluate()