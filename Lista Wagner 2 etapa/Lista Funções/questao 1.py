def autenticador(email, senha):
    if email == 'admin' and senha == 'admin':
        return True
    else:
        return False

email = input('Digite o email: ')
senha = input('Digite a senha: ')

resultado = autenticador(email, senha)

print(resultado)