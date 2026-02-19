"""
Retrosynthesis function implemented using AiZynthExpander

Due to excessive data volume, it is no longer displayed in this repo.
If needed, download AiZynthExpander data at https://molecularai.github.io/aizynthfinder/aizynthfinder.html
"""

import pandas as pd
from aizynthfinder.aizynthfinder import AiZynthExpander  # , AiZynthFinder

filename = "cases_data/retrosynthesis/public_data/config.yml"

def retrosynthesis(products):
    filename = "config.yml"
    expander = AiZynthExpander(configfile=filename)
    expander.expansion_policy.select("uspto")
    reactions = expander.do_expansion(products)
    candidate_routes = []
    for i, reaction_tuple in enumerate(reactions):
        reaction = reaction_tuple[0]


        res = {
            "index": i,
            "reactants": [mol.smiles for mol in reaction.reactants[0]],
            "scores": reaction.metadata.get("scores", 0),
            "template_hash": reaction.metadata.get("template_hash", "unknown")
        }

        reactants = '.'.join(res["reactants"])
        candidate_routes.append(reactants)
        print("Reactants: ", reactants)
    return candidate_routes

