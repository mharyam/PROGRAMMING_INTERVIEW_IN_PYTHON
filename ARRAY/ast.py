import re


class Compiler(object):

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()

    def compile(self, program):
        return self.pass3(self.pass2(self.pass1(program)))

    def tokenize(self, program):
        """Turn a program string into an array of tokens.  Each token
           is either '[', ']', '(', ')', '+', '-', '*', '/', a variable
           name or a number (as a string)"""
        token_iter = (m.group(0) for m in re.finditer(r'[-+*/()[\]]|[A-Za-z]+|\d+', program))
        return [int(tok) if tok.isdigit() else tok for tok in token_iter]

    def pass1(self, program):
        """Returns an un-optimized AST"""
        # tokens = self.tokenize(program)
        #
        # for char in tokens:
        #     if char == "(":
        #         self.push(char)
        #     elif char == ")":
        #         if stack.pop() == None:
        #             return False
        #
        # if stack.size() == 0:
        #     return True
        # else:
        #     return False
        pass

    def pass2(self, ast):
        """Returns an AST with constant expressions reduced"""
        pass

    def pass3(self, ast):
        """Returns assembly instructions"""
        pass


prog = '[ x y z ] ( 2*3*x + 5*y - 3*z ) / (1 + 3 + 2*2)'
prog2 = '[x y] (x + y) / 2'

c = Compiler()

print(c.tokenize(prog2))
print(type(c.tokenize(prog2)))

import re


class Compiler(object):

    def compile(self, program):
        return self.pass3(self.pass2(self.pass1(program)))

    def tokenize(self, program):
        """Turn a program string into an array of tokens.  Each token
           is either '[', ']', '(', ')', '+', '-', '*', '/', a variable
           name or a number (as a string)"""
        token_iter = (m.group(0) for m in re.finditer(r'[-+*/()[\]]|[A-Za-z]+|\d+', program))
        return [int(tok) if tok.isdigit() else tok for tok in token_iter]

    def pass1(self, program):
        """Returns an un-optimized AST"""
        tokens = self.tokenize(program)
        pass

    def pass2(self, ast):
        """Returns an AST with constant expressions reduced"""
        pass

    def pass3(self, ast):
        """Returns assembly instructions"""
        pass


import unittest
from preloaded import simulate
from solution import Compiler


