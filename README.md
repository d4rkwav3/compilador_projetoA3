
# Projeto A3 Teoria da Computação e Compiladores

Desenvolvemos um analisador léxico e sintático em Python para uma linguagem de programação
que chamamos de Brazuca, inspirada pelo Portugol, onde as instruções são feitas em
português do Brasil e depois é transcrita para código Python válido, para maiores informações 
sobre a estrutura básica da linguagem consultar o arquivo documentacao.docx nesse repositório.

## Membros do Grupo

- Bruno Venâncio de Souza e Silva - RA: 821135934
- Danilo do Espirito Santo dos Santos - RA: 8222246362
- Henrick Melo Vital - RA: 821224905
- Henrique Isaias de Lima - RA: 8222243252
- Leonardo Fernandes Carrilho - RA: 821229981
- Lucas Lima Lopes - RA: 822161128
- Thiago Vieira Ramos - RA: 821235443


## Rodando localmente

Esse compilador exige Python 3.10 ou superior instalado, além do gerenciador de pacotes python PiP.

Clone o projeto:

```bash
  git clone https://github.com/d4rkwav3/compilador_projetoA3
```

Entre no diretório do projeto:

```bash
  cd compilador_projetoA3
```

Instale as dependências:

```bash
  pip install -r requirements.txt
```

Inicie o compilador:

```bash
  python compilador.py
```

Será solicitado que digite o nome do arquivo a ser analisad (precisa estar na mesma pasta do projeto),
se o arquivo passar pela analise léxica e sintática, um novo arquivo chamado resultado.py será criado, caso contrário 
o erro será impresso no terminal.