from decimal import *
from bd.config import config
from psycopg2.extensions import AsIs
from datetime import datetime

class PokemonM():
    def __init__(self, dex_num, name, height, weight, evolution_familly_id, type1, type2):
        self.dex_num = dex_num
        self.name = name
        self.height = height
        self.weight = weight
        self.evolution_familly_id = evolution_familly_id
        self.type1 = type1
        self.type2 = type2

    def createPokemon(valuesList):
        pokemon = PokemonM(
            int(valuesList[0]),
            valuesList[1],
            float(valuesList[2]),
            float(valuesList[3]),
            int(valuesList[4]),
            valuesList[5],
            valuesList[6]
        )
        return pokemon
    
    def registerPokemon(pokemon):
        string_sql = 'INSERT INTO public.pokemons(dex_num, name, height, weight, evolution_familly_id, type1, type2) VALUES (%s, %s, %s, %s, %s, %s, %s);'
        new_insert = (pokemon.dex_num, pokemon.name, pokemon.height, pokemon.weight, pokemon.evolution_familly_id, pokemon.type1, pokemon.type2)
        status = config.alteraBD(config, string_sql, new_insert)
        return status
    
    def deletePokemon(id):
        string_sql = 'DELETE FROM public.pokemons WHERE dex_num = %s;'
        status = config.alteraBD(config, string_sql, [id])

        return status
    
    def selectPokemon(id):
        string_sql = 'SELECT * FROM public.pokemons WHERE dex_num = %s;'
        pokemons = config.consultaBD(config, string_sql, [id])
        if(len(pokemons[1]) != 0):
            pokemon = PokemonM.createPokemon(pokemons[1][0])
            return pokemon 
        else: 
            return None
    
    def updatePokemon(l):
        string_sql = "UPDATE public.pokemons SET %s = %s WHERE dex_num = %s;"
        params = ((AsIs[l[1]]), int(l[2]), int(l[0]))
        status = config.alteraBD(config, string_sql, params)
        return status

class SpriteM():
    def __init__(self, pokemon_id, default_sprite, shiny_sprite):
        self.pokemon_id = pokemon_id
        self.default_sprite = default_sprite
        self.shiny_sprite = shiny_sprite
    
    def createSprite(valuesList):
        sprite = SpriteM(
            int(valuesList[0]),
            valuesList[1],
            valuesList[2]
        )        
        return sprite
    
    def registerSprite(sprite):
        string_sql = 'INSERT INTO public.sprites(pokemon_id, default_sprite, shiny_sprite) VALUES (%s, %s, %s);'
        new_insert = (sprite.pokemon_id, sprite.default_sprite, sprite.shiny_sprite)
        status = config.alteraBD(config, string_sql, new_insert)
        return status

    def deleteSprite(id):
        string_sql = 'DELETE FROM public.sprites WHERE pokemon_id = %s;'
        status = config.alteraBD(config, string_sql, [id])
        return status

class EvolutionM():
    def __init__(self, family_id, family_species):
        self.family_id = family_id
        self.family_species = family_species

    def createEvolution(valuesList):
        evolution = EvolutionM(
            int(valuesList[0]),
            valuesList[1]
        )
        return evolution
    
    def registerEvolution(evolution):
        string_sql = 'INSERT INTO public.pokemon_evolutions(family_id, family_species) VALUES (%s, %s);'
        new_insert = (evolution.family_id, evolution.family_species)
        status = config.alteraBD(config, string_sql, new_insert)
        return status
    
    def deleteEvolution(family_species):
        string_sql = 'DELETE FROM public.pokemon_evolutions WHERE pokemon_id = %s;'
        status = config.alteraBD(config, string_sql, [family_species])
        return status