person_1 = {
    'name': 'Elf',
    'health': 100,
    'damage': 50
}
person_2 = {
    'name': 'ork',
    'health': 120,
    'damage': 80
}
print(f'Персонаж 1 {person_1["health"]},  Персонаж 2 {person_2["health"]}')


def attack(defen,agr):
    defen["health"] -= agr["damage"]
    return defen


person_1 = attack(person_1, person_2)
person_2=attack(person_2, person_1)

print(f'Персонаж 1 {person_1["health"]},  Персонаж 2 {person_2["health"]}')
