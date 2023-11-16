import ply.lex as lex

# lista de tokens
tokens = (
    'INTEIRO',
    'ADICAO',
    'SUBTRACAO',
    'MULTIPLICACAO',
    'DIVISAO',
    'ABRE_PAREN',
    'FECHA_PAREN',
    'COMENTARIO'
)

# expressões regulares para os tokens mais simples
t_ADICAO = r'\+'
t_SUBTRACAO = r'-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO = r'/'
t_ABRE_PAREN = r'\('
t_FECHA_PAREN = r'\)'
t_ignore = ' \t'

# expressões regulares que exigem ações adicionais são definidas usando uma função
def t_INTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# rastreia o número de linhas
def t_novalinha(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# ignora as linha de comentários
def t_COMENTARIO(t):
    r'\#.*'
    pass

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

for token in lexer:
    print(f'Token: {token.type} -> Valor: {token.value}')