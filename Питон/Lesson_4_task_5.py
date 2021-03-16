from functools import reduce
list_generated = [i for i in range(100,1000) if i%2 == 0]
print(reduce(lambda x,y:x+y,list_generated))

