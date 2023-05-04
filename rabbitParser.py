# Generated from rabbit.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,49,205,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,77,8,1,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,99,8,4,1,5,
        1,5,5,5,103,8,5,10,5,12,5,106,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,124,8,6,1,7,1,7,1,7,1,7,1,
        7,1,8,1,8,1,8,1,8,3,8,135,8,8,1,8,3,8,138,8,8,1,9,1,9,1,10,1,10,
        1,11,1,11,1,11,1,11,3,11,148,8,11,1,12,1,12,1,12,1,13,1,13,1,13,
        1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,19,
        1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,23,1,23,1,24,
        1,24,1,25,1,25,1,25,1,25,1,25,3,25,188,8,25,1,26,1,26,1,26,1,26,
        3,26,194,8,26,1,26,1,26,1,26,1,26,3,26,200,8,26,1,26,3,26,203,8,
        26,1,26,0,0,27,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,0,5,1,0,46,47,1,0,18,21,1,0,32,39,1,0,
        40,41,1,0,42,43,211,0,54,1,0,0,0,2,76,1,0,0,0,4,78,1,0,0,0,6,80,
        1,0,0,0,8,98,1,0,0,0,10,100,1,0,0,0,12,123,1,0,0,0,14,125,1,0,0,
        0,16,137,1,0,0,0,18,139,1,0,0,0,20,141,1,0,0,0,22,147,1,0,0,0,24,
        149,1,0,0,0,26,152,1,0,0,0,28,155,1,0,0,0,30,157,1,0,0,0,32,159,
        1,0,0,0,34,161,1,0,0,0,36,163,1,0,0,0,38,165,1,0,0,0,40,170,1,0,
        0,0,42,173,1,0,0,0,44,176,1,0,0,0,46,178,1,0,0,0,48,180,1,0,0,0,
        50,187,1,0,0,0,52,202,1,0,0,0,54,55,3,2,1,0,55,1,1,0,0,0,56,77,3,
        42,21,0,57,77,3,38,19,0,58,77,3,44,22,0,59,77,3,24,12,0,60,77,3,
        26,13,0,61,77,3,14,7,0,62,77,3,12,6,0,63,77,3,18,9,0,64,77,3,20,
        10,0,65,77,3,36,18,0,66,77,3,34,17,0,67,77,3,32,16,0,68,77,3,30,
        15,0,69,77,3,28,14,0,70,77,3,22,11,0,71,77,3,40,20,0,72,77,3,8,4,
        0,73,77,3,40,20,0,74,77,3,6,3,0,75,77,3,4,2,0,76,56,1,0,0,0,76,57,
        1,0,0,0,76,58,1,0,0,0,76,59,1,0,0,0,76,60,1,0,0,0,76,61,1,0,0,0,
        76,62,1,0,0,0,76,63,1,0,0,0,76,64,1,0,0,0,76,65,1,0,0,0,76,66,1,
        0,0,0,76,67,1,0,0,0,76,68,1,0,0,0,76,69,1,0,0,0,76,70,1,0,0,0,76,
        71,1,0,0,0,76,72,1,0,0,0,76,73,1,0,0,0,76,74,1,0,0,0,76,75,1,0,0,
        0,77,3,1,0,0,0,78,79,5,1,0,0,79,5,1,0,0,0,80,81,5,2,0,0,81,82,3,
        52,26,0,82,7,1,0,0,0,83,84,5,3,0,0,84,85,3,48,24,0,85,86,5,4,0,0,
        86,87,3,52,26,0,87,99,1,0,0,0,88,89,5,5,0,0,89,90,3,48,24,0,90,91,
        5,4,0,0,91,92,7,0,0,0,92,99,1,0,0,0,93,94,5,5,0,0,94,95,3,48,24,
        0,95,96,5,4,0,0,96,97,3,16,8,0,97,99,1,0,0,0,98,83,1,0,0,0,98,88,
        1,0,0,0,98,93,1,0,0,0,99,9,1,0,0,0,100,104,5,6,0,0,101,103,3,2,1,
        0,102,101,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,
        0,105,107,1,0,0,0,106,104,1,0,0,0,107,108,5,7,0,0,108,11,1,0,0,0,
        109,110,5,8,0,0,110,111,3,16,8,0,111,112,5,9,0,0,112,113,3,10,5,
        0,113,114,5,10,0,0,114,124,1,0,0,0,115,116,5,8,0,0,116,117,3,16,
        8,0,117,118,5,9,0,0,118,119,3,10,5,0,119,120,5,11,0,0,120,121,3,
        10,5,0,121,122,5,10,0,0,122,124,1,0,0,0,123,109,1,0,0,0,123,115,
        1,0,0,0,124,13,1,0,0,0,125,126,5,12,0,0,126,127,3,52,26,0,127,128,
        3,10,5,0,128,129,5,13,0,0,129,15,1,0,0,0,130,131,3,52,26,0,131,134,
        3,46,23,0,132,135,3,52,26,0,133,135,3,16,8,0,134,132,1,0,0,0,134,
        133,1,0,0,0,135,138,1,0,0,0,136,138,3,52,26,0,137,130,1,0,0,0,137,
        136,1,0,0,0,138,17,1,0,0,0,139,140,5,14,0,0,140,19,1,0,0,0,141,142,
        5,15,0,0,142,21,1,0,0,0,143,144,5,16,0,0,144,148,3,52,26,0,145,146,
        5,16,0,0,146,148,7,0,0,0,147,143,1,0,0,0,147,145,1,0,0,0,148,23,
        1,0,0,0,149,150,5,17,0,0,150,151,7,1,0,0,151,25,1,0,0,0,152,153,
        5,22,0,0,153,154,5,44,0,0,154,27,1,0,0,0,155,156,5,23,0,0,156,29,
        1,0,0,0,157,158,5,24,0,0,158,31,1,0,0,0,159,160,5,25,0,0,160,33,
        1,0,0,0,161,162,5,26,0,0,162,35,1,0,0,0,163,164,5,27,0,0,164,37,
        1,0,0,0,165,166,5,28,0,0,166,167,3,52,26,0,167,168,5,4,0,0,168,169,
        3,52,26,0,169,39,1,0,0,0,170,171,5,29,0,0,171,172,3,52,26,0,172,
        41,1,0,0,0,173,174,5,30,0,0,174,175,3,52,26,0,175,43,1,0,0,0,176,
        177,5,31,0,0,177,45,1,0,0,0,178,179,7,2,0,0,179,47,1,0,0,0,180,181,
        5,48,0,0,181,49,1,0,0,0,182,188,5,45,0,0,183,188,5,46,0,0,184,188,
        5,47,0,0,185,188,3,48,24,0,186,188,7,1,0,0,187,182,1,0,0,0,187,183,
        1,0,0,0,187,184,1,0,0,0,187,185,1,0,0,0,187,186,1,0,0,0,188,51,1,
        0,0,0,189,190,3,50,25,0,190,193,7,3,0,0,191,194,3,50,25,0,192,194,
        3,52,26,0,193,191,1,0,0,0,193,192,1,0,0,0,194,203,1,0,0,0,195,196,
        3,50,25,0,196,199,7,4,0,0,197,200,3,50,25,0,198,200,3,52,26,0,199,
        197,1,0,0,0,199,198,1,0,0,0,200,203,1,0,0,0,201,203,3,50,25,0,202,
        189,1,0,0,0,202,195,1,0,0,0,202,201,1,0,0,0,203,53,1,0,0,0,11,76,
        98,104,123,134,137,147,187,193,199,202
    ]

