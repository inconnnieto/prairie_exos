import random

#creation des cartes
tt_les_cartes = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5]

#debut de la partie (ca devra devenir une fonction)
def partie (strat_human, strat_robot):
    #melange des cartes
    random.shuffle(tt_les_cartes)
    #distribution
    state = {
        "robot hand": tt_les_cartes[:5],
        "human hand": tt_les_cartes[5:],
        "point robot": 0,
        "point human": 0,
        "tour": 0,
        "CR": None, #Carte Robot
        "CH": None, #Carte Human
        "winner": ""
    }

    for i in range(1, 6):
        state["tour"] += 1
        state["CR"] = None
        state["CH"] = None
        state["CR"] = strat_robot(state)
        state["CH"] = strat_human(state)
        if state ["CR"] >= state ["CH"]:
            state["point robot"] += 1
        else:
            state["point human"] += 1

    #determiner le gagnant (il faudra ici retourner le resultat de la partie)
    if state["point robot"] > state["point human"]:
        state["winner"] = "robot"
    else:
        state["winner"] = "human"

    return state

def plays(n, strat_human, strat_robot):
    tt_parties = []
    for j in range (n):
        tt_parties.append(partie(strat_human, strat_robot))
        return tt_parties
    
import strat_eg
print(
    plays(n = 1000,
          strat_human = strat_eg.coucou,
          strat_robot = strat_eg.coucou
          )
)