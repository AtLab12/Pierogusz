from antlr4 import *
from PieroguszLexer import PieroguszLexer
from PieroguszParser import PieroguszParser
from LLVMActions import LLVMActions

def main():
    input_stream = FileStream("../test/part-2/loop.Pierogusz")
    lexer = PieroguszLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PieroguszParser(token_stream)

    tree = parser.prog()
    llvm_actions = LLVMActions()

    walker = ParseTreeWalker()
    walker.walk(llvm_actions, tree)

if __name__ == '__main__':
    main()