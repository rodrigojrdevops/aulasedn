import requests

url = "https://randomuser.me/api/"

#fazendo uma requisição get
response = requests.get(url)

if response.status_code == 200:
    
    data = response.json()
    
    user = data['results'][0]
    name = f"{user['name']['title']} {user['name']['first']} {user['name']['last']}"
    email = user['email']
    country = user['location']['country']
    
    print(f"Nome: {name}")
    print(f"Email: {email}")
    print(f"pais: {country}")
else:
    print("Erro de chamada API: {response.status_code} ")
    
        
    
