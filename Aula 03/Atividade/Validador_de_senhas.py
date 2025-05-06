#Verificar se a senha é forte tendo 8 digítos ao menos um número

while True:
    senha = input("Digite sua senha( ou 'sair' para encerrar)")
    
    #Verifica se o usuário quer sair
    if senha.lower() == 'sair':
        print("Encerrando o programa.")
        break
    
    tem_numero = False
    
    #Verifica se tem ao menos um número
    for char in senha:
        if char.isdigit():
            tem_numero = True
            break
        
        #Precisa ter 8 caracteries e um número
        
        if len(senha) < 8:
            print("A senha precisa ter 8 caracteres e um número.")
        elif not tem_numero:
            print("A senha é fraca: Precisa ter ao menos um núemro!:)")
            
            