import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

import random

def asch(ref, A, B, C, rep): #verifie si la reponse est bonn
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

# dataset   ref  A  B   C   rep
test_data_true = [10, 5, 10, 20, 2]
must_be_true = asch(*test_data_true) # same as content of []
#print(must_be_true)

# dataset   ref  A  B   C   rep
test_data_false = [10, 5, 10, 20, 2]
must_be_false = asch(*test_data_false)
#print(must_be_false)

#Le modèle du dataset d'entraînement

df1 = pd.read_csv("8_octavia_train_40.csv") #read dataset

import csv 
with open('8_octavia_train_40.csv') as csvfile:
    df1 = list(csv.reader(csvfile))
 
df1 = df1[1:]
#doesnt change original table so need to make a temp table
df1_temp = []

for l in df1:
    l_temp = []
    for case in l:
        if case == "true":
            l_temp.append(1)
        else:
            l_temp.append(int(case))
    df1_temp.append(l_temp)

df1 = df1_temp

# print(df1)

#count = 1
#for l in df:
#    count += 1
#    if asch(*l[:5]):
#        pass
#    else:
#        print("problem!")
#        print("line: ", count)
#        print(l)

### ML if not imported yet import pandas, sklearn tree, sk learn decision tree, matplotlib
df2 = pd.read_csv("8_octavia_train_35.csv")

features = ['ref','A','B','C','rep']

df2["valid"] = df2["valid"].map({True: 1, False: 0})

inputs = df2[features]
outputs = df2['valid']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(inputs, outputs)  #fit means train

tree.plot_tree(dtree, feature_names=features)
#plt.show()

df3 = pd.read_csv("8_octavia_asch_test_dataset_10.csv")

df3["valid"] = df3["valid"].map({True: 1, False: 0})
inputs_test = df3[features]
outputs = df3['valid']

#predit is use
print(dtree.predict(inputs_test))
plt.show()

#fonction qui simule le Asch

