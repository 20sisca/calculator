from ply import lex

tokens = ('NUMBER',)

t_NUMBER = '[0-9]+'
t_ignore = ' '

lexer = lex.lex()

if __name__ == "__main__" :
    lexer.input('42')
    for tok in lexer :
        print(tok)