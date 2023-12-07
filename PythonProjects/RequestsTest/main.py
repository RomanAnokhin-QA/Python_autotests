import requests

response=requests.post(url='https://api.pokemonbattle.me:9104/pokemons', 
              headers={'Content-Type': 'application/json','trainer_token':'79d00d24e704b84bf12fbd5f21a10dce'},
              json={
                  "name": "gerald",
                  "photo": "https://dolnikov.ru/pokemons/albums/001.png"
                   }, timeout=5)
print(f'Code:{response.status_code} - {response.reason}. Message: {response.text}')

response=requests.put(url='https://api.pokemonbattle.me:9104/pokemons', 
              headers={'Content-Type': 'application/json','trainer_token':'79d00d24e704b84bf12fbd5f21a10dce'},
              json={
                   "pokemon_id": "21370",
                   "name": "rumpel",
                   "photo": "https://dolnikov.ru/pokemons/albums/008.png"
                    }, timeout=5)
print(f'Code:{response.status_code} - {response.reason}. Message: {response.text}')

response=requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball', 
              headers={'Content-Type': 'application/json','trainer_token':'79d00d24e704b84bf12fbd5f21a10dce'},
              json={
                   "pokemon_id": "21371"
                   }, timeout=5)
print(f'Code:{response.status_code} - {response.reason}. Message: {response.text}')

