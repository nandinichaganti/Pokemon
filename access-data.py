import requests
import json

def get_all_pokemon_details():
    base_url = "https://pokeapi.co/api/v2/pokemon?limit=2000"
    response = requests.get(base_url)
    if response.status_code != 200:
        print("Failed to retrieve Pokémon list:", response.status_code)
        return
    pokemon_list = response.json()["results"]
    useful_fields = [
        "name",
        "id",
        "abilities",
        "types",
        "stats",
        "base_experience",
        "height",
        "weight"
    ]
    all_pokemon_data = []
    for pokemon in pokemon_list:
        poke_url = pokemon["url"]
        poke_resp = requests.get(poke_url)
        if poke_resp.status_code == 200:
            data = poke_resp.json()
            useful_data = {field: data.get(field) for field in useful_fields}
            all_pokemon_data.append(useful_data)
            print(f"Collected: {useful_data['name']}")
        else:
            print(f"Failed to retrieve data for {pokemon['name']}: {poke_resp.status_code}")
    with open("all_pokemon_useful_data.json", "w", encoding="utf-8") as f:
        json.dump(all_pokemon_data, f, indent=2)
    print(f"Saved details for {len(all_pokemon_data)} Pokémon to all_pokemon_useful_data.json")

if __name__ == "__main__":
    get_all_pokemon_details()