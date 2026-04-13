try:
    numero = float(input('Digite um número: '))
    print(f'Você digitou: {numero:.2f}')

except ValueError:
    print('Erro: você deve digitar um número válido.')