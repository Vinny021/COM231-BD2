# ALUNOS
# 
# João Pedro Marcelino de Sousa - 2018006008
# Vinícius Barbosa - 2020009867

from datetime import datetime
from decimal import *

class View():
    def inicio(self):
        return self.menu()

    def menu(self):
        print("MENU")
        print("1. Cadastrar Pokemon")
        print("2. Deletar Pokemon")
        print("3. Consultar Pokemon")
        print("4. Sair")
        option = int(input("Digite o numero da opcao desejada: "))
        return option

    def inputsPokemon(self):
        dex_num = input("Digite o numero do pokemon: ")
        name = input("Digite o nome do pokemon: ")
        height = input("Digite a altura do pokemon: ")
        weight = input("Digite o peso do pokemon: ")
        type1 = input("Digite o primeiro tipo do pokemon: ")
        type2 = input("Digite o segundo tipo do pokemon: ")
        
        values = [int(dex_num), name, float(height), float(weight), type1, type2]
        return values

    
    def printPokemon(self, pokemon):
        if(pokemon is not None):
            print("Numero do Pedido: " + str(pokemon.dex_num))
            print("Nome do Pokemon: " + pokemon.name)
            print("Altura do Pokemon: " + str(pokemon.height))
            print("Peso do Pokemon: " + str(pokemon.weight))
            print("Tipo do Pokemon: " + pokemon.type1)
            if(pokemon.type2):
                print("Segundo Tipo do Pokemon: " + pokemon.type2)
        else:
            print("Consulta vazia")

    def getPokemonId(self):
        pokemonId = int(input('Digite o numero do pokemon: '))
        return pokemonId

    def printStatus(self, status):
        if (status == 'sucesso'):
            print("Comando executado no banco de dados com sucesso")
        else:
            print(status)