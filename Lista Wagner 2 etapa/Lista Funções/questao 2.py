def aplicar_desconto(preco):
    return preco * 0.9

preco = float(input('Digite o preço do produto: '))
preco_com_desconto = aplicar_desconto(preco)

print(f'Preço com desconto: {preco_com_desconto:.2f}')