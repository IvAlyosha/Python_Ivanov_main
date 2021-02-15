person_1 = {
    'name': 'Elf',
    'health': 100,
    'damage': 50,
    'armor': 4
}
person_2 = {
    'name': 'orc',
    'health': 120,
    'damage': 80,
    'armor': 1.1
}

print(f'{person_1["name"]} {person_1["health"]},  {person_2["name"]} {person_2["health"]}')


def defence(defence, damage):
    return damage / defence


def attack(defen, agr):
    defen["health"] -= defence(defen["armor"], agr["damage"])
    return defen


person_1 = attack(person_1, person_2)
person_2 = attack(person_2, person_1)
print(f'{person_1["name"]} {person_1["health"]},  {person_2["name"]} {person_2["health"]}')
