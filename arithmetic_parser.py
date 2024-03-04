from arithmetic_expressions import (Litteral)
from arithmetic_lexer import tokens
from ply import yacc

def p_litteral(p) :
    'expression : NUMBER'
    p[0] = Litteral(int(p[1]))

parser = yacc.yacc()

if __name__ == "__main__":
    print(parser.parse('42').eval())
    # print(parser.parse('((2 + 7)*(4-2))').eval())


