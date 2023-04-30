
not_gate = [[1],
            [0]]

and_gate = [[0],
            [0],
            [0],
            [1]]

nand_gate = [[1],
             [1],
             [1],
             [0]]

or_gate = [[0],
           [1],
           [1],
           [1]]

exor_gate = [[0],
             [1],
             [1],
             [0]]

adder_gate = lambda args: [i for i in bin(args[0] + args[1] + args[2])[2:]]

four_bit_adder = [[0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 1, 1, 0],
                  [0, 1, 0, 0, 0],
                  [0, 1, 0, 1, 0],
                  [0, 1, 1, 0, 0],
                  [0, 1, 1, 1, 0],
                  [1, 0, 0, 0, 0],
                  [1, 0, 0, 1, 0],
                  [1, 0, 1, 0, 0],
                  [1, 0, 1, 1, 0],
                  [1, 1, 0, 0, 0],
                  [1, 1, 0, 1, 0],
                  [1, 1, 1, 0, 0],
                  [1, 1, 1, 1, 0],
                  [0, 0, 0, 0, 1],
                  [0, 0, 0, 1, 1],
                  [0, 0, 1, 0, 1],
                  [0, 0, 1, 1, 1],
                  [0, 1, 0, 0, 1],
                  [0, 1, 0, 1, 1],
                  [0, 1, 1, 0, 1],
                  [0, 1, 1, 1, 1],
                  [1, 0, 0, 0, 1],
                  [1, 0, 0, 1, 1],
                  [1, 0, 1, 0, 1],
                  [1, 0, 1, 1, 1],
                  [1, 1, 0, 0, 1],
                  [1, 1, 0, 1, 1],
                  [1, 1, 1, 0, 1],
                  [1, 1, 1, 1, 1]]


eight_bit_adder=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 1, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 1, 1, 1, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 0, 1, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1, 1, 0],
                 [0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 1, 1, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 0, 0, 1, 1, 0],
                 [0, 0, 0, 1, 0, 1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 1, 0, 1, 0],
                 [0, 0, 0, 1, 0, 1, 1, 0, 0],
                 [0, 0, 0, 1, 0, 1, 1, 1, 0],
                 [0, 0, 0, 1, 1, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 0, 0, 1, 0],
                 [0, 0, 0, 1, 1, 0, 1, 0, 0],
                 [0, 0, 0, 1, 1, 0, 1, 1, 0],
                 [0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 1, 1, 1, 0, 1, 0],
                 [0, 0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 0, 1, 1, 1, 1, 1, 0],
                 [0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 1, 0],
                 [0, 0, 1, 0, 0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 0, 1, 1, 0],
                 [0, 0, 1, 0, 0, 1, 0, 0, 0],
                 [0, 0, 1, 0, 0, 1, 0, 1, 0],
                 [0, 0, 1, 0, 0, 1, 1, 0, 0],
                 [0, 0, 1, 0, 0, 1, 1, 1, 0],
                 [0, 0, 1, 0, 1, 0, 0, 0, 0],
                 [0, 0, 1, 0, 1, 0, 0, 1, 0],
                 [0, 0, 1, 0, 1, 0, 1, 0, 0],
                 [0, 0, 1, 0, 1, 0, 1, 1, 0],
                 [0, 0, 1, 0, 1, 1, 0, 0, 0],
                 [0, 0, 1, 0, 1, 1, 0, 1, 0],
                 [0, 0, 1, 0, 1, 1, 1, 0, 0],
                 [0, 0, 1, 0, 1, 1, 1, 1, 0],
                 [0, 0, 1, 1, 0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 0, 0, 0, 1, 0],
                 [0, 0, 1, 1, 0, 0, 1, 0, 0],
                 [0, 0, 1, 1, 0, 0, 1, 1, 0],
                 [0, 0, 1, 1, 0, 1, 0, 0, 0],
                 [0, 0, 1, 1, 0, 1, 0, 1, 0],
                 [0, 0, 1, 1, 0, 1, 1, 0, 0],
                 [0, 0, 1, 1, 0, 1, 1, 1, 0],
                 [0, 0, 1, 1, 1, 0, 0, 0, 0],
                 [0, 0, 1, 1, 1, 0, 0, 1, 0],
                 [0, 0, 1, 1, 1, 0, 1, 0, 0],
                 [0, 0, 1, 1, 1, 0, 1, 1, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0, 0],
                 [0, 0, 1, 1, 1, 1, 0, 1, 0],
                 [0, 0, 1, 1, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 1, 1, 1, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [0, 1, 0, 0, 0, 0, 1, 0, 0],
                 [0, 1, 0, 0, 0, 0, 1, 1, 0],
                 [0, 1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 1, 0, 0, 0, 1, 0, 1, 0],
                 [0, 1, 0, 0, 0, 1, 1, 0, 0],
                 [0, 1, 0, 0, 0, 1, 1, 1, 0],
                 [0, 1, 0, 0, 1, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1, 0, 0, 1, 0],
                 [0, 1, 0, 0, 1, 0, 1, 0, 0],
                 [0, 1, 0, 0, 1, 0, 1, 1, 0],
                 [0, 1, 0, 0, 1, 1, 0, 0, 0],
                 [0, 1, 0, 0, 1, 1, 0, 1, 0],
                 [0, 1, 0, 0, 1, 1, 1, 0, 0],
                 [0, 1, 0, 0, 1, 1, 1, 1, 0],
                 [0, 1, 0, 1, 0, 0, 0, 0, 0],
                 [0, 1, 0, 1, 0, 0, 0, 1, 0],
                 [0, 1, 0, 1, 0, 0, 1, 0, 0],
                 [0, 1, 0, 1, 0, 0, 1, 1, 0],
                 [0, 1, 0, 1, 0, 1, 0, 0, 0],
                 [0, 1, 0, 1, 0, 1, 0, 1, 0],
                 [0, 1, 0, 1, 0, 1, 1, 0, 0],
                 [0, 1, 0, 1, 0, 1, 1, 1, 0],
                 [0, 1, 0, 1, 1, 0, 0, 0, 0],
                 [0, 1, 0, 1, 1, 0, 0, 1, 0],
                 [0, 1, 0, 1, 1, 0, 1, 0, 0],
                 [0, 1, 0, 1, 1, 0, 1, 1, 0],
                 [0, 1, 0, 1, 1, 1, 0, 0, 0],
                 [0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [0, 1, 0, 1, 1, 1, 1, 0, 0],
                 [0, 1, 0, 1, 1, 1, 1, 1, 0],
                 [0, 1, 1, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 0, 0, 0, 0, 1, 0],
                 [0, 1, 1, 0, 0, 0, 1, 0, 0],
                 [0, 1, 1, 0, 0, 0, 1, 1, 0],
                 [0, 1, 1, 0, 0, 1, 0, 0, 0],
                 [0, 1, 1, 0, 0, 1, 0, 1, 0],
                 [0, 1, 1, 0, 0, 1, 1, 0, 0],
                 [0, 1, 1, 0, 0, 1, 1, 1, 0],
                 [0, 1, 1, 0, 1, 0, 0, 0, 0],
                 [0, 1, 1, 0, 1, 0, 0, 1, 0],
                 [0, 1, 1, 0, 1, 0, 1, 0, 0],
                 [0, 1, 1, 0, 1, 0, 1, 1, 0],
                 [0, 1, 1, 0, 1, 1, 0, 0, 0],
                 [0, 1, 1, 0, 1, 1, 0, 1, 0],
                 [0, 1, 1, 0, 1, 1, 1, 0, 0],
                 [0, 1, 1, 0, 1, 1, 1, 1, 0],
                 [0, 1, 1, 1, 0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 0, 0, 0, 1, 0],
                 [0, 1, 1, 1, 0, 0, 1, 0, 0],
                 [0, 1, 1, 1, 0, 0, 1, 1, 0],
                 [0, 1, 1, 1, 0, 1, 0, 0, 0],
                 [0, 1, 1, 1, 0, 1, 0, 1, 0],
                 [0, 1, 1, 1, 0, 1, 1, 0, 0],
                 [0, 1, 1, 1, 0, 1, 1, 1, 0],
                 [0, 1, 1, 1, 1, 0, 0, 0, 0],
                 [0, 1, 1, 1, 1, 0, 0, 1, 0],
                 [0, 1, 1, 1, 1, 0, 1, 0, 0],
                 [0, 1, 1, 1, 1, 0, 1, 1, 0],
                 [0, 1, 1, 1, 1, 1, 0, 0, 0],
                 [0, 1, 1, 1, 1, 1, 0, 1, 0],
                 [0, 1, 1, 1, 1, 1, 1, 0, 0],
                 [0, 1, 1, 1, 1, 1, 1, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 1, 0, 0],
                 [1, 0, 0, 0, 0, 0, 1, 1, 0],
                 [1, 0, 0, 0, 0, 1, 0, 0, 0],
                 [1, 0, 0, 0, 0, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 1, 1, 0, 0],
                 [1, 0, 0, 0, 0, 1, 1, 1, 0],
                 [1, 0, 0, 0, 1, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0, 0, 1, 0],
                 [1, 0, 0, 0, 1, 0, 1, 0, 0],
                 [1, 0, 0, 0, 1, 0, 1, 1, 0],
                 [1, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 0, 0, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 1, 1, 1, 0, 0],
                 [1, 0, 0, 0, 1, 1, 1, 1, 0],
                 [1, 0, 0, 1, 0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 0, 0, 0, 1, 0],
                 [1, 0, 0, 1, 0, 0, 1, 0, 0],
                 [1, 0, 0, 1, 0, 0, 1, 1, 0],
                 [1, 0, 0, 1, 0, 1, 0, 0, 0],
                 [1, 0, 0, 1, 0, 1, 0, 1, 0],
                 [1, 0, 0, 1, 0, 1, 1, 0, 0],
                 [1, 0, 0, 1, 0, 1, 1, 1, 0],
                 [1, 0, 0, 1, 1, 0, 0, 0, 0],
                 [1, 0, 0, 1, 1, 0, 0, 1, 0],
                 [1, 0, 0, 1, 1, 0, 1, 0, 0],
                 [1, 0, 0, 1, 1, 0, 1, 1, 0],
                 [1, 0, 0, 1, 1, 1, 0, 0, 0],
                 [1, 0, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 1, 1, 1, 1, 0, 0],
                 [1, 0, 0, 1, 1, 1, 1, 1, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 0, 0, 1, 0, 0],
                 [1, 0, 1, 0, 0, 0, 1, 1, 0],
                 [1, 0, 1, 0, 0, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 1, 0, 1, 0],
                 [1, 0, 1, 0, 0, 1, 1, 0, 0],
                 [1, 0, 1, 0, 0, 1, 1, 1, 0],
                 [1, 0, 1, 0, 1, 0, 0, 0, 0],
                 [1, 0, 1, 0, 1, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 0, 1, 0, 0],
                 [1, 0, 1, 0, 1, 0, 1, 1, 0],
                 [1, 0, 1, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 1, 1, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 0],
                 [1, 0, 1, 0, 1, 1, 1, 1, 0],
                 [1, 0, 1, 1, 0, 0, 0, 0, 0],
                 [1, 0, 1, 1, 0, 0, 0, 1, 0],
                 [1, 0, 1, 1, 0, 0, 1, 0, 0],
                 [1, 0, 1, 1, 0, 0, 1, 1, 0],
                 [1, 0, 1, 1, 0, 1, 0, 0, 0],
                 [1, 0, 1, 1, 0, 1, 0, 1, 0],
                 [1, 0, 1, 1, 0, 1, 1, 0, 0],
                 [1, 0, 1, 1, 0, 1, 1, 1, 0],
                 [1, 0, 1, 1, 1, 0, 0, 0, 0],
                 [1, 0, 1, 1, 1, 0, 0, 1, 0],
                 [1, 0, 1, 1, 1, 0, 1, 0, 0],
                 [1, 0, 1, 1, 1, 0, 1, 1, 0],
                 [1, 0, 1, 1, 1, 1, 0, 0, 0],
                 [1, 0, 1, 1, 1, 1, 0, 1, 0],
                 [1, 0, 1, 1, 1, 1, 1, 0, 0],
                 [1, 0, 1, 1, 1, 1, 1, 1, 0],
                 [1, 1, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 1, 0, 0, 0, 0, 1, 0, 0],
                 [1, 1, 0, 0, 0, 0, 1, 1, 0],
                 [1, 1, 0, 0, 0, 1, 0, 0, 0],
                 [1, 1, 0, 0, 0, 1, 0, 1, 0],
                 [1, 1, 0, 0, 0, 1, 1, 0, 0],
                 [1, 1, 0, 0, 0, 1, 1, 1, 0],
                 [1, 1, 0, 0, 1, 0, 0, 0, 0],
                 [1, 1, 0, 0, 1, 0, 0, 1, 0],
                 [1, 1, 0, 0, 1, 0, 1, 0, 0],
                 [1, 1, 0, 0, 1, 0, 1, 1, 0],
                 [1, 1, 0, 0, 1, 1, 0, 0, 0],
                 [1, 1, 0, 0, 1, 1, 0, 1, 0],
                 [1, 1, 0, 0, 1, 1, 1, 0, 0],
                 [1, 1, 0, 0, 1, 1, 1, 1, 0],
                 [1, 1, 0, 1, 0, 0, 0, 0, 0],
                 [1, 1, 0, 1, 0, 0, 0, 1, 0],
                 [1, 1, 0, 1, 0, 0, 1, 0, 0],
                 [1, 1, 0, 1, 0, 0, 1, 1, 0],
                 [1, 1, 0, 1, 0, 1, 0, 0, 0],
                 [1, 1, 0, 1, 0, 1, 0, 1, 0],
                 [1, 1, 0, 1, 0, 1, 1, 0, 0],
                 [1, 1, 0, 1, 0, 1, 1, 1, 0],
                 [1, 1, 0, 1, 1, 0, 0, 0, 0],
                 [1, 1, 0, 1, 1, 0, 0, 1, 0],
                 [1, 1, 0, 1, 1, 0, 1, 0, 0],
                 [1, 1, 0, 1, 1, 0, 1, 1, 0],
                 [1, 1, 0, 1, 1, 1, 0, 0, 0],
                 [1, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 1, 0, 1, 1, 1, 1, 0, 0],
                 [1, 1, 0, 1, 1, 1, 1, 1, 0],
                 [1, 1, 1, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 0, 0, 0, 0, 1, 0],
                 [1, 1, 1, 0, 0, 0, 1, 0, 0],
                 [1, 1, 1, 0, 0, 0, 1, 1, 0],
                 [1, 1, 1, 0, 0, 1, 0, 0, 0],
                 [1, 1, 1, 0, 0, 1, 0, 1, 0],
                 [1, 1, 1, 0, 0, 1, 1, 0, 0],
                 [1, 1, 1, 0, 0, 1, 1, 1, 0],
                 [1, 1, 1, 0, 1, 0, 0, 0, 0],
                 [1, 1, 1, 0, 1, 0, 0, 1, 0],
                 [1, 1, 1, 0, 1, 0, 1, 0, 0],
                 [1, 1, 1, 0, 1, 0, 1, 1, 0],
                 [1, 1, 1, 0, 1, 1, 0, 0, 0],
                 [1, 1, 1, 0, 1, 1, 0, 1, 0],
                 [1, 1, 1, 0, 1, 1, 1, 0, 0],
                 [1, 1, 1, 0, 1, 1, 1, 1, 0],
                 [1, 1, 1, 1, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 0, 0, 0, 1, 0],
                 [1, 1, 1, 1, 0, 0, 1, 0, 0],
                 [1, 1, 1, 1, 0, 0, 1, 1, 0],
                 [1, 1, 1, 1, 0, 1, 0, 0, 0],
                 [1, 1, 1, 1, 0, 1, 0, 1, 0],
                 [1, 1, 1, 1, 0, 1, 1, 0, 0],
                 [1, 1, 1, 1, 0, 1, 1, 1, 0],
                 [1, 1, 1, 1, 1, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 0, 0, 1, 0],
                 [1, 1, 1, 1, 1, 0, 1, 0, 0],
                 [1, 1, 1, 1, 1, 0, 1, 1, 0],
                 [1, 1, 1, 1, 1, 1, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 0, 1, 0],
                 [1, 1, 1, 1, 1, 1, 1, 0, 0],
                 [1, 1, 1, 1, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1],
                 [0, 0, 0, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 0, 0, 0, 1, 1, 1],
                 [0, 0, 0, 0, 0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0, 1, 0, 1, 1],
                 [0, 0, 0, 0, 0, 1, 1, 0, 1],
                 [0, 0, 0, 0, 0, 1, 1, 1, 1],
                 [0, 0, 0, 0, 1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 1, 0, 0, 1, 1],
                 [0, 0, 0, 0, 1, 0, 1, 0, 1],
                 [0, 0, 0, 0, 1, 0, 1, 1, 1],
                 [0, 0, 0, 0, 1, 1, 0, 0, 1],
                 [0, 0, 0, 0, 1, 1, 0, 1, 1],
                 [0, 0, 0, 0, 1, 1, 1, 1, 1],
                 [0, 0, 0, 1, 0, 0, 0, 0, 1],
                 [0, 0, 0, 1, 0, 0, 0, 1, 1],
                 [0, 0, 0, 1, 0, 0, 1, 0, 1],
                 [0, 0, 0, 1, 0, 0, 1, 1, 1],
                 [0, 0, 0, 1, 0, 1, 0, 0, 1],
                 [0, 0, 0, 1, 0, 1, 0, 1, 1],
                 [0, 0, 0, 1, 0, 1, 1, 0, 1],
                 [0, 0, 0, 1, 0, 1, 1, 1, 1],
                 [0, 0, 0, 1, 1, 0, 0, 0, 1],
                 [0, 0, 0, 1, 1, 0, 0, 1, 1],
                 [0, 0, 0, 1, 1, 0, 1, 0, 1],
                 [0, 0, 0, 1, 1, 0, 1, 1, 1],
                 [0, 0, 0, 1, 1, 1, 0, 0, 1],
                 [0, 0, 0, 1, 1, 1, 0, 1, 1],
                 [0, 0, 0, 1, 1, 1, 1, 0, 1],
                 [0, 0, 0, 1, 1, 1, 1, 1, 1],
                 [0, 0, 1, 0, 0, 0, 0, 0, 1],
                 [0, 0, 1, 0, 0, 0, 0, 1, 1],
                 [0, 0, 1, 0, 0, 0, 1, 0, 1],
                 [0, 0, 1, 0, 0, 0, 1, 1, 1],
                 [0, 0, 1, 0, 0, 1, 0, 0, 1],
                 [0, 0, 1, 0, 0, 1, 0, 1, 1],
                 [0, 0, 1, 0, 0, 1, 1, 0, 1],
                 [0, 0, 1, 0, 0, 1, 1, 1, 1],
                 [0, 0, 1, 0, 1, 0, 0, 0, 1],
                 [0, 0, 1, 0, 1, 0, 0, 1, 1],
                 [0, 0, 1, 0, 1, 0, 1, 0, 1],
                 [0, 0, 1, 0, 1, 0, 1, 1, 1],
                 [0, 0, 1, 0, 1, 1, 0, 0, 1],
                 [0, 0, 1, 0, 1, 1, 0, 1, 1],
                 [0, 0, 1, 0, 1, 1, 1, 0, 1],
                 [0, 0, 1, 0, 1, 1, 1, 1, 1],
                 [0, 0, 1, 1, 0, 0, 0, 0, 1],
                 [0, 0, 1, 1, 0, 0, 0, 1, 1],
                 [0, 0, 1, 1, 0, 0, 1, 0, 1],
                 [0, 0, 1, 1, 0, 0, 1, 1, 1],
                 [0, 0, 1, 1, 0, 1, 0, 0, 1],
                 [0, 0, 1, 1, 0, 1, 0, 1, 1],
                 [0, 0, 1, 1, 0, 1, 1, 0, 1],
                 [0, 0, 1, 1, 0, 1, 1, 1, 1],
                 [0, 0, 1, 1, 1, 0, 0, 0, 1],
                 [0, 0, 1, 1, 1, 0, 0, 1, 1],
                 [0, 0, 1, 1, 1, 0, 1, 0, 1],
                 [0, 0, 1, 1, 1, 0, 1, 1, 1],
                 [0, 0, 1, 1, 1, 1, 0, 0, 1],
                 [0, 0, 1, 1, 1, 1, 0, 1, 1],
                 [0, 0, 1, 1, 1, 1, 1, 0, 1],
                 [0, 0, 1, 1, 1, 1, 1, 1, 1],
                 [0, 1, 0, 0, 0, 0, 0, 0, 1],
                 [0, 1, 0, 0, 0, 0, 0, 1, 1],
                 [0, 1, 0, 0, 0, 0, 1, 0, 1],
                 [0, 1, 0, 0, 0, 0, 1, 1, 1],
                 [0, 1, 0, 0, 0, 1, 0, 0, 1],
                 [0, 1, 0, 0, 0, 1, 0, 1, 1],
                 [0, 1, 0, 0, 0, 1, 1, 0, 1],
                 [0, 1, 0, 0, 0, 1, 1, 1, 1],
                 [0, 1, 0, 0, 1, 0, 0, 0, 1],
                 [0, 1, 0, 0, 1, 0, 0, 1, 1],
                 [0, 1, 0, 0, 1, 0, 1, 0, 1],
                 [0, 1, 0, 0, 1, 0, 1, 1, 1],
                 [0, 1, 0, 0, 1, 1, 0, 0, 1],
                 [0, 1, 0, 0, 1, 1, 0, 1, 1],
                 [0, 1, 0, 0, 1, 1, 1, 0, 1],
                 [0, 1, 0, 0, 1, 1, 1, 1, 1],
                 [0, 1, 0, 1, 0, 0, 0, 0, 1],
                 [0, 1, 0, 1, 0, 0, 0, 1, 1],
                 [0, 1, 0, 1, 0, 0, 1, 0, 1],
                 [0, 1, 0, 1, 0, 0, 1, 1, 1],
                 [0, 1, 0, 1, 0, 1, 0, 0, 1],
                 [0, 1, 0, 1, 0, 1, 0, 1, 1],
                 [0, 1, 0, 1, 0, 1, 1, 0, 1],
                 [0, 1, 0, 1, 0, 1, 1, 1, 1],
                 [0, 1, 0, 1, 1, 0, 0, 0, 1],
                 [0, 1, 0, 1, 1, 0, 0, 1, 1],
                 [0, 1, 0, 1, 1, 0, 1, 0, 1],
                 [0, 1, 0, 1, 1, 0, 1, 1, 1],
                 [0, 1, 0, 1, 1, 1, 0, 0, 1],
                 [0, 1, 0, 1, 1, 1, 0, 1, 1],
                 [0, 1, 0, 1, 1, 1, 1, 0, 1],
                 [0, 1, 0, 1, 1, 1, 1, 1, 1],
                 [0, 1, 1, 0, 0, 0, 0, 0, 1],
                 [0, 1, 1, 0, 0, 0, 0, 1, 1],
                 [0, 1, 1, 0, 0, 0, 1, 0, 1],
                 [0, 1, 1, 0, 0, 0, 1, 1, 1],
                 [0, 1, 1, 0, 0, 1, 0, 0, 1],
                 [0, 1, 1, 0, 0, 1, 0, 1, 1],
                 [0, 1, 1, 0, 0, 1, 1, 0, 1],
                 [0, 1, 1, 0, 0, 1, 1, 1, 1],
                 [0, 1, 1, 0, 1, 0, 0, 0, 1],
                 [0, 1, 1, 0, 1, 0, 0, 1, 1],
                 [0, 1, 1, 0, 1, 0, 1, 0, 1],
                 [0, 1, 1, 0, 1, 0, 1, 1, 1],
                 [0, 1, 1, 0, 1, 1, 0, 0, 1],
                 [0, 1, 1, 0, 1, 1, 0, 1, 1],
                 [0, 1, 1, 0, 1, 1, 1, 0, 1],
                 [0, 1, 1, 0, 1, 1, 1, 1, 1],
                 [0, 1, 1, 1, 0, 0, 0, 0, 1],
                 [0, 1, 1, 1, 0, 0, 0, 1, 1],
                 [0, 1, 1, 1, 0, 0, 1, 0, 1],
                 [0, 1, 1, 1, 0, 0, 1, 1, 1],
                 [0, 1, 1, 1, 0, 1, 0, 0, 1],
                 [0, 1, 1, 1, 0, 1, 0, 1, 1],
                 [0, 1, 1, 1, 0, 1, 1, 0, 1],
                 [0, 1, 1, 1, 0, 1, 1, 1, 1],
                 [0, 1, 1, 1, 1, 0, 0, 0, 1],
                 [0, 1, 1, 1, 1, 0, 0, 1, 1],
                 [0, 1, 1, 1, 1, 0, 1, 0, 1],
                 [0, 1, 1, 1, 1, 0, 1, 1, 1],
                 [0, 1, 1, 1, 1, 1, 0, 0, 1],
                 [0, 1, 1, 1, 1, 1, 0, 1, 1],
                 [0, 1, 1, 1, 1, 1, 1, 0, 1],
                 [0, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 1, 1],
                 [1, 0, 0, 0, 0, 0, 1, 0, 1],
                 [1, 0, 0, 0, 0, 0, 1, 1, 1],
                 [1, 0, 0, 0, 0, 1, 0, 0, 1],
                 [1, 0, 0, 0, 0, 1, 0, 1, 1],
                 [1, 0, 0, 0, 0, 1, 1, 0, 1],
                 [1, 0, 0, 0, 0, 1, 1, 1, 1],
                 [1, 0, 0, 0, 1, 0, 0, 0, 1],
                 [1, 0, 0, 0, 1, 0, 0, 1, 1],
                 [1, 0, 0, 0, 1, 0, 1, 0, 1],
                 [1, 0, 0, 0, 1, 0, 1, 1, 1],
                 [1, 0, 0, 0, 1, 1, 0, 0, 1],
                 [1, 0, 0, 0, 1, 1, 0, 1, 1],
                 [1, 0, 0, 0, 1, 1, 1, 0, 1],
                 [1, 0, 0, 0, 1, 1, 1, 1, 1],
                 [1, 0, 0, 1, 0, 0, 0, 0, 1],
                 [1, 0, 0, 1, 0, 0, 0, 1, 1],
                 [1, 0, 0, 1, 0, 0, 1, 0, 1],
                 [1, 0, 0, 1, 0, 0, 1, 1, 1],
                 [1, 0, 0, 1, 0, 1, 0, 0, 1],
                 [1, 0, 0, 1, 0, 1, 0, 1, 1],
                 [1, 0, 0, 1, 0, 1, 1, 0, 1],
                 [1, 0, 0, 1, 0, 1, 1, 1, 1],
                 [1, 0, 0, 1, 1, 0, 0, 0, 1],
                 [1, 0, 0, 1, 1, 0, 0, 1, 1],
                 [1, 0, 0, 1, 1, 0, 1, 0, 1],
                 [1, 0, 0, 1, 1, 0, 1, 1, 1],
                 [1, 0, 0, 1, 1, 1, 0, 0, 1],
                 [1, 0, 0, 1, 1, 1, 0, 1, 1],
                 [1, 0, 0, 1, 1, 1, 1, 0, 1],
                 [1, 0, 0, 1, 1, 1, 1, 1, 1],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1],
                 [1, 0, 1, 0, 0, 0, 0, 1, 1],
                 [1, 0, 1, 0, 0, 0, 1, 0, 1],
                 [1, 0, 1, 0, 0, 0, 1, 1, 1],
                 [1, 0, 1, 0, 0, 1, 0, 0, 1],
                 [1, 0, 1, 0, 0, 1, 0, 1, 1],
                 [1, 0, 1, 0, 0, 1, 1, 0, 1],
                 [1, 0, 1, 0, 0, 1, 1, 1, 1],
                 [1, 0, 1, 0, 1, 0, 0, 0, 1],
                 [1, 0, 1, 0, 1, 0, 0, 1, 1],
                 [1, 0, 1, 0, 1, 0, 1, 0, 1],
                 [1, 0, 1, 0, 1, 0, 1, 1, 1],
                 [1, 0, 1, 0, 1, 1, 0, 0, 1],
                 [1, 0, 1, 0, 1, 1, 0, 1, 1],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1],
                 [1, 0, 1, 0, 1, 1, 1, 1, 1],
                 [1, 0, 1, 1, 0, 0, 0, 0, 1],
                 [1, 0, 1, 1, 0, 0, 0, 1, 1],
                 [1, 0, 1, 1, 0, 0, 1, 0, 1],
                 [1, 0, 1, 1, 0, 0, 1, 1, 1],
                 [1, 0, 1, 1, 0, 1, 0, 0, 1],
                 [1, 0, 1, 1, 0, 1, 0, 1, 1],
                 [1, 0, 1, 1, 0, 1, 1, 0, 1],
                 [1, 0, 1, 1, 0, 1, 1, 1, 1],
                 [1, 0, 1, 1, 1, 0, 0, 0, 1],
                 [1, 0, 1, 1, 1, 0, 0, 1, 1],
                 [1, 0, 1, 1, 1, 0, 1, 0, 1],
                 [1, 0, 1, 1, 1, 0, 1, 1, 1],
                 [1, 0, 1, 1, 1, 1, 0, 0, 1],
                 [1, 0, 1, 1, 1, 1, 0, 1, 1],
                 [1, 0, 1, 1, 1, 1, 1, 0, 1],
                 [1, 0, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 0, 0, 0, 0, 0, 1, 1],
                 [1, 1, 0, 0, 0, 0, 1, 0, 1],
                 [1, 1, 0, 0, 0, 0, 1, 1, 1],
                 [1, 1, 0, 0, 0, 1, 0, 0, 1],
                 [1, 1, 0, 0, 0, 1, 0, 1, 1],
                 [1, 1, 0, 0, 0, 1, 1, 0, 1],
                 [1, 1, 0, 0, 0, 1, 1, 1, 1],
                 [1, 1, 0, 0, 1, 0, 0, 0, 1],
                 [1, 1, 0, 0, 1, 0, 0, 1, 1],
                 [1, 1, 0, 0, 1, 0, 1, 0, 1],
                 [1, 1, 0, 0, 1, 0, 1, 1, 1],
                 [1, 1, 0, 0, 1, 1, 0, 0, 1],
                 [1, 1, 0, 0, 1, 1, 0, 1, 1],
                 [1, 1, 0, 0, 1, 1, 1, 0, 1],
                 [1, 1, 0, 0, 1, 1, 1, 1, 1],
                 [1, 1, 0, 1, 0, 0, 0, 0, 1],
                 [1, 1, 0, 1, 0, 0, 0, 1, 1],
                 [1, 1, 0, 1, 0, 0, 1, 0, 1],
                 [1, 1, 0, 1, 0, 0, 1, 1, 1],
                 [1, 1, 0, 1, 0, 1, 0, 0, 1],
                 [1, 1, 0, 1, 0, 1, 0, 1, 1],
                 [1, 1, 0, 1, 0, 1, 1, 0, 1],
                 [1, 1, 0, 1, 0, 1, 1, 1, 1],
                 [1, 1, 0, 1, 1, 0, 0, 0, 1],
                 [1, 1, 0, 1, 1, 0, 0, 1, 1],
                 [1, 1, 0, 1, 1, 0, 1, 0, 1],
                 [1, 1, 0, 1, 1, 0, 1, 1, 1],
                 [1, 1, 0, 1, 1, 1, 0, 0, 1],
                 [1, 1, 0, 1, 1, 1, 0, 1, 1],
                 [1, 1, 0, 1, 1, 1, 1, 0, 1],
                 [1, 1, 0, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 0, 0, 0, 0, 1, 1],
                 [1, 1, 1, 0, 0, 0, 1, 0, 1],
                 [1, 1, 1, 0, 0, 0, 1, 1, 1],
                 [1, 1, 1, 0, 0, 1, 0, 0, 1],
                 [1, 1, 1, 0, 0, 1, 0, 1, 1],
                 [1, 1, 1, 0, 0, 1, 1, 0, 1],
                 [1, 1, 1, 0, 0, 1, 1, 1, 1],
                 [1, 1, 1, 0, 1, 0, 0, 0, 1],
                 [1, 1, 1, 0, 1, 0, 0, 1, 1],
                 [1, 1, 1, 0, 1, 0, 1, 0, 1],
                 [1, 1, 1, 0, 1, 0, 1, 1, 1],
                 [1, 1, 1, 0, 1, 1, 0, 0, 1],
                 [1, 1, 1, 0, 1, 1, 0, 1, 1],
                 [1, 1, 1, 0, 1, 1, 1, 0, 1],
                 [1, 1, 1, 0, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 0, 0, 0, 1, 1],
                 [1, 1, 1, 1, 0, 0, 1, 0, 1],
                 [1, 1, 1, 1, 0, 0, 1, 1, 1],
                 [1, 1, 1, 1, 0, 1, 0, 0, 1],
                 [1, 1, 1, 1, 0, 1, 0, 1, 1],
                 [1, 1, 1, 1, 0, 1, 1, 0, 1],
                 [1, 1, 1, 1, 0, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 0, 0, 1, 1],
                 [1, 1, 1, 1, 1, 0, 1, 0, 1],
                 [1, 1, 1, 1, 1, 0, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 0, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1],
                 
                 ]

all_gates = [not_gate, and_gate, nand_gate, or_gate, exor_gate, adder_gate, four_bit_adder, eight_bit_adder]