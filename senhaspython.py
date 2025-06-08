def senha_forte(senha):
    return len(senha) >= 8 and any(char.isdigit() for char in senha)

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    if senha.lower() == 'sair':
        break

    if senha_forte(senha):
        print("Senha válida e forte.")
        break
    else:
        print("Senha fraca. Deve ter pelo menos 8 caracteres e conter pelo menos um número.")
