import ply.lex as lex

# lista de palavras reservadas
reserved = {
    'se': 'P_RESERVADA_SE',
    'então': 'P_RESERVADA_ENTAO',
    'senão': 'P_RESERVADA_SENAO',
    'retorne': 'P_RESERVADA_RETORNE',
    'verdadeiro': 'P_RESERVADA_VERDADEIRO',
    'falso': 'P_RESERVADA_FALSO',
    'imprima': 'P_RESERVADA_IMPRIMA',
    'int': 'P_RESERVADA_TIPO_INTEIRO'
}

# lista de tokens
tokens = [
    'NUM_INTEIRO',
    'SIMBOL_ADICAO',
    'SIMBOL_SUBTRACAO',
    'SIMBOL_MULTIPLICACAO',
    'SIMBOL_DIVISAO',
    'MAIORQUE',
    'MAIOROUIGUAL',
    'MENORQUE',
    'MENOROUIGUAL',
    'ABRE_PAREN',
    'FECHA_PAREN',
    'SIMBOL_COMENTARIO',
    'ID',
    'SIMBOL_ATRIBUICAO'
 ] + list(reserved.values())

# expressões regulares para os tokens mais simples
t_SIMBOL_ADICAO = r'\+'
t_SIMBOL_SUBTRACAO = r'-'
t_SIMBOL_MULTIPLICACAO = r'\*'
t_SIMBOL_DIVISAO = r'/'
t_ABRE_PAREN = r'\('
t_FECHA_PAREN = r'\)'
t_ignore = ' \t'
t_SIMBOL_ATRIBUICAO = r'\='
t_MAIORQUE = r'\>'
t_MENORQUE = r'\<'
t_MAIOROUIGUAL = r'\>\='
t_MENOROUIGUAL = r'\<\='

# expressões regulares que exigem ações adicionais são definidas usando uma função
def t_NUM_INTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# rastreia o número de linhas
def t_novalinha(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# ignora as linha de comentários
def t_SIMBOL_COMENTARIO(t):
    r'\#.*'
    pass

# função para identificar variáveis
def t_ID(t):
    r'[a-zA-Z][a-z-A-Z0-9çÇãÃ]*'
    t.type = reserved.get(t.value, 'ID') # Verifica se é uma palavra reservada
    return t

# função para lidar com erros, por hora apenas ignora
def t_error(t):
    print(f'Um erro foi encontrado: {t.value}')
    t.lexer.skip(1)

# constroi o analizador léxico com base nas regras acima
lexer = lex.lex()

teste = open("sample.txt", 'r')

# for linha in teste:
#     print(linha)

lexer.input(teste.read())

teste.close()

for token in lexer:
    print(f'Token: {token.type} -> Valor: {token.value}')