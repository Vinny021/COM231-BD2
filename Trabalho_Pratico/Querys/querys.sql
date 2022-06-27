CREATE TABLE pokemons (
    dex_num int primary key,
    name char(20) not null,
    height numeric not null,
    weight numeric not null,
    evolution_familly_id int not null,
    type1 char(10) not null,
    type2 char(10)
);

CREATE TABLE sprites (
    pokemon_id int primary key,
    default_sprite char(150) not null,
    shiny_sprite char(150),
    FOREIGN KEY(pokemon_id) REFERENCES pokemons(dex_num) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE pokemon_families (
    family_id int primary key,
    family_species char(20) not null,
    FOREIGN KEY(family_id) REFERENCES pokemons(dex_num) ON DELETE CASCADE ON UPDATE CASCADE   
);

CREATE TABLE regions (
    id int primary key,
    name char(20),
    id_first_pokemon int not null,
    id_last_pokemon int not null
);

CREATE FUNCTION pokemon_evolutions(id int)
  RETURNS TABLE (pokemon_id text, pokemon_name text)
AS
$body$
  SELECT dex_num, name  FROM pokemons
  WHERE evolution_familly_id = $1 
$body$
language sql;

CREATE VIEW pokemons_infos AS 
    SELECT 
        p.name as "Nome", 
        p.type1 as "Tipo Principal",
        p.type2 as "Tipo Secundário",
        r.name as "Região" FROM 
    pokemons p INNER JOIN regions r ON  
        dex_num >= id_first_pokemon AND dex_num <= id_last_pokemon;

CREATE ROLE "User";
GRANT SELECT ON pokemons_infos TO "User";
GRANT EXECUTE ON FUNCTION pokemon_evolutions TO "User";

CREATE ROLE "Gerenciador"
GRANT 
    SELECT, UPDATE, DELETE, INSERT 
ON 
    pokemon_families, pokemons, regions, sprites 
TO "Gerenciador";

CREATE ROLE "Admin";
GRANT ALL ON ALL TABLES IN SCHEMA "public" TO "Admin";