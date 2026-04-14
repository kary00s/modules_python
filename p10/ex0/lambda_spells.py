def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_data = sorted(artifacts, key=lambda dic: dic["power"], reverse=True)
    return sorted_data


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtred_data = filter(lambda f:  f["power"] >= min_power, mages)
    return list(filtred_data)

def spell_transformer(spells: list[str]) -> list[str]:
    transformeted_data = map(lambda spl :  f"*{spl}*", spells)
    return list(transformeted_data)

def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x["power"])
    min_power = min(mages, key=lambda x: x["power"])
    max_min = [max_power.get("power"), min_power.get("power")]
    avg =  sum(max_min) / 2

    return {
        "max_power": max_min[0],
        "min_power": max_min[1],
        "avg_power": avg
    }

def main():

    artifact = [

             {"name": "Crystal Orb",
             "power": 85, 
             "type": "selver"},
            
            {"name": "Fire Staff",
             "power": 92, 
             "type": "selver"},
            ]

    print("Testing artifact sorter...")
    sorted_data = artifact_sorter(artifact)
    first = sorted_data[0]
    second = sorted_data[1]
    print(first["name"], 
          f"({first["power"]}", 
          " comes before ", 
          second["name"], 
          f"({second["power"]})\n")
    

    lst = ["fireball", "heal", "shield"]
    transformed_data = spell_transformer(lst)
    print("Testing spell transformer...")
    for item in transformed_data:
        print(item, end=" ")
    print()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)