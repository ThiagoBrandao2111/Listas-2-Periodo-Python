def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Erro: não é possível dividir por zero.'


# Teste da função
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
resultado = dividir(numero1, numero2)

print(resultado)


Listas-2-Periodo-Python
Atividade do 2° período do curso de Sistemas de Informação