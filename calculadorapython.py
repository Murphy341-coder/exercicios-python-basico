def calcular(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return num1 / num2
    else:
        raise ValueError("Operação inválida.")

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        resultado = calcular(num1, num2, operacao)
        print(f"Resultado: {resultado}")
        break

    except ValueError as e:
        print(f"Erro: {e}")
    except ZeroDivisionError as e:
        print(f"Erro: {e}")
    except Exception:
        print("Erro desconhecido. Tente novamente.")