class Test(unittest.TestCase):
    def test_basic_functionality(self):
        prog = '[ x y z ] ( 2*3*x + 5*y - 3*z ) / (1 + 3 + 2*2)';
        t1 = {'op': '/', 'a': {'op': '-', 'a': {'op': '+', 'a': {'op': '*', 'a': {'op': '*', 'a': {'op': 'imm', 'n': 2},
                                                                                  'b': {'op': 'imm', 'n': 3}},
                                                                 'b': {'op': 'arg', 'n': 0}},
                                                'b': {'op': '*', 'a': {'op': 'imm', 'n': 5},
                                                      'b': {'op': 'arg', 'n': 1}}},
                               'b': {'op': '*', 'a': {'op': 'imm', 'n': 3}, 'b': {'op': 'arg', 'n': 2}}},
              'b': {'op': '+', 'a': {'op': '+', 'a': {'op': 'imm', 'n': 1}, 'b': {'op': 'imm', 'n': 3}},
                    'b': {'op': '*', 'a': {'op': 'imm', 'n': 2}, 'b': {'op': 'imm', 'n': 2}}}};
        t2 = {'op': '/', 'a': {'op': '-', 'a': {'op': '+', 'a': {'op': '*', 'a': {'op': 'imm', 'n': 6},
                                                                 'b': {'op': 'arg', 'n': 0}},
                                                'b': {'op': '*', 'a': {'op': 'imm', 'n': 5},
                                                      'b': {'op': 'arg', 'n': 1}}},
                               'b': {'op': '*', 'a': {'op': 'imm', 'n': 3}, 'b': {'op': 'arg', 'n': 2}}},
              'b': {'op': 'imm', 'n': 8}};
        c = Compiler()
        self.assertTrue(c, 'Able to construct compiler')

        p1 = c.pass1(prog)
        self.assertEqual(p1, t1, 'Pass1')

        p2 = c.pass2(p1)
        self.assertEqual(p2, t2, 'Pass2')

        p3 = c.pass3(p2)
        self.assertEqual(simulate(p3, [4, 0, 0]), 3, 'prog(4,0,0) == 3')
        self.assertEqual(simulate(p3, [4, 8, 0]), 8, 'prog(4,8,0) == 8')
        self.assertEqual(simulate(p3, [4, 8, 16]), 2, 'prog(4,8,6) == 2')

        """
        You are writing a three-pass compiler for a simple programming language into a small assembly language.

The programming language has this syntax:

    function   ::= '[' arg-list ']' expression

    arg-list   ::= /* nothing */
                 | variable arg-list

    expression ::= term
                 | expression '+' term
                 | expression '-' term

    term       ::= factor
                 | term '*' factor
                 | term '/' factor

    factor     ::= number
                 | variable
                 | '(' expression ')'
Variables are strings of alphabetic characters. Numbers are strings of decimal digits representing integers. So, for example, a function which computes a2 + b2 might look like:

    [ a b ] a*a + b*b
A function which computes the average of two numbers might look like:

    [ first second ] (first + second) / 2
You need write a three-pass compiler. All test cases will be valid programs, so you needn't concentrate on error-handling.

The first pass will be the method pass1 which takes a string representing a function in the original programming language and will return a (JSON) object that represents that Abstract Syntax Tree. The Abstract Syntax Tree must use the following representations:

    { 'op': '+', 'a': a, 'b': b }    // add subtree a to subtree b
    { 'op': '-', 'a': a, 'b': b }    // subtract subtree b from subtree a
    { 'op': '*', 'a': a, 'b': b }    // multiply subtree a by subtree b
    { 'op': '/', 'a': a, 'b': b }    // divide subtree a from subtree b
    { 'op': 'arg', 'n': n }          // reference to n-th argument, n integer
    { 'op': 'imm', 'n': n }          // immediate value n, n integer
Note: arguments are indexed from zero. So, for example, the function
[ x y ] ( x + y ) / 2 would look like:

    { 'op': '/', 'a': { 'op': '+', 'a': { 'op': 'arg', 'n': 0 },
                                   'b': { 'op': 'arg', 'n': 1 } },
                 'b': { 'op': 'imm', 'n': 2 } }
The second pass of the compiler will be called pass2. This pass will take the output from pass1 and return a new Abstract Syntax Tree (with the same format) with all constant expressions reduced as much as possible. So, if for example, the function is [ x ] x + 2*5, the result of pass1 would be:

    { 'op': '+', 'a': { 'op': 'arg', 'n': 0 },
                 'b': { 'op': '*', 'a': { 'op': 'imm', 'n': 2 },
                                   'b': { 'op': 'imm', 'n': 5 } } }
This would be passed into pass2 which would return:

    { 'op': '+', 'a': { 'op': 'arg', 'n': 0 },
                 'b': { 'op': 'imm', 'n': 10 } }
The third pass of the compiler is pass3. The pass3 method takes in an Abstract Syntax Tree and returns an array of strings. Each string is an assembly directive. You are working on a small processor with two registers (R0 and R1), a stack, and an array of input arguments. The result of a function is expected to be in R0. The processor supports the following instructions:

    "IM n"     // load the constant value n into R0
    "AR n"     // load the n-th input argument into R0
    "SW"       // swap R0 and R1
    "PU"       // push R0 onto the stack
    "PO"       // pop the top value off of the stack into R0
    "AD"       // add R1 to R0 and put the result in R0
    "SU"       // subtract R1 from R0 and put the result in R0
    "MU"       // multiply R0 by R1 and put the result in R0
    "DI"       // divide R0 by R1 and put the result in R0
So, one possible return value from pass3 given the Abstract Syntax Tree shown above from pass2 is:

    [ "IM 10", "SW", "AR 0", "AD" ]
Here is a simulator for the target machine. It takes an array of assembly instructions and an array of arguments and returns the result.

def simulate(asm, argv):
    r0, r1 = None, None
    stack = []
    for ins in asm:
        if ins[:2] == 'IM' or ins[:2] == 'AR':
            ins, n = ins[:2], int(ins[2:])
        if ins == 'IM':   r0 = n
        elif ins == 'AR': r0 = argv[n]
        elif ins == 'SW': r0, r1 = r1, r0
        elif ins == 'PU': stack.append(r0)
        elif ins == 'PO': r0 = stack.pop()
        elif ins == 'AD': r0 += r1
        elif ins == 'SU': r0 -= r1
        elif ins == 'MU': r0 *= r1
        elif ins == 'DI': r0 /= r1
    return r0"""