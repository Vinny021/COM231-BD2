import requests
import json

from bd.modelo import EvolutionM, PokemonM, RegionM, SpriteM
from bd.view import View

def getPokemonNameById(id):
    url = "https://pokeapi.co/api/v2/pokemon/" + str(id)
    request = requests.get(url)
    pokemonJson = json.loads(request.content)
    return pokemonJson['name'].capitalize()

def getPokemon(id):
    url = "https://pokeapi.co/api/v2/pokemon/" + str(id)
    request = requests.get(url)
    pokemonJson = json.loads(request.content)
    return pokemonJson

def getPokemonSpecie(id):
    url = "https://pokeapi.co/api/v2/pokemon-species/" + str(id)
    request= requests.get(url)
    pokemonSpecieJson = json.loads(request.content)

    evolutionJson = {"id": None, "chain": {"species": { "name": None}}}

    if(pokemonSpecieJson['evolution_chain'] == None):
        pokemonJson = getPokemon(id)
        evolutionJson['id'] = id
        evolutionJson['chain']['species']['name'] = pokemonJson['name']
    else:
        evolutionUrl = pokemonSpecieJson['evolution_chain']['url']
        request = requests.get(evolutionUrl)
        evolutionJson = json.loads(request.content)
    
    return evolutionJson

def getRegion(id):
    url = "https://pokeapi.co/api/v2/generation/" + str(id)
    request = requests.get(url)
    regionJson = json.loads(request.content)
    return regionJson

def dataloadPokemon(pokemonJson, specieJson):
    formatedHeight = "{:.2f}".format(float((pokemonJson['height']) * 0.1))
    formatedWeight = "{:.2f}".format(float((pokemonJson['weight']) * 0.1))
    pokemonValues = [
        int(pokemonJson['id']),
        pokemonJson['name'].capitalize()[:20],
        float(formatedHeight),
        float(formatedWeight),
        int(specieJson['id']),
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

def dataloadEvolution(specieJson):
    specieValues = [
        int(specieJson['id']),
        specieJson['chain']['species']['name'].capitalize()
    ]

    evolution = EvolutionM.createEvolution(specieValues)
    status = EvolutionM.registerEvolution(evolution)

    if(status != 'sucesso'):
        return "Evolution do pokemon especie com id: " + str(specieJson['id'])

    view.printStatus(status)

def dataloadRegion(regionJson):
    first_id = int(regionJson['pokemon_species'][0]['url'].split('/')[6])
    last_id = first_id + len(regionJson['pokemon_species']) - 1
    regionValues = [
        int(regionJson['id']),
        regionJson['main_region']['name'].capitalize(),
        first_id,
        last_id
    ]

    region = RegionM.createRegion(regionValues)
    status = RegionM.registerRegion(region)

    if(status != 'sucesso'):
        return "Já existe região com nome: " + str(regionJson['main_region']['name'].capitalize())

    view.printStatus(status)


def dataloadPokemons(minValue, maxValue):
    erros = []
    for id in range (int(minValue), int(maxValue)):
        pokemonJson = getPokemon(id)
        speciesJson = getPokemonSpecie(id)
        
        error = dataloadPokemon(pokemonJson, speciesJson)
        if(error != None):
            erros.append(error)
        
        error = dataloadSprit(pokemonJson)
        if(error != None):
            erros.append(error)

        error = dataloadEvolution(speciesJson)
        if(error != None):
            erros.append(error)

    if(len(erros) != 0):
        print('Erro no registro dos seguintes pokemons: ', erros)

def dataloadRegions(minValue, maxValue):
    erros = []
    for id in range(int(minValue), int(maxValue)):
        regionJson = getRegion(id)

        error = dataloadRegion(regionJson)
        if(error != None):
            erros.append(error)
    
    if(len(erros) != 0):
        print('Erro no registro das seguintes regiões: ', erros)
        

def deletePokemons(minValue, maxValue):
    erros = []
    for id in range (int(minValue), int(maxValue)):
        status = PokemonM.deletePokemon(id)
        if(status != 'sucesso'):
            erros.append(id)

        pokemonName = getPokemonNameById(id)
        EvolutionM.deleteEvolution(pokemonName)
        
        view.printStatus(status)
    
    if(len(erros) != 0):
        print('Erro no registro dos seguintes pokemons: ', erros)

def deleteRegions(minValue, maxValue):
    erros = []

    for id in range(int(minValue), int(maxValue)):
        status = RegionM.deleteRegion(id)
        if(status != 'sucesso'):
            erros.append(id)
        
        view.printStatus(status)
    
    if(len(erros) != 0):
        print('Região não existe')

def menu():
        print("MENU")
        print("1. Dataload de Pokemons")
        print("2. Remover Range Pokemons")
        print("3. Dataload de Região")
        print("4. Remover Regiões")
        print("5. Sair")
        
        option = int(input("Digite o numero da opcao desejada: "))

        return option

if __name__ == "__main__":
    view = View()

    opcao = menu()

    while opcao != 5:
        if opcao == 1:
            minValue = input("Digite o id inicial: ")
            maxValue = input("Digite o id limite (Não é incluido): ")
            dataloadPokemons(minValue, maxValue)
        if opcao == 2:
            minValue = input("Digite o id inicial: ")
            maxValue = input("Digite o id limite (Não é incluido): ")
            deletePokemons(minValue, maxValue)
        if opcao == 3:
            print("Região de 1 até 8\n")
            minValue = input("Digite o id inicial: ")
            maxValue = input("Digite o id limite (Não é incluido): ")
            dataloadRegions(minValue, maxValue)
        if opcao == 4:
            print("Região de 1 até 8\n")
            minValue = input("Digite o id inicial: ")
            maxValue = input("Digite o id limite (Não é incluido): ")
            deleteRegions(minValue, maxValue)

        opcao = menu()


    
    
