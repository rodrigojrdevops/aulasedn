#registrar as notas dos alunos

notas = []
numero_de_alunos = 0

while True:
    entrada = input("Digite a nota do aluno (ou 'sair' para encerrar): ")
    
    #verifica se o professor quer encerrar
    if entrada.lower() == 'sair':
        break
    
    try:
        nota = float(entrada)
        
        if 0 <= nota <= 10:
            notas.append(nota)
            numero_de_alunos += 1
        else:
            print("Nota inválida. Digite uma nota entre 0 e 10.")
            
    except ValueError:
        print("Entrada inválida. Digite um número válido entre 0 a 10 ou 'fim' ")   
        
    #calcula e exibe a média das notas
    if numero_de_alunos > 0:
        media = sum(notas) / numero_de_alunos
        print(f"A média das notas é: {media:.2f}")
        print(f"O número de alunos é: {numero_de_alunos}")
    else:
        print("Nenhuma nota foi registrada.")    
        