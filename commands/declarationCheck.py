from antlr4 import InputStream, CommonTokenStream

from rabbitLexer import rabbitLexer
from rabbitListener import rabbitListener
from rabbitParser import rabbitParser

def declarationCheck(line):
    line = line.strip()
    data = InputStream(line)
    # lexer
    lexer = rabbitLexer(data)
    stream = CommonTokenStream(lexer)
    # parser
    parser = rabbitParser(stream)
    listener = rabbitListener()
    parser.addParseListener(listener)
    try:
        _ = parser.prog()
    except Exception as err:
        print(err)
        exit()