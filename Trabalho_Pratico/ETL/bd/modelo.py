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

class EvolutionFamiliesM():
    def __init__(self, family_id, family_species):
        self.family_id = family_id
        self.family_species = family_species

    def createEvolution(valuesList):
        evolution = EvolutionFamiliesM(
            int(valuesList[0]),
            valuesList[1]
        )
        return evolution
    
    def registerEvolution(evolution):
        string_sql = 'INSERT INTO public.pokemon_families(family_id, family_species) VALUES (%s, %s);'
        new_insert = (evolution.family_id, evolution.family_species)
        status = config.alteraBD(config, string_sql, new_insert)
        return status
    
    def deleteEvolution(family_species):
        string_sql = 'DELETE FROM public.pokemon_families WHERE pokemon_id = %s;'
        status = config.alteraBD(config, string_sql, [family_species])
        return status

class RegionM():
    def __init__(self ,id, name, id_first_pokemon, id_last_pokemon):
        self.id = id
        self.name = name
        self.id_first_pokemon = id_first_pokemon
        self.id_last_pokemon = id_last_pokemon
    
    def createRegion(valuesList):
        region = RegionM(
            int(valuesList[0]),
            valuesList[1],
            int(valuesList[2]),
            int(valuesList[3])
        )
        return region
    
    def registerRegion(region):
        string_sql = 'INSERT INTO public.regions(id, name, id_first_pokemon, id_last_pokemon) VALUES (%s, %s, %s ,%s);'
        new_insert = (region.id, region.name, region.id_first_pokemon, region.id_last_pokemon)
        status = config.alteraBD(config, string_sql, new_insert)
        return status
    
    def deleteRegion(id):
        string_sql = 'DELETE FROM public.regions WHERE id = %s;'
        status = config.alteraBD(config, string_sql, [id])
        return status