import requests

response = requests.get("https://www.python.org")

if response.status_code == 200:
    print("Requisição bem sucedida!")
    
    print(response.text[:100])  
else:
    print(F"Requisição falhou {response.status_code}")
    
    # Exemplo de requisição POST