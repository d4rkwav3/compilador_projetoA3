import ply.yacc as yacc
# importa os tokens do analisador léxico, senão não funciona
from lexical_analizer import tokens

start = 'expressao'
inteiros = {}
decimais = {}
strings = {}

# define a procedência dos operadores
precedence = (
    ('nonassoc', 'MENORQUE', 'MENOROUIGUAL', 'MAIORQUE', 'MAIOROUIGUAL'),  # operadores de comparação
    ('left', 'SIMBOL_ADICAO', 'SIMBOL_SUBTRACAO'),
    ('left', 'SIMBOL_MULTIPLICACAO', 'SIMBOL_DIVISAO'),
)

def p_expressao_declaracao(p):
    'expressao : declaracao'
    p[0] = p[1]

def p_expressao_atribuicao(p):
    'expressao : atribuicao'
    p[0] = p[1]

def p_expressao_controle(p):
    'expressao : controle'
    p[0] = p[1]

def p_expressao_loop(p):
    'expressao : loop'
    p[0] = p[1]

def p_expressao_funcao(p):
    'expressao : funcao'
    p[0] = p[1]

def p_controle_se(p):
    'controle : P_RESERVADA_SE expressao P_RESERVADA_ENTAO'
    p[0] = p[2]

def p_controle_senao(p):
    'controle : P_RESERVADA_SENAO P_RESERVADA_ENTAO'
    pass

def p_loop_enquanto(p):
    'loop : P_RESERVARDA_LOOP_ENQUANTO expressao P_RESERVADA_ENTAO'
    p[0] = p[2]

def p_loop_paracada(p):
    'loop : P_RESERVARDA_LOOP_PARACADA ID P_RESERVADA_EM expressao P_RESERVADA_ENTAO'
    p[0] = p[4]

def p_expressao_comentario(p):
    'expressao : COMENTARIO'
    print(f'Linha de comentário ignorada -> {p[1]}')

def p_declaracao_inteiro(p):
    'declaracao : P_RESERVADA_TIPO_INTEIRO ID SIMBOL_ATRIBUICAO NUM_INTEIRO'
    # print(f'{p[0]} {p[1]} {p[2]} {p[3]} {p[4]}')
    inteiros.update({p[2] : p[4]})
    p[0] = p[2]

def p_declaracao_decimal(p):
    'declaracao : P_RESERVARDA_TIPO_DECIMAL ID SIMBOL_ATRIBUICAO NUM_DECIMAL'
    decimais.update({p[2] : p[4]})
    p[0] = p[2]

def p_declaracao_palavra(p):
    'declaracao : P_RESERVADA_TIPO_PALAVRA ID SIMBOL_ATRIBUICAO STRING_LITERAL'
    strings.update({p[2] : p[4]})
    p[0] = p[2]

def p_declaracao_funcao_1_arg(p):
    'declaracao : P_RESERVADA_TIPO_INTEIRO ID SIMBOL_ATRIBUICAO ID ABRE_PAREN ID FECHA_PAREN'
    p[0] = p[1]

def p_declaracao_funcao_1_literal(p):
    'declaracao : P_RESERVADA_TIPO_INTEIRO ID SIMBOL_ATRIBUICAO ID ABRE_PAREN STRING_LITERAL FECHA_PAREN'
    p[0] = p[6]

def p_declaracao_funcao_0_arg(p):
    'declaracao : P_RESERVADA_TIPO_INTEIRO ID SIMBOL_ATRIBUICAO ID ABRE_PAREN FECHA_PAREN'
    p[0] = p[1]

def p_funcao(p):
    'funcao : ID ABRE_PAREN termo FECHA_PAREN'
    p[0] = p[2]

def p_atribuicao(p):
    'atribuicao : ID SIMBOL_ATRIBUICAO termo'
    p[0] = p[3]

# Deriva uma expressão para uma expressão ADIÇÃO termo
def p_expressao_adicao(p):
    'expressao : expressao SIMBOL_ADICAO termo'
    p[0] = p[1] + p[3]

# Deriva uma expressão para uma expressão SUBTRAÇÃO termo
def p_expressao_subtracao(p):
    'expressao : expressao SIMBOL_SUBTRACAO termo'
    p[0] = p[1] - p[3]

# Deriva uma expressão por um termo
def p_expressao_termo(p):
    'expressao : termo'
    p[0] = p[1]

# Deriva um termo para um termo MULTIPLICAÇÃO fator
def p_termo_multiplicacao(p):
    'termo : termo SIMBOL_MULTIPLICACAO fator'
    p[0] = p[1] * p[3]

# Deriva um termo para um termo DIVISÃO fator
def p_termo_divisao(p):
    'termo : termo SIMBOL_DIVISAO fator'
    p[0] = p[1] / p[3]

def p_termo_maior(p):
    'termo : termo MAIORQUE fator'
    value = inteiros.get(p[1])

    if p[1] in inteiros.keys():
        # print('Teste', value)
        p[0] = value > p[3]
    else:
        p[0] = p[1] > p[3]

def p_termo_maior_ou_igual(p):
    'termo : termo MAIOROUIGUAL fator'
    value = inteiros.get(p[1])

    if p[1] in inteiros.keys():
        # print('Teste', value)
        p[0] = value >= p[3]
    else:
        p[0] = p[1] >= p[3]

def p_termo_menor(p):
    'termo : termo MENORQUE fator'
    value = inteiros.get(p[1])

    if p[1] in inteiros.keys():
        # print('Teste', value)
        p[0] = value < p[3]
    else:
        p[0] = p[1] < p[3]

def p_termo_menor_ou_igual(p):
    'termo : termo MENOROUIGUAL fator'
    value = inteiros.get(p[1])

    if p[1] in inteiros.keys():
        p[0] = value <= p[3]
    else:
        p[0] = p[1] <= p[3]        

def p_termo_comparar_valor(p):
    'termo : termo COMPARAR_VALOR fator'
    value = inteiros.get(p[1]) if True else strings.get(p[1])

    if p[1] in inteiros.keys():
        p[0] = value == p[3]
    elif p[1] in strings.keys():
        p[0] = value == p[3]
    else:
        p[0] = p[1] == p[3] 

# Deriva um termo para um fator
def p_termo_fator(p):
    'termo : fator'
    p[0] = p[1]

# Deriva um fator para um INTEIRO
def p_fator_num(p):
    'fator : primitivo'
    p[0] = p[1]

def p_numero_inteiro(p):
    'primitivo : NUM_INTEIRO'
    p[0] = p[1]

def p_numero_decimal(p):
    'primitivo : NUM_DECIMAL'
    p[0] = p[1]

def p_fator_string(p):
    'primitivo : STRING_LITERAL'
    p[0] = p[1]

def p_fator_id(p):
    'fator : ID'
    eh_int = p[1] in inteiros.keys()
    eh_dec = p[1] in decimais.keys()
    eh_str = p[1] in strings.keys()
    erro_decl = f'Erro sintático! variável {p[1]} nunca foi declarada!'
    
    if eh_int or eh_dec or eh_str:
        pass
    else:
        print(erro_decl)

    p[0] = p[1]

# Deriva um fator para uma expressão entre parênteses
def p_fator_expressao(p):
    'fator : ABRE_PAREN expressao FECHA_PAREN'
    p[0] = p[2]

# Informa sobre algum erro detectado
def p_error(p):
    print(f'Erro de sintaxe detectado! -> {p.value}')

# constrói o parser com base nas regras de derivação acima
parser = yacc.yacc()

variaveis = {}

with open('sample2.txt', 'r') as string:
    for linha in string:
        result = parser.parse(linha, tracking=True)
        print(result)

for k, v in inteiros.items():
    # print('\tinteiro', k, '->', v)
    variaveis.update({k: v})

for k, v in decimais.items():
    # print('\tdecimal', k, '->', v)
    variaveis.update({k: v})

for k, v in strings.items():
    # print('\tpalavra', k, '->', v)
    variaveis.update({k: v})

for k, v in variaveis.items():
    print('\t', k, '->', v)