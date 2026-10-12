import json
from neo4j import GraphDatabase

# Neo4j connection details
uri = "neo4j://127.0.0.1:7687"
user = "neo4j"
password = "test1234"

driver = GraphDatabase.driver(uri, auth=(user, password))

def create_graph(tx, pokemon, type_names, evolves_from):
    # Create Pokemon node
    tx.run(
        """
        MERGE (p:Pokemon {name: $name})
        SET p.id = $id, p.height = $height, p.weight = $weight, p.base_experience = $base_experience,
            p.hp = $hp, p.attack = $attack, p.defense = $defense,
            p.special_attack = $special_attack, p.special_defense = $special_defense, p.speed = $speed
        """,
        **pokemon
    )
    # Create Type nodes and relationships
    for t in type_names:
        tx.run(
            """
            MERGE (type:Type {name: $type_name})
            WITH type
            MATCH (p:Pokemon {name: $pokemon_name})
            MERGE (p)-[:HAS_TYPE]->(type)
            """,
            type_name=t,
            pokemon_name=pokemon["name"]
        )
    # Create evolution relationship if applicable
    if evolves_from:
        tx.run(
            """
            MATCH (p1:Pokemon {name: $from_name}), (p2:Pokemon {name: $to_name})
            MERGE (p1)-[:EVOLVES_TO]->(p2)
            """,
            from_name=evolves_from,
            to_name=pokemon["name"]
        )

def extract_stats(stats):
    stat_map = {
        "hp": 0,
        "attack": 0,
        "defense": 0,
        "special-attack": 0,
        "special-defense": 0,
        "speed": 0
    }
    for stat in stats:
        name = stat["stat"]["name"]
        if name in stat_map:
            stat_map[name.replace("-", "_")] = stat["base_stat"]
    return stat_map

with open("all_pokemon_useful_data.json", encoding="utf-8") as f:
    pokemons = json.load(f)

# Prepare all Pokémon names for evolution lookup
pokemon_names = set(p["name"] for p in pokemons)

with driver.session() as session:
    for p in pokemons:
        # Extract types
        type_names = [t["type"]["name"] for t in p.get("types", [])]
        # Extract stats
        stats = extract_stats(p.get("stats", []))
        # Prepare properties
        pokemon_props = {
            "name": p.get("name"),
            "id": p.get("id"),
            "height": p.get("height"),
            "weight": p.get("weight"),
            "base_experience": p.get("base_experience"),
            **stats
        }
        # Evolution: if name contains '-', link to base form (before '-') if it exists
        evolves_from = None
        if "-" in p["name"]:
            base_name = p["name"].split("-")[0]
            if base_name in pokemon_names:
                evolves_from = base_name
        session.execute_write(create_graph, pokemon_props, type_names, evolves_from)

driver.close()