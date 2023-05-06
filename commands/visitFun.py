from antlr4 import InputStream, CommonTokenStream
from rabbitLexer import rabbitLexer
from rabbitParser import rabbitParser


def visitFun(line, visitor):
    line = line.strip()
    data = InputStream(line)
    # lexer
    lexer = rabbitLexer(data)
    stream = CommonTokenStream(lexer)
    # parser
    parser = rabbitParser(stream)
    tree = parser.prog()
    # evaluator
    output = visitor.visit(tree)