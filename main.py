from NUMEROS import Leiaint

while True:
    try:
        n = Leiaint('Digite um numero inteiro: ')
    except ImportError:
        print('Erro ao importar o modulo. ')
    except (ValueError, TypeError):
        print('Digite um numero inteiro válido: ')
    else:
        print(f'O numero que você digitou foi {n}')
    finally:
        print('Programa Encerrado!')
        break
