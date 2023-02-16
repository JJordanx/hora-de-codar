'''
FUNCOES DE VALIDAÇÃO
'''
# Funcao que ler um numero inteiro - Sistema de validação.


def leiaint(msg):
    """
    msg : vai receber o numero que o usuario digitar
    """
    ok = False  # O OBJETIVO DESSA VARIAVEL DE RESUL LOGICO É UTILIZA-LA PARA SAIR DO PROG QUANDO SEU VALOR FOR TRUE
    valor = 0
    while True:
        # o que foi digitado será colocado dentro de n (var local de dentro da funcao)
        n = str(input(msg))
        if n.isnumeric():  # se n for um valor numerico
            # uma cópia do tipo inteira de n será armazenada dentro de valor
            valor = int(n)
            ok = True  # confirmação de encerramento do prog
        else:  # caso nao seja um valor numerico
            # mostre essa frase de erro
            print(f'\033[0;31mErro! Digite um numero inteiro válido!\033[m')
        if ok:  # se o ok for True
            break  # pare o programa
    return valor  # retorne o valor de n
