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

class EquationTools(object):
    def __init__(self, diff, int_qty=0, ops=0):
        """Initiate object."""
        self.int_qty = int_qty  # Controls number of integers in equations
        self.ops = ops
    
    def int_tool(self, int_qty, diff):
        """Create a dictionary and fills it with integer values."""
        self.int_dic = []
        if diff == "med2":
            integers = [9, 9, 99, 99]
            random.shuffle(integers)
            self.ops = ('*', '-', '*')
    
        elif diff == "med1":
            integers = [9, 9, 9, 9]
            self.ops = ('+', '-', '*')
        
        elif diff == "easy1":
            integers = [9, 9]
            self.ops = ('+', '-')
        
        elif diff == "easy2":
            integers = [9, 9, 9]
            self.ops = ('+', '-')
        
        elif diff == "hard":
            integers = [99, 99, 99, 99]
            self.ops = ('+', '-', '/', '*')
        
        self.int_qty = len(integers)
    
        for i, val in enumerate(integers):
            num = range(1, integers[i])
            temp = float(random.choice(num))
            self.int_dic.append(temp)
    def opt_gen_tool(self, ops):
        """Generate the necessary operators for the equation."""
        self.op_dic = []
        temp = 0
        for i in range(0, (self.int_qty-1)):
            temp = str(random.choice(self.ops))
            self.op_dic.append(temp)
    
    def eq_generator(self, dict_list, opt_list):
        """Create equation."""
        while True:
            self.int_tool(self.int_qty, self.diff)
            self.equation = [
                x for x in itertools.chain.from_iterable(
                    itertools.zip_longest(
                        self.int_dic,
                        self.op_dic,
                        fillvalue=''))]
            self.equation = ' '.join(str(e) for e in self.equation)
            if ("/0" not in self.equation):
                break
            self.ans = eval(self.equation)


class MistSums(EquationTools):
    """Don't know what this does."""
    
    def __init__(
            self, ans=0, equation=0,
            diff="med",
            int_qty=0,
            op_qty=0,
            ops=0,
            dict_list=[],
            opt_list=[]):
        
        EquationTools.__init__(
            self,
            diff,
            int_qty,
            op_qty)
        
        self.equation = equation
        self.ans = ans
        self.diff = diff
        self.int_qty = int_qty
        self.ops = ops
    
    def EasyOps1(self):
        """Make an easy op."""
        
        while True:
            self.int_tool(self.int_qty, self.diff)
            self.opt_gen_tool(self.ops)
            self.eq_generator(self.int_dic, self.op_dic)
            if (
                    (
                        float(self.ans).is_integer()) and
                    (self.ans >= 0) and
                    (self.ans <= 9)):
                self.equation = self.equation.replace('.0', '')
                self.ans = str(self.ans).replace('.0', '')
                break


usrAvg = 0
msg = ""
eq = ""
corCount = 0
inCorCount = 0
meanRT = []
time = 10
totalCor = 0
difficulty = "easy1"
timeCoef = 1
