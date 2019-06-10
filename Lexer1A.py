import ply.lex as lex

reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    "not":"NOT"
}


tokens=["VARIABLE","NUMBER","PLUS","MINUS","TIMES","DIVIDE","EQUALS","STRING","COMPARACION","ID"] + list(reserved.values())
t_ignore=" \t| |( )*"
t_PLUS=r"\+"
t_MINUS=r"-"
t_TIMES=r"\*"
t_DIVIDE=r"/"
t_EQUALS=r"="
t_VARIABLE=r"[a-zA-Z]([a-zA-Z0-9])*"

t_STRING=r"'([a-zA-Z0-9]| )*'"
t_COMPARACION=r"=="


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    if(t.type=="ID"):
        t.type="VARIABLE"
    return t

def t_error(t):
    print('Illegal character')
    t.lexer.skip(1)


def t_NUMBER(t):
    r"\d+"
    t.value=int(t.value)
    return t

lex.lex()
lex.input("if not 2332 =='carro'")
while True:
    tok=lex.token()
    if not tok: break
    print("TOK:", tok.type, "  TOK VALUE: ",tok.value)