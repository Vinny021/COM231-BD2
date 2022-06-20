import requests
import json

from bd.modelo import PokemonM, SpriteM
from bd.view import View

def getPokemon(id):
    url = "https://pokeapi.co/api/v2/pokemon/" + str(id)
    request = requests.get(url)
    pokemonJson = json.loads(request.content)
    return pokemonJson

def dataloadPokemon(pokemonJson):
    pokemonValues = [
        int(pokemonJson['id']),
        pokemonJson['name'].capitalize(),
        float(pokemonJson['height']),
        float(pokemonJson['weight']),
        pokemonJson['types'][0]['type']['name'].capitalize()
    ]

    if(len(pokemonJson['types']) > 1):
        pokemonValues.append(pokemonJson['types'][1]['type']['name'].capitalize())
    else:
        pokemonValues.append(None)
    
    pokemon = PokemonM.createPokemon(pokemonValues)
    status = PokemonM.registerPokemon(pokemon)

    if(status != 'sucesso'):
        return "Pokemon com id: " + str(pokemonJson['id'])

    view.printStatus(status)

def dataloadSprit(pokemonJson):
    spriteValues = [
        int(pokemonJson['id']),
        pokemonJson['sprites']['front_default'],
        pokemonJson['sprites']['front_shiny']
    ]

    sprite = SpriteM.createSprite(spriteValues)
    status = SpriteM.registerSprite(sprite)

    if(status != 'sucesso'):
        return "Sprite do pokemon com id: " + str(pokemonJson['id'])

    view.printStatus(status)

def dataloadPokemons(minValue, maxValue):
    erros = []
    for id in range (int(minValue), int(maxValue)):
        pokemonJson = getPokemon(id)
        
        error = dataloadPokemon(pokemonJson)
        if(error != None):
            erros.append(error)
        
        error = dataloadSprit(pokemonJson)
        if(error != None):
            erros.append(error)

    if(len(erros) != 0):
        print('Erro no registro dos seguintes pokemons: ', erros)

def deletePokemons(minValue, maxValue):
    erros = []
    for id in range (int(minValue), int(maxValue)):
        status = PokemonM.deletePokemon(id)
        if(status != 'sucesso'):
            erros.append(id)
        view.printStatus(status)
    
    if(len(erros) != 0):
        print('Erro no registro dos seguintes pokemons: ', erros)

def menu():
        print("MENU")
        print("1. Dataload de Pokemons")
        print("2. Remover Range Pokemons")
        print("3. Sair")
        
        option = int(input("Digite o numero da opcao desejada: "))

        return option

if __name__ == "__main__":
    view = View()

    opcao = menu()

    while opcao != 3:
        if opcao == 1:
            minValue = input("Digite o id inicial: ")
            maxValue = input("Digite o id limite (Não é incluido): ")
            dataloadPokemons(minValue, maxValue)
        if opcao == 2:
            minValue = input("Digite o id inicial: ")
            maxValue = input("Digite o id limite (Não é incluido): ")
            deletePokemons(minValue, maxValue)

        opcao = menu()


    
    
