import random
import time

numeros_aleatorios = random.randint(0,100)
print(f"Núemros aleatórios: {numeros_aleatorios}")  

inicio = time.time()
for _ in range(1000000):
    pass
fim = time.time()
print(f"Tempo de execução: {fim - inicio:.6f} segundos")                   