class rabbitParser ( Parser ):

    grammarFileName = "rabbit.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'reset'", "'print '", "'int '", "' '", 
                     "'bool '", "'{'", "'}'", "'if '", "'?'", "'endif'", 
                     "'else'", "'for'", "'endfor'", "'getX'", "'getY'", 
                     "'name '", "'angle '", "'90'", "'180'", "'270'", "'360'", 
                     "'setview '", "'spaceLeft'", "'checkField'", "'putItem'", 
                     "'getItem'", "'getAngle'", "'jump '", "'sleep '", "'go '", 
                     "'home'", "'<'", "'>'", "'=='", "'!='", "'<='", "'>='", 
                     "' and '", "' or '", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "KATY", "INT", "TRUE", "FALSE", "STRING", "WS" ]

    RULE_prog = 0
    RULE_cmd = 1
    RULE_restart = 2
    RULE_print = 3
    RULE_declaration = 4
    RULE_block = 5
    RULE_if = 6
    RULE_for = 7
    RULE_comparison = 8
    RULE_getX = 9
    RULE_getY = 10
    RULE_setValue = 11
    RULE_angle = 12
    RULE_setView = 13
    RULE_spaceLeft = 14
    RULE_checkField = 15
    RULE_putItem = 16
    RULE_getItem = 17
    RULE_getAngle = 18
    RULE_jump = 19
    RULE_sleep = 20
    RULE_go = 21
    RULE_home = 22
    RULE_comparisonOperator = 23
    RULE_name = 24
    RULE_value = 25
    RULE_expr = 26

    ruleNames =  [ "prog", "cmd", "restart", "print", "declaration", "block", 
                   "if", "for", "comparison", "getX", "getY", "setValue", 
                   "angle", "setView", "spaceLeft", "checkField", "putItem", 
                   "getItem", "getAngle", "jump", "sleep", "go", "home", 
                   "comparisonOperator", "name", "value", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    KATY=44
    INT=45
    TRUE=46
    FALSE=47
    STRING=48
    WS=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmd(self):
            return self.getTypedRuleContext(rabbitParser.CmdContext,0)


        def getRuleIndex(self):
            return rabbitParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = rabbitParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.cmd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return rabbitParser.RULE_cmd

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CommandContext(CmdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rabbitParser.CmdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def go(self):
            return self.getTypedRuleContext(rabbitParser.GoContext,0)

        def jump(self):
            return self.getTypedRuleContext(rabbitParser.JumpContext,0)

        def home(self):
            return self.getTypedRuleContext(rabbitParser.HomeContext,0)

        def angle(self):
            return self.getTypedRuleContext(rabbitParser.AngleContext,0)

        def setView(self):
            return self.getTypedRuleContext(rabbitParser.SetViewContext,0)

        def for_(self):
            return self.getTypedRuleContext(rabbitParser.ForContext,0)

        def getX(self):
            return self.getTypedRuleContext(rabbitParser.GetXContext,0)

        def getY(self):
            return self.getTypedRuleContext(rabbitParser.GetYContext,0)

        def getAngle(self):
            return self.getTypedRuleContext(rabbitParser.GetAngleContext,0)

        def getItem(self):
            return self.getTypedRuleContext(rabbitParser.GetItemContext,0)

        def putItem(self):
            return self.getTypedRuleContext(rabbitParser.PutItemContext,0)

        def checkField(self):
            return self.getTypedRuleContext(rabbitParser.CheckFieldContext,0)

        def spaceLeft(self):
            return self.getTypedRuleContext(rabbitParser.SpaceLeftContext,0)

        def sleep(self):
            return self.getTypedRuleContext(rabbitParser.SleepContext,0)

        def print_(self):
            return self.getTypedRuleContext(rabbitParser.PrintContext,0)

        def restart(self):
            return self.getTypedRuleContext(rabbitParser.RestartContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)


    class IfBlockContext(CmdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rabbitParser.CmdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def if_(self):
            return self.getTypedRuleContext(rabbitParser.IfContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfBlock" ):
                listener.enterIfBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfBlock" ):
                listener.exitIfBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfBlock" ):
                return visitor.visitIfBlock(self)
            else:
                return visitor.visitChildren(self)


    class ReassignmentContext(CmdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rabbitParser.CmdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def setValue(self):
            return self.getTypedRuleContext(rabbitParser.SetValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReassignment" ):
                listener.enterReassignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReassignment" ):
                listener.exitReassignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReassignment" ):
                return visitor.visitReassignment(self)
            else:
                return visitor.visitChildren(self)


    class DeclarationExprContext(CmdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rabbitParser.CmdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def declaration(self):
            return self.getTypedRuleContext(rabbitParser.DeclarationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationExpr" ):
                listener.enterDeclarationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationExpr" ):
                listener.exitDeclarationExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationExpr" ):
                return visitor.visitDeclarationExpr(self)
            else:
                return visitor.visitChildren(self)



    def cmd(self):

        localctx = rabbitParser.CmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_cmd)
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = rabbitParser.CommandContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.go()
                pass

            elif la_ == 2:
                localctx = rabbitParser.CommandContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.jump()
                pass

            elif la_ == 3:
                localctx = rabbitParser.CommandContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.home()
                pass

            elif la_ == 4:
                localctx = rabbitParser.CommandContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.angle()
                pass

            elif la_ == 5:
                localctx = rabbitParser.CommandContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                self.setView()
                pass

            elif la_ == 6:
                localctx = rabbitParser.CommandContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 61
                self.for_()
                pass

            elif la_ == 7:
                localctx = rabbitParser.IfBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 62
                self.if_()
                pass

            elif la_ == 8:
                localctx = rabbitParser.CommandContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 63
                self.getX()
                pass

            elif la_ == 9:
                localctx = rabbitParser.CommandContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 64
                self.getY()
                pass

            elif la_ == 10:
                localctx = rabbitParser.CommandContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 65
                self.getAngle()
                pass

            elif la_ == 11:
                localctx = rabbitParser.CommandContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 66
                self.getItem()
                pass

            elif la_ == 12:
                localctx = rabbitParser.CommandContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 67
                self.putItem()
                pass

            elif la_ == 13:
                localctx = rabbitParser.CommandContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 68
                self.checkField()
                pass

            elif la_ == 14:
                localctx = rabbitParser.CommandContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 69
                self.spaceLeft()
                pass

            elif la_ == 15:
                localctx = rabbitParser.ReassignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 70
                self.setValue()
                pass

            elif la_ == 16:
                localctx = rabbitParser.CommandContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 71
                self.sleep()
                pass

            elif la_ == 17:
                localctx = rabbitParser.DeclarationExprContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 72
                self.declaration()
                pass

            elif la_ == 18:
                localctx = rabbitParser.CommandContext(self, localctx)
                self.enterOuterAlt(localctx, 18)
                self.state = 73
                self.sleep()
                pass

            elif la_ == 19:
                localctx = rabbitParser.CommandContext(self, localctx)
                self.enterOuterAlt(localctx, 19)
                self.state = 74
                self.print_()
                pass

            elif la_ == 20:
                localctx = rabbitParser.CommandContext(self, localctx)
                self.enterOuterAlt(localctx, 20)
                self.state = 75
                self.restart()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RestartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return rabbitParser.RULE_restart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRestart" ):
                listener.enterRestart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRestart" ):
                listener.exitRestart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRestart" ):
                return visitor.visitRestart(self)
            else:
                return visitor.visitChildren(self)




    def restart(self):

        localctx = rabbitParser.RestartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_restart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(rabbitParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(rabbitParser.ExprContext,0)


        def getRuleIndex(self):
            return rabbitParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = rabbitParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(rabbitParser.T__1)
            self.state = 81
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(rabbitParser.NameContext,0)


        def expr(self):
            return self.getTypedRuleContext(rabbitParser.ExprContext,0)


        def TRUE(self):
            return self.getToken(rabbitParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(rabbitParser.FALSE, 0)

        def comparison(self):
            return self.getTypedRuleContext(rabbitParser.ComparisonContext,0)


        def getRuleIndex(self):
            return rabbitParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = rabbitParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.match(rabbitParser.T__2)
                self.state = 84
                self.name()
                self.state = 85
                self.match(rabbitParser.T__3)
                self.state = 86
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.match(rabbitParser.T__4)
                self.state = 89
                self.name()
                self.state = 90
                self.match(rabbitParser.T__3)
                self.state = 91
                _la = self._input.LA(1)
                if not(_la==46 or _la==47):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.match(rabbitParser.T__4)
                self.state = 94
                self.name()
                self.state = 95
                self.match(rabbitParser.T__3)
                self.state = 96
                self.comparison()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rabbitParser.CmdContext)
            else:
                return self.getTypedRuleContext(rabbitParser.CmdContext,i)


        def getRuleIndex(self):
            return rabbitParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = rabbitParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(rabbitParser.T__5)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4291023150) != 0):
                self.state = 101
                self.cmd()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(rabbitParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self):
            return self.getTypedRuleContext(rabbitParser.ComparisonContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rabbitParser.BlockContext)
            else:
                return self.getTypedRuleContext(rabbitParser.BlockContext,i)


        def getRuleIndex(self):
            return rabbitParser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = rabbitParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_if)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.match(rabbitParser.T__7)
                self.state = 110
                self.comparison()
                self.state = 111
                self.match(rabbitParser.T__8)
                self.state = 112
                self.block()
                self.state = 113
                self.match(rabbitParser.T__9)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.match(rabbitParser.T__7)
                self.state = 116
                self.comparison()
                self.state = 117
                self.match(rabbitParser.T__8)
                self.state = 118
                self.block()
                self.state = 119
                self.match(rabbitParser.T__10)
                self.state = 120
                self.block()
                self.state = 121
                self.match(rabbitParser.T__9)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(rabbitParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(rabbitParser.BlockContext,0)


        def getRuleIndex(self):
            return rabbitParser.RULE_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor" ):
                listener.enterFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor" ):
                listener.exitFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor" ):
                return visitor.visitFor(self)
            else:
                return visitor.visitChildren(self)




    def for_(self):

        localctx = rabbitParser.ForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(rabbitParser.T__11)
            self.state = 126
            self.expr()
            self.state = 127
            self.block()
            self.state = 128
            self.match(rabbitParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparisonOperator(self):
            return self.getTypedRuleContext(rabbitParser.ComparisonOperatorContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rabbitParser.ExprContext)
            else:
                return self.getTypedRuleContext(rabbitParser.ExprContext,i)


        def comparison(self):
            return self.getTypedRuleContext(rabbitParser.ComparisonContext,0)


        def getRuleIndex(self):
            return rabbitParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = rabbitParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comparison)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.expr()
                self.state = 131
                self.comparisonOperator()
                self.state = 134
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 132
                    self.expr()
                    pass

                elif la_ == 2:
                    self.state = 133
                    self.comparison()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GetXContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return rabbitParser.RULE_getX

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetX" ):
                listener.enterGetX(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetX" ):
                listener.exitGetX(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetX" ):
                return visitor.visitGetX(self)
            else:
                return visitor.visitChildren(self)




    def getX(self):

        localctx = rabbitParser.GetXContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_getX)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(rabbitParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GetYContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return rabbitParser.RULE_getY

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetY" ):
                listener.enterGetY(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetY" ):
                listener.exitGetY(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetY" ):
                return visitor.visitGetY(self)
            else:
                return visitor.visitChildren(self)




    def getY(self):

        localctx = rabbitParser.GetYContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_getY)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(rabbitParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(rabbitParser.ExprContext,0)


        def TRUE(self):
            return self.getToken(rabbitParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(rabbitParser.FALSE, 0)

        def getRuleIndex(self):
            return rabbitParser.RULE_setValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetValue" ):
                listener.enterSetValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetValue" ):
                listener.exitSetValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetValue" ):
                return visitor.visitSetValue(self)
            else:
                return visitor.visitChildren(self)




    def setValue(self):

        localctx = rabbitParser.SetValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_setValue)
        self._la = 0 # Token type
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.match(rabbitParser.T__15)
                self.state = 144
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.match(rabbitParser.T__15)
                self.state = 146
                _la = self._input.LA(1)
                if not(_la==46 or _la==47):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AngleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return rabbitParser.RULE_angle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAngle" ):
                listener.enterAngle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAngle" ):
                listener.exitAngle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAngle" ):
                return visitor.visitAngle(self)
            else:
                return visitor.visitChildren(self)




    def angle(self):

        localctx = rabbitParser.AngleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_angle)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(rabbitParser.T__16)
            self.state = 150
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3932160) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetViewContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KATY(self):
            return self.getToken(rabbitParser.KATY, 0)

        def getRuleIndex(self):
            return rabbitParser.RULE_setView

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetView" ):
                listener.enterSetView(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetView" ):
                listener.exitSetView(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetView" ):
                return visitor.visitSetView(self)
            else:
                return visitor.visitChildren(self)




    def setView(self):

        localctx = rabbitParser.SetViewContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_setView)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(rabbitParser.T__21)
            self.state = 153
            self.match(rabbitParser.KATY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpaceLeftContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return rabbitParser.RULE_spaceLeft

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpaceLeft" ):
                listener.enterSpaceLeft(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpaceLeft" ):
                listener.exitSpaceLeft(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpaceLeft" ):
                return visitor.visitSpaceLeft(self)
            else:
                return visitor.visitChildren(self)




    def spaceLeft(self):

        localctx = rabbitParser.SpaceLeftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_spaceLeft)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(rabbitParser.T__22)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CheckFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return rabbitParser.RULE_checkField

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCheckField" ):
                listener.enterCheckField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCheckField" ):
                listener.exitCheckField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCheckField" ):
                return visitor.visitCheckField(self)
            else:
                return visitor.visitChildren(self)




    def checkField(self):

        localctx = rabbitParser.CheckFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_checkField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(rabbitParser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PutItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return rabbitParser.RULE_putItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPutItem" ):
                listener.enterPutItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPutItem" ):
                listener.exitPutItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutItem" ):
                return visitor.visitPutItem(self)
            else:
                return visitor.visitChildren(self)




    def putItem(self):

        localctx = rabbitParser.PutItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_putItem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(rabbitParser.T__24)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GetItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return rabbitParser.RULE_getItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetItem" ):
                listener.enterGetItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetItem" ):
                listener.exitGetItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetItem" ):
                return visitor.visitGetItem(self)
            else:
                return visitor.visitChildren(self)




    def getItem(self):

        localctx = rabbitParser.GetItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_getItem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(rabbitParser.T__25)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GetAngleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return rabbitParser.RULE_getAngle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetAngle" ):
                listener.enterGetAngle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetAngle" ):
                listener.exitGetAngle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetAngle" ):
                return visitor.visitGetAngle(self)
            else:
                return visitor.visitChildren(self)




    def getAngle(self):

        localctx = rabbitParser.GetAngleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_getAngle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(rabbitParser.T__26)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JumpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rabbitParser.ExprContext)
            else:
                return self.getTypedRuleContext(rabbitParser.ExprContext,i)


        def getRuleIndex(self):
            return rabbitParser.RULE_jump

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJump" ):
                listener.enterJump(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJump" ):
                listener.exitJump(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJump" ):
                return visitor.visitJump(self)
            else:
                return visitor.visitChildren(self)




    def jump(self):

        localctx = rabbitParser.JumpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_jump)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(rabbitParser.T__27)
            self.state = 166
            self.expr()
            self.state = 167
            self.match(rabbitParser.T__3)
            self.state = 168
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SleepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(rabbitParser.ExprContext,0)


        def getRuleIndex(self):
            return rabbitParser.RULE_sleep

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSleep" ):
                listener.enterSleep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSleep" ):
                listener.exitSleep(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSleep" ):
                return visitor.visitSleep(self)
            else:
                return visitor.visitChildren(self)




    def sleep(self):

        localctx = rabbitParser.SleepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_sleep)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(rabbitParser.T__28)
            self.state = 171
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(rabbitParser.ExprContext,0)


        def getRuleIndex(self):
            return rabbitParser.RULE_go

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGo" ):
                listener.enterGo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGo" ):
                listener.exitGo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGo" ):
                return visitor.visitGo(self)
            else:
                return visitor.visitChildren(self)




    def go(self):

        localctx = rabbitParser.GoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_go)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(rabbitParser.T__29)
            self.state = 174
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HomeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return rabbitParser.RULE_home

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHome" ):
                listener.enterHome(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHome" ):
                listener.exitHome(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHome" ):
                return visitor.visitHome(self)
            else:
                return visitor.visitChildren(self)




    def home(self):

        localctx = rabbitParser.HomeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_home)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(rabbitParser.T__30)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return rabbitParser.RULE_comparisonOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOperator" ):
                listener.enterComparisonOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOperator" ):
                listener.exitComparisonOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonOperator" ):
                return visitor.visitComparisonOperator(self)
            else:
                return visitor.visitChildren(self)




    def comparisonOperator(self):

        localctx = rabbitParser.ComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_comparisonOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1095216660480) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(rabbitParser.STRING, 0)

        def getRuleIndex(self):
            return rabbitParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = rabbitParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(rabbitParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(rabbitParser.INT, 0)

        def TRUE(self):
            return self.getToken(rabbitParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(rabbitParser.FALSE, 0)

        def name(self):
            return self.getTypedRuleContext(rabbitParser.NameContext,0)


        def getRuleIndex(self):
            return rabbitParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = rabbitParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(rabbitParser.INT)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.match(rabbitParser.TRUE)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.match(rabbitParser.FALSE)
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 4)
                self.state = 185
                self.name()
                pass
            elif token in [18, 19, 20, 21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 186
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3932160) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return rabbitParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rabbitParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(rabbitParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class InfiExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a rabbitParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rabbitParser.ValueContext)
            else:
                return self.getTypedRuleContext(rabbitParser.ValueContext,i)

        def expr(self):
            return self.getTypedRuleContext(rabbitParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfiExpr" ):
                listener.enterInfiExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfiExpr" ):
                listener.exitInfiExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfiExpr" ):
                return visitor.visitInfiExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = rabbitParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = rabbitParser.InfiExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.value()
                self.state = 190
                _la = self._input.LA(1)
                if not(_la==40 or _la==41):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 193
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 191
                    self.value()
                    pass

                elif la_ == 2:
                    self.state = 192
                    self.expr()
                    pass


                pass

            elif la_ == 2:
                localctx = rabbitParser.InfiExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.value()
                self.state = 196
                _la = self._input.LA(1)
                if not(_la==42 or _la==43):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 199
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 197
                    self.value()
                    pass

                elif la_ == 2:
                    self.state = 198
                    self.expr()
                    pass


                pass

            elif la_ == 3:
                localctx = rabbitParser.NumberExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 201
                self.value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





