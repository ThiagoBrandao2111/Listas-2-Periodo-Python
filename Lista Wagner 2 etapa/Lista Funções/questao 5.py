def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc < 25:
        return 'Peso normal'
    else:
        return 'Acima do peso'

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = calcular_imc(peso, altura)

print(f'IMC: {imc:.2f}')
print(f'Classificação: {classificar_imc(imc)}')