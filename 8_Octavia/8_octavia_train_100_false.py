import random
import pandas as pd

def asch(ref, A, B, C, rep):
    if ref == A:
        if rep == 1:
            return True
        else:
            return False
    elif ref == B:
        if rep == 2:
            return True
        else:
            return False
    elif ref == C:
        if rep == 3:
            return True
        else:
            return False
    return False

octavia_train_100 = []

for i in range(100): 
    values = [random.choice(range(1, 10)) for j in range(3)]
    A, B, C = values
    ref = random.choice(values)
    rep = values.index(ref) + 1 

    valid = asch(ref, A, B, C, rep) 
    octavia_train_100.append([ref, A, B, C, rep, valid])

columns = ['ref', 'A', 'B', 'C', 'rep', 'valid']
train100_df = pd.DataFrame(octavia_train_100, columns=columns)
train100_df.to_csv('8_octavia_asch_train_dataset_199.csv', index=False) 
