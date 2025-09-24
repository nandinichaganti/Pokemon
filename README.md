# Pokemon

## Project Summary

This project fetches Pokémon data from the PokéAPI, processes it, and builds a graph database in Neo4j to enable advanced querying and visualization of Pokémon, their types, and evolution relationships.

### access-data.py
- Fetches all Pokémon from the PokéAPI.
- For each Pokémon, retrieves details such as name, id, abilities, types, stats, base_experience, height, and weight.
- Stores all this data in a JSON file called `all_pokemon_useful_data.json`.

### create-graph.py
- Reads the Pokémon data from `all_pokemon_useful_data.json`.
- Connects to a Neo4j database.
- For each Pokémon:
	- Creates a `Pokemon` node with properties (name, id, height, weight, base_experience, and stats).
	- Creates `Type` nodes and `HAS_TYPE` relationships for each Pokémon’s types.
	- If the Pokémon’s name contains a hyphen (`-`), creates an `EVOLVES_TO` relationship from the base form (before the hyphen) to the current Pokémon, if the base form exists.
- Uses the updated Neo4j driver method `execute_write` for transactions.

This setup allows you to build a graph database of Pokémon, their types, and their evolution relationships for advanced querying and visualization.