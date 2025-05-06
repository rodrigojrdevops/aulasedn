#Contar pares e impares

pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'sair' para encerrar): ")
    
    if entrada.lower() == 'sair':
        print("Encerrando o programa.")
        break
    
    try:
        
        numero = int(entrada)
        
        if numero % 2 == 0:
           print(f"O número {numero} é par.")
           pares +=1
        else:
            print(f"O número {numero} é ímpar.")
            pares +=1
            
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")
        
    print(n/resultados
           print(f"Quantidade de números pares: {pares}")
           print(f"Quantidade de números ímpares: {impares}")
        