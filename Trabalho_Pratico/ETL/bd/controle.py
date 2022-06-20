# ALUNOS
# 
# João Pedro Marcelino de Sousa - 2018006008
# Vinícius Barbosa - 2020009867

from view import View
from modelo import PokemonM

class Controle:
    def __init__(self):
        self.view = View()

    def inicio(self):
        opcao = self.view.inicio()

        while opcao != 4:
            if opcao == 1:
                l = self.view.inputsPokemon()
                pokemon = PokemonM.createPokemon(l)
                status = PokemonM.registerPokemon(pokemon)
                self.view.printStatus(status)
            if opcao == 2:
                id = self.view.getPokemonId()
                status = PokemonM.deletePokemon(id)
                self.view.printStatus(status)
            if opcao == 3:
                id = self.view.getPokemonId()
                pokemon = PokemonM.selectPokemon(id)
                self.view.printPokemon(pokemon)
            opcao = self.view.menu()

if __name__ == "__main__":
    main = Controle()
    main.inicio()
