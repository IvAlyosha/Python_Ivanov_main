import random
fruits_all=['apple','panaple','banan','cocnut','waterlemon','peach','kiwi','grapefruit','banan','peach','dragon fruit', 'orange', 'apricot']
fruits_1=[random.choice(fruits_all) for number in range(0,6)]
print(fruits_1)
fruits_2=[random.choice(fruits_all) for number in range(0,6)]
print(fruits_2)
fruits_union=set([i for i in fruits_1 if i in fruits_2])
print(fruits_union)