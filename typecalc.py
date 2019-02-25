import json

with open("types.json", "r") as read_file:
    types = json.load(read_file)

pogo_multipliers = {
    "se": 1.6,
    "neutral": 1,
    "nve": 0.625,
    "immune": 0.625*0.625
}

for pkmntype in types:
    if pkmntype["type"] == "Fighting":
        print("Super effective vs: " + str(pkmntype["deals_damage"]["se"]))
        print("Neutral vs: " + str(pkmntype["deals_damage"]["neutral"]))
        print("Not very effective vs: " + str(pkmntype["deals_damage"]["nve"]))