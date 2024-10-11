import json
import random

with open('4_Exo_Quarta.json') as j:
        l = json.load(j)

def groupe(k):
    if k < 1: raise ValueError("Nope")
    data = l.copy()
    random.shuffle(data)
    result = []
    while len(data) > 0:
        g = []
        for i in range(k):
            g.append(data.pop())
            if len(data) == 0: break
        result.append(g)
    return result

k = int(input("define value of k: "))
print(groupe(k))