import re
from lexical_analizer import lexer
from syntax_analyzer import parser, inteiros, decimais, strings, variaveis, erros

resultado = ''
arquivo = input("Digite o nome do arquivo que deseja analizar:\n-> ")

try:
    with open(arquivo, 'r') as analise_lexica:
        lexer.input(analise_lexica.read())
    
    print('\n------------ Início da Analise Léxica ------------\n')

    for token in lexer:
        if token.type == 'NOVA_LINHA':
            print('\n')
        else:
            print(f'Token: {token.type} -> Valor: {token.value}')

    lexer.lineno = 1
    print('\n-------------- Fim da Analise Léxica -------------\n')

    with open(arquivo, 'r') as analise_sintatica:
        print('\n------------ Início da Analise Sintática ------------\n')

        for linha in analise_sintatica:
            result = parser.parse(linha, tracking=True)
            print(result)

        print('\n------------- Fim da Analise Sintática --------------\n')

    for k, v in inteiros.items():
        variaveis.update({k: v})

    for k, v in decimais.items():
        variaveis.update({k: v})

    for k, v in strings.items():
        variaveis.update({k: v})

    for k, v in variaveis.items():
        print('\t', k, '->', v)

except FileNotFoundError as err:
    print(f'O arquivo {arquivo} não foi encontrado!\n', err)

except FileExistsError as err:
    print(f'O arquivo {arquivo} existe mas não pode ser escrito!\n', err)

finally:
    if len(erros) == 0:
        print("\nAnalise concluída, nenhum erro foi localizado, traduzindo o arquivo...")

        with open(arquivo, 'r') as traducao, open('resultado.py', 'w') as saida:
            for linha in traducao:
                linha = re.sub(r'\bpalavra \b', '', linha)
                linha = re.sub(r'\binteiro \b', '', linha)
                linha = re.sub(r'\bdecimal \b', '', linha)
                linha = re.sub(r'\bse\b', 'if', linha)
                linha = re.sub(r'\bsenão\b', 'else', linha)
                linha = re.sub(r'\b então\b', ':', linha)
                linha = re.sub(r'\benquanto\b', 'while', linha)
                linha = re.sub(r'\bparacada\b', 'for', linha)
                linha = re.sub(r'\bem\b', 'in', linha)
                linha = re.sub(r'\bleia\b', 'input', linha)
                linha = re.sub(r'\bimprima\b', 'print', linha)
                resultado += linha
            
            saida.writelines(resultado)
            print("\nArquivo traduzido com sucesso em resultado.py")
    else:
        print("\nUm ou mais erros foram identificados, corrija-os e tente novamente.")