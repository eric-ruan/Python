try:
    a = int(input('Digite um número: '))
    b = int(input('DIgite outro número: '))
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou!!')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero')
except KeyboardInterrupt:
    print('O úsuario prefiriu não informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {a/b:.1f}')
finally:
    print('Volte sempre')