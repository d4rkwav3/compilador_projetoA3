import ply.lex as lex

# lista de palavras reservadas
reserved = {
    'se': 'P_RESERVADA_SE',
    'então': 'P_RESERVADA_ENTAO',
    'senão': 'P_RESERVADA_SENAO',
    'inteiro': 'P_RESERVADA_TIPO_INTEIRO',
    'palavra': 'P_RESERVADA_TIPO_PALAVRA',
    'decimal': 'P_RESERVARDA_TIPO_DECIMAL',
    'enquanto': 'P_RESERVARDA_LOOP_ENQUANTO',
    'paracada': 'P_RESERVARDA_LOOP_PARACADA',
    'em': 'P_RESERVADA_EM'
}

# lista de tokens
tokens = [
    'NUM_INTEIRO',
    'NUM_DECIMAL',
    'SIMBOL_ADICAO',
    'SIMBOL_SUBTRACAO',
    'SIMBOL_MULTIPLICACAO',
    'SIMBOL_DIVISAO',
    'MAIORQUE',
    'MAIOROUIGUAL',
    'MENORQUE',
    'MENOROUIGUAL',
    'COMPARAR_VALOR',
    'ABRE_PAREN',
    'FECHA_PAREN',
    'COMENTARIO',
    'ID',
    'SIMBOL_ATRIBUICAO',
    'STRING_LITERAL',
    'ACUMULADOR',
    'REDUTOR',
 ] + list(reserved.values())

# expressões regulares para os tokens mais simples
t_SIMBOL_ADICAO = r'\+'
t_SIMBOL_SUBTRACAO = r'-'
t_SIMBOL_MULTIPLICACAO = r'\*'
t_SIMBOL_DIVISAO = r'/'
t_ABRE_PAREN = r'\('
t_FECHA_PAREN = r'\)'
t_SIMBOL_ATRIBUICAO = r'\='
t_COMPARAR_VALOR =  r'\=\='
t_MAIORQUE = r'\>'
t_MENORQUE = r'\<'
t_MAIOROUIGUAL = r'\>\='
t_MENOROUIGUAL = r'\<\='
t_ACUMULADOR = r'\+\='
t_REDUTOR = r'\-\='
t_ignore = ' \t'

# números com casas decimais
def t_NUM_DECIMAL(t):
    r'[-]?[\d+]\.[\d+]'
    t.value = float(t.value)
    return t

# expressões regulares que exigem ações adicionais são definidas usando uma função
def t_NUM_INTEIRO(t):
    r'[-]?\d+'
    t.value = int(t.value)
    return t

# rastreia o número de linhas
def t_NOVALINHA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    # print(f'\n---------------- Linha {t.lexer.lineno} ----------------\n')

# ignora as linha de comentários
def t_COMENTARIO(t):
    r'\#.*'
    # print(f'Linha de comentário ignorada -> {t.value}')
    return t

# identifica as strings literais
def t_STRING_LITERAL(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

# função para identificar variáveis
def t_ID(t):
    r'[a-zA-Z][a-z-A-Z0-9çÇãÃéÉúÚ]*'
    t.type = reserved.get(t.value, 'ID') # Verifica se é uma palavra reservada
    return t

# função para lidar com erros, por hora apenas ignora
def t_error(t):
    print(f'Um erro foi encontrado: {t.value}')
    t.lexer.skip(1)

# constroi o analizador léxico com base nas regras acima
lexer = lex.lex()

teste = open("sample2.txt", 'r')
lexer.input(teste.read())
teste.close()

print('------------ Início da Analise Léxica ------------\n')
# print(f'\n---------------- Linha {lexer.lineno} ----------------\n')

for token in lexer:
    print(f'Token: {token.type} -> Valor: {token.value}')

lexer.lineno = 1
print('\n-------------- Fim da Analise Léxica -------------\n')