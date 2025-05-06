def calculo_gorjeta(Valor_conta, porcentagem_gorjeta)
    """Esta função calcula o valor da gorjeta baseado no total da conta e da porcentagem.
    
       Parametros:
          Valor conta (float): O valor total da conta
          porcentagem_gorjeta *(float): Porcentagem da gorjeta
       Retorna:
        float: O valor da gorjeta calculada   
        
        
    """
    
    gorjeta = Valor_conta * porcentagem_gorjeta / 100
    
    return round(gorjeta, 2)


total_conta = float(input("Digite o valor total da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))


valor_gorjeta = calculo_gorjeta(total_conta, porcentagem)
print(f"Para uam conta de {total_conta:.2f} a gorjeta de {porcentagem}% tem o valor de R${valor_gorjeta:.2f}
)