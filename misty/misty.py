#!/usr/bin/env python3
"""Generate equations for the Montreal Imaging Stress Task."""
import random
import itertools


"""Equation generation tool.
This creates equation generating object.
Arguments include equation difficulty, number of integers,
and the number of operators.
Includes functions for:

    """

class MistSums(object):
    def __init__(self):
        """Initiate object."""
        self.int_qty = 0  # initial int qty is 0
        self.ops = 0  # initial op qty is 0
        self.equation=0
        self.ans=0
    
    def int_tool(self, diff):
        """Create a dictionary and fills it with integer values."""
        self.int_dic = []
        if diff == "easy1":
            integers = [9, 9]
            self.ops = ('+', '-')
        
        elif diff == "easy2":
            integers = [9, 9, 9]
            self.ops = ('+', '-')
        
        elif diff == "med1":
            integers = [9, 9, 9, 9]
            self.ops = ('+', '-', '*')
        
        elif diff == "med2":
            integers = [9, 9, 99, 99]
            random.shuffle(integers)
            self.ops = ('*', '-', '*')
        
        elif diff == "hard":
            integers = [99, 99, 99, 99]
            self.ops = ('+', '-', '/', '*')
        
        self.int_qty = len(integers)
        
        for i, val in enumerate(integers):
            num = range(1, integers[i])
            temp = float(random.choice(num))
            self.int_dic.append(temp)
        
    def opt_gen_tool(self):
        """Generate the necessary operators for the equation."""
        self.op_dic = []
        temp = 0
        for i in range(0, (self.int_qty-1)):
            temp = str(random.choice(self.ops))
            self.op_dic.append(temp)
    
    def eq_generator(self, diff):
        """Create equation."""
        while True:
            self.int_tool(diff)
            self.opt_gen_tool()
            self.equation = [
                x for x in itertools.chain.from_iterable(
                    itertools.zip_longest(
                        self.int_dic,
                        self.op_dic,
                        fillvalue=''))]
            self.equation = ' '.join(str(e) for e in self.equation)
            if ("/0" not in self.equation):
                self.ans = eval(self.equation)
                break
    
    def make_equation(self, diff):
        """Make an easy op."""
        if "last_eq" not in locals():
            last_eq = "world"
        
        while True:
            self.eq_generator(diff)
            if ((float(self.ans).is_integer()) and
                (int(self.ans) >= 0) and
                (int(self.ans) <= 9)) and last_eq != self.equation:
                self.equation = self.equation.replace('.0', '')
                self.ans = str(self.ans).replace('.0', '')
                last_ans = self.ans
                break
