import re

resultado = ''

with open('sample2.txt', 'r') as traducao, open('resultado.py', 'w') as saida:
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