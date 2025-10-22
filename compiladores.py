import ply.lex as lex
import ply.yacc as yacc

# =====================
# ANALISADOR LÉXICO
# =====================

# lista de tokens
tokens = [
    'DERIVAR', 'INTEGRAR', 'ATRIBUIR', 'MOSTRAR',
    'ID', 'NUMBER',
    'OP', 'LPAREN', 'RPAREN', 'EQUALS'
]

# palavras reservadas
t_DERIVAR = r'derivar'
t_INTEGRAR = r'integrar'
t_ATRIBUIR = r'atribuir'
t_MOSTRAR = r'mostrar'
t_OP = r'\+|\-|\*|\/|\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value == 'derivar':
        t.type = 'DERIVAR'
    elif t.value == 'integrar':
        t.type = 'INTEGRAR'
    elif t.value == 'atribuir':
        t.type = 'ATRIBUIR'
    elif t.value == 'mostrar':
        t.type = 'MOSTRAR'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# ============================
# ANALISADOR SINTÁTICO
# ============================

def p_comando_atribuir(p):
    'comando : ATRIBUIR ID EQUALS expressao'
    p[0] = ('atribuir', p[2], p[4])

def p_comando_mostrar(p):
    'comando : MOSTRAR expressao'
    p[0] = ('mostrar', p[2])

def p_expressao_operacao(p):
    'expressao : expressao OP termo'
    p[0] = ('op', p[2], p[1], p[3])

def p_expressao_termo(p):
    'expressao : termo'
    p[0] = p[1]

def p_termo_id(p):
    'termo : ID'
    p[0] = ('id', p[1])

def p_termo_number(p):
    'termo : NUMBER'
    p[0] = ('num', p[1])

def p_termo_parenteses(p):
    'termo : LPAREN expressao RPAREN'
    p[0] = p[2]

def p_termo_derivar(p):
    'termo : DERIVAR expressao'
    p[0] = ('derivar', p[2])

def p_termo_integrar(p):
    'termo : INTEGRAR expressao'
    p[0] = ('integrar', p[2])

def p_error(p):
    if p:
        print(f"Erro de sintaxe próximo a '{p.value}'")
    else:
        print("Erro de sintaxe: fim inesperado da entrada")

parser = yacc.yacc()

# ============
# EXECUÇÃO
# ============

print("Digite uma expressão para análise sintática.")
print("Exemplo: atribuir resultado = derivar x + 2 * integrar y")

entrada = input("Expressão: ")

resultado = parser.parse(entrada, lexer=lexer)

if resultado:
    print("Expressão sintaticamente CORRETA!")
    print("Árvore sintática:", resultado)
else:
    print("Expressão inválida.")