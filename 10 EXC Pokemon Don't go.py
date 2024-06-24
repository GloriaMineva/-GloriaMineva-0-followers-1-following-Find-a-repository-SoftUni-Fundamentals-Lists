def valid_index(pokemons, current_idx, calculation):
    current_pokemon_value = pokemons[current_idx]
    calculation += current_pokemon_value
    del pokemons[current_idx]
    pokemons = [element + current_pokemon_value if element <= current_pokemon_value else element - current_pokemon_value for element in pokemons]
    return pokemons, calculation
def small_index(pokemons, calculation):
    current_pokemon_value = pokemons[0]
    last_pokemon = pokemons[-1]
    calculation += current_pokemon_value
    del pokemons[0]
    pokemons.insert(0, last_pokemon)
    pokemons = [element + current_pokemon_value if element <= current_pokemon_value else element - current_pokemon_value for element in pokemons]
    return pokemons, calculation

def big_index(pokemons, calculation):
    current_pokemon_value = pokemons[-1]
    first_pokemon = pokemons[0]
    calculation += current_pokemon_value
    del pokemons[-1]
    pokemons.append(first_pokemon)
    pokemons = [element + current_pokemon_value if element <= current_pokemon_value else element - current_pokemon_value for element in pokemons]
    return pokemons, calculation



pokemons = list(map(int, input().split()))
calculation = 0
while pokemons:
    current_idx = int(input())
    if 0 <= current_idx < len(pokemons):
        pokemons, calculation = valid_index(pokemons, current_idx, calculation)
    elif current_idx < 0:
        pokemons, calculation = small_index(pokemons, calculation)
    else:
        pokemons, calculation = big_index(pokemons, calculation)
print(calculation)
