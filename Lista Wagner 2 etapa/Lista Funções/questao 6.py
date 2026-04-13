def aplicar_imposto(preco):
    return preco * 1.15

preco = float(input('Digite o preço do produto: '))
preco_final = aplicar_imposto(preco)

print(f'Preço com imposto: {preco_final:.2f}')