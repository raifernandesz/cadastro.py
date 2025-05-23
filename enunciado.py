

print("faca o cadastro ")
nome_usuario = input("Crie seu nome de usuario")
senha = input("Crie sua senha: ")


print("Faça o login")
nome_login = input("Digite seu nome de usuario: ")
senha_login = input("Digite sua senha: ")


while nome_login  != nome_usuario or senha_login != senha:
     print("nome de usuario ou senha incorretos")
     nome_login = input("Digite seu nome de usuario")
     senha_login = input("Digite sua senha: ")

print(" Login bem sucedido !")