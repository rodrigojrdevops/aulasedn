def validar_palindromo(texto):
    """Verifica se o texto é palindromo
    Parm:
        texto(str
    return:
        bool: True or False
    """
    
    
    texto_precessado = ''
    
    for caractere in texto.lower():
        if caractere.isalnum
            texto_precessado += caractere
            
    return texto_precessado == texto_precessado[::-1]


    texto = input("Digite uma frase ou palavra: ")
    resultado = validar_palindromo(texto)
    
    if resultado:
        resposta = "sim"
    else:
        resposta = "não"
        
        print(f"A frase ou palavra '{texto}' é um palindromo? {resposta}")