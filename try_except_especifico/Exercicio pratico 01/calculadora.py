while True:
    try:
        #números com interação do usuário
        num1 = float(input("digite o primeiro número: "))
        num2 = float(input("digite o segundo número: "))
        
        operacao = input("Digite a operação (+, -, *, / ):")
        if operacao == "+":
            
        elif operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
            if num2 == 0:
                raise ZeroDivisionError("Não é possível dividir por zero")
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida")
        
        print(f"Resultado: {resultado}")
        break
    
    except ValueError as e:
            
            if str(e) == "Operação inválida":
                print(e)
            else:
                print("Erro: Digite um número válido")
                
    except ZeroDivisionError as e:
        print(e)