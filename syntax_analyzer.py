import ply.yacc as yacc
# importa os tokens do analisador léxico, senão não funciona
from lexical_analizer import tokens

# define a procedência dos operadores
precedence = (
    ('nonassoc', 'MENORQUE', 'MENOROUIGUAL', 'MAIORQUE', 'MAIOROUIGUAL'),  # operadores de comparação
    ('left', 'SIMBOL_ADICAO', 'SIMBOL_SUBTRACAO'),
    ('left', 'SIMBOL_MULTIPLICACAO', 'SIMBOL_DIVISAO'),
)

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

# Deriva um termo para um fator
def p_termo_fator(p):
    'termo : fator'
    p[0] = p[1]

# Deriva um fator para um INTEIRO
def p_fator_num(p):
    'fator : NUM_INTEIRO'
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

sample = open('sample2.txt', 'r')

result = parser.parse(sample.read())

sample.close()

print(result)