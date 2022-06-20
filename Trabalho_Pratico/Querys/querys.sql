CREATE TABLE pokemons (
    dex_num int primary key,
    name char(20) not null,
    height numeric not null,
    weight numeric not null,
    type1 char(10) not null,
    type2 char(10)
);

CREATE TABLE sprites (
    pokemon_id int primary key,
    default_sprite char(150) not null,
    shiny_sprite char(150),
    FOREIGN KEY(pokemon_id) REFERENCES pokemons(dex_num) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE pokemon_evolutions (
    id char(20) primary key,
    base_form_id int not null,
    second_form_id int not null,
    third_form_id int not null,
    FOREIGN KEY(base_form_id) REFERENCES pokemons(dex_num) ON DELETE CASCADE ON UPDATE CASCADE    
    FOREIGN KEY(second_form_id) REFERENCES pokemons(dex_num) ON DELETE CASCADE ON UPDATE CASCADE    
    FOREIGN KEY(third_form_id) REFERENCES pokemons(dex_num) ON DELETE CASCADE ON UPDATE CASCADE    
);

CREATE TABLE regions (
    name char(20) primary key,
    id_first_pokemon int not null,
    id_last_pokemon int not null,
    FOREIGN KEY(id_first_pokemon) REFERENCES pokemons(dex_num) ON DELETE CASCADE ON UPDATE CASCADE
    FOREIGN KEY(id_last_pokemon) REFERENCES pokemons(dex_num) ON DELETE CASCADE ON UPDATE CASCADE
);
