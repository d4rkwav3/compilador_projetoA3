import ply.yacc as yacc
# importa os tokens do analisador léxico, senão não funciona
from lexical_analizer import tokens
# A analise sintática começa com a variável expressao
start = 'expressao'
# dicionários para guardar os nomes e tipos de variaveis e erros
inteiros = {}
decimais = {}
strings = {}
erros = {}

# define a procedência dos operadores
precedence = (
    ('nonassoc', 'MENORQUE', 'MENOROUIGUAL', 'MAIORQUE', 'MAIOROUIGUAL'),  # operadores de comparação
    ('left', 'SIMBOL_ADICAO', 'SIMBOL_SUBTRACAO'),
    ('left', 'SIMBOL_MULTIPLICACAO', 'SIMBOL_DIVISAO'),
)
# Deriva uma expressão por uma declaração
def p_expressao_declaracao(p):
    'expressao : declaracao'
    p[0] = p[1]

# Deriva uma expressão por uma atribuição
def p_expressao_atribuicao(p):
    'expressao : atribuicao'
    p[0] = p[1]

# Deriva uma expressão por um controle
def p_expressao_controle(p):
    'expressao : controle'
    p[0] = p[1]

# Deriva uma expressão por um loop
def p_expressao_loop(p):
    'expressao : loop'
    p[0] = p[1]

# Deriva uma expressão por uma função
def p_expressao_funcao(p):
    'expressao : funcao'
    p[0] = p[1]

# Deriva uma expressão por uma nova_linha
def p_expressao_novalinha(p):
    'expressao : nova_linha'
    p[0] = p[1]

# Deriva um controle para um if expressão then
def p_controle_se(p):
    'controle : P_RESERVADA_SE expressao P_RESERVADA_ENTAO'
    p[0] = p[2]

# Deriva um controle para um else then
def p_controle_senao(p):
    'controle : P_RESERVADA_SENAO P_RESERVADA_ENTAO'
    pass

# Deriva um loop para um while expressão então
def p_loop_enquanto(p):
    'loop : P_RESERVARDA_LOOP_ENQUANTO expressao P_RESERVADA_ENTAO'
    p[0] = p[2]

# Deriva um loop para um for id em expressao then
def p_loop_paracada(p):
    'loop : P_RESERVARDA_LOOP_PARACADA ID P_RESERVADA_EM expressao P_RESERVADA_ENTAO'
    if isinstance(p[2], str):
        strings.update({p[2] : 'Loop FOR'})
    p[0] = p[4]

# Deriva uma expressão para um comentário
def p_expressao_comentario(p):
    'expressao : COMENTARIO'
    print(f'Linha de comentário ignorada -> {p[1]}')

# Deriva para uma declaração de variável de tipo inteira
def p_declaracao_inteiro(p):
    'declaracao : P_RESERVADA_TIPO_INTEIRO ID SIMBOL_ATRIBUICAO NUM_INTEIRO'
    # print(p[0], '=', p[2])
    inteiros.update({p[2] : p[4]})
    p[0] = p[2]

# Deriva para uma declaração de variável de tipo decimal
def p_declaracao_decimal(p):
    'declaracao : P_RESERVADA_TIPO_DECIMAL ID SIMBOL_ATRIBUICAO NUM_DECIMAL'
    decimais.update({p[2] : p[4]})
    p[0] = p[2]

# Deriva para uma declaração de variável de tipo palavra
def p_declaracao_palavra(p):
    'declaracao : P_RESERVADA_TIPO_PALAVRA ID SIMBOL_ATRIBUICAO STRING_LITERAL'
    strings.update({p[2] : p[4]})
    p[0] = p[2]

# Deriva para uma variável palavra que guarda uma função
def p_declaracao_funcao_string(p):
    'declaracao : P_RESERVADA_TIPO_PALAVRA ID SIMBOL_ATRIBUICAO ID ABRE_PAREN ID FECHA_PAREN'
    p[0] = p[1]

# Deriva para uma variável inteira que guarda uma função
def p_declaracao_funcao_inteiro(p):
    'declaracao : P_RESERVADA_TIPO_INTEIRO ID SIMBOL_ATRIBUICAO ID ABRE_PAREN STRING_LITERAL FECHA_PAREN'
    p[0] = p[6]

# Deriva para uma variável inteira que guarda uma função qualquer
def p_declaracao_funcao_0_arg_inteiro(p):
    'declaracao : P_RESERVADA_TIPO_INTEIRO ID SIMBOL_ATRIBUICAO ID ABRE_PAREN FECHA_PAREN'
    p[0] = p[1]

# Deriva para uma variável palavra que guarda uma função
def p_declaracao_funcao_string_funcao(p):
    'declaracao : P_RESERVADA_TIPO_PALAVRA ID SIMBOL_ATRIBUICAO funcao'
    #print('p_declaracao_funcao_string_funcao', p[2], p[4])
    strings.update({p[2] : 'função atribuida a variável'})
    p[0] = p[4]

# Deriva para uma variável inteira que guarda uma função
def p_declaracao_funcao_inteiro_funcao(p):
    'declaracao : P_RESERVADA_TIPO_INTEIRO ID SIMBOL_ATRIBUICAO funcao'
    #print('p_declaracao_funcao_inteiro', p[2], p[4])
    inteiros.update({p[2] : 'função atribuida a variável'})
    p[0] = p[4]

# Deriva para uma variável decimal que guarda uma função
def p_declaracao_funcao_decimal(p):
    'declaracao : P_RESERVADA_TIPO_DECIMAL ID SIMBOL_ATRIBUICAO funcao'
    #print('p_declaracao_funcao_decimal', p[2], p[4])
    decimais.update({p[2] : 'função atribuida a variável'})
    p[0] = p[4]

# Deriva para uma variável decimal que guarda uma expressão númerica
def p_declaracao_decimal_expressao(p):
    'declaracao : P_RESERVADA_TIPO_DECIMAL ID SIMBOL_ATRIBUICAO termo'
    #print('p_declaracao_funcao_decimal', p[2], p[4])
    decimais.update({p[2] : 'expressao atribuida a variável'})
    p[0] = p[4]

# Deriva para uma variável inteira que guarda uma expressão númerica
def p_declaracao_inteiro_expressao(p):
    'declaracao : P_RESERVADA_TIPO_INTEIRO ID SIMBOL_ATRIBUICAO termo'
    #print('p_declaracao_funcao_decimal', p[2], p[4])
    inteiros.update({p[2] : 'expressao atribuida a variável'})
    p[0] = p[4]

# Deriva para a função de imprimir na tela
def p_funcao_imprimir(p):
    'funcao : FUNCAO_IMPRIMIR ABRE_PAREN fator FECHA_PAREN'
    p[0] = p[2]

# Deriva para a função de ler do teclado
def p_funcao_ler(p):
    'funcao : FUNCAO_LER ABRE_PAREN fator FECHA_PAREN'
    p[0] = p[2]

# Deriva para um função qualquer com uma variável, número ou literal como argumento
def p_funcao_args(p):
    'funcao : ID ABRE_PAREN termo FECHA_PAREN'
    p[0] = p[2]

# Deriva para uma função vazia
def p_funcao_vazia(p):
    'funcao : ID ABRE_PAREN FECHA_PAREN'
    p[0] = p[2]

# Deriva uma atribuição para um id = termo
def p_atribuicao(p):
    'atribuicao : ID SIMBOL_ATRIBUICAO termo'
    p[0] = p[3]

# Deriva uma atribuição para um id += primitivo
def p_atribuicao_acumuladora(p):
    'atribuicao : ID ACUMULADOR primitivo'
    p[0] = p[3]

# Deriva uma atribuição para um id -= primitivo
def p_atribuicao_redutora(p):
    'atribuicao : ID REDUTOR primitivo'
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

# Deriva um termo para um termo > fator
def p_termo_maior(p):
    'termo : termo MAIORQUE fator'
    value = inteiros.get(p[1])
    #print('p_termo_maior', p[1], value)

    if p[1] in inteiros.keys():
        p[0] = value > p[3]
    else:
        p[0] = p[1] > p[3]

# Deriva um termo para um termo >= fator
def p_termo_maior_ou_igual(p):
    'termo : termo MAIOROUIGUAL fator'
    value = inteiros.get(p[1])

    if p[1] in inteiros.keys():
        p[0] = value >= p[3]
    else:
        p[0] = p[1] >= p[3]

# Deriva um termo para um termo < fator
def p_termo_menor(p):
    'termo : termo MENORQUE fator'
    value = inteiros.get(p[1])
    # print('p_termo_menor', value)
    if p[1] in inteiros.keys():
        p[0] = value < p[3]
    else:
        p[0] = p[1] < p[3]

# Deriva um termo para um termo <= fator
def p_termo_menor_ou_igual(p):
    'termo : termo MENOROUIGUAL fator'
    value = inteiros.get(p[1])

    if p[1] in inteiros.keys():
        p[0] = value <= p[3]
    else:
        p[0] = p[1] <= p[3]        

# Deriva um termo para um termo == fator
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

# Deriva um fator para um primitivo
def p_fator_num(p):
    'fator : primitivo'
    p[0] = p[1]

# Deriva um primitivo para um número inteiro
def p_primitivo_inteiro(p):
    'primitivo : NUM_INTEIRO'
    p[0] = p[1]

# Deriva um primitivo para um número decimal
def p_primitivo_decimal(p):
    'primitivo : NUM_DECIMAL'
    p[0] = p[1]

# Deriva um primitivo para uma string literal
def p_primitivo_string(p):
    'primitivo : STRING_LITERAL'
    p[0] = p[1]

# Deriva um fator para um id e salva a variável ou imprime um erro
def p_fator_id(p):
    'fator : ID'
    # Verifica se a variável foi declarada anteriormente
    eh_int = p[1] in inteiros.keys()
    eh_dec = p[1] in decimais.keys()
    eh_str = p[1] in strings.keys()
    erro_decl = f'Erro sintático! variável {p[1]} nunca foi declarada!'
    
    if eh_int or eh_dec or eh_str:
        pass
    else:
        # caso a variável não tenha sido declarada antes, imprimi um erro
        erros.update({'Erro' : erro_decl})
        print(erro_decl)

    p[0] = p[1]

# Deriva uma nova_linha para um caracter de nova linha (\n)
def p_nova_linha(p):
    'nova_linha : NOVA_LINHA'
    print('Nova linha')

# Deriva um fator para uma expressão entre parênteses
def p_fator_expressao(p):
    'fator : ABRE_PAREN expressao FECHA_PAREN'
    p[0] = p[2]

# Informa sobre algum erro detectado
def p_error(p):
    
    if p == None:
        print('linha vazia')
    else:
        print(f'Erro de sintaxe detectado! -> {p.value}')

# constrói o parser com base nas regras de derivação acima
parser = yacc.yacc()

variaveis = {}

# Os 3 primeiros loops mergem as variáveis em um único dicionário
for k, v in inteiros.items():
    # print('\tinteiro', k, '->', v)
    variaveis.update({k: v})

for k, v in decimais.items():
    # print('\tdecimal', k, '->', v)
    variaveis.update({k: v})

for k, v in strings.items():
    # print('\tpalavra', k, '->', v)
    variaveis.update({k: v})

# for k, v in variaveis.items():
#    print('\t', k, '->', v)