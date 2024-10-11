import random
from pprint import pprint


all_cards = [0, 1, 2, 3, 4, 1, 2, 3, 4, 5]

def play(strategy_robot, strategy_human):
    random.shuffle(all_cards)   #mix cards

    state = {
        "hand_robot": all_cards[:5], #split in half distribute in 2 variables human and robot
        "hand_human": all_cards[5:],
        "point_robot": 0,
        "point_human": 0,
        "turn": 0,
        "card_robot": None,
        "card_human": None,
        "winner": ""
    }
    
    for i in range(1, 6):       #loop 5 times
        state["turn"] += 1
        state["card_robot"] = None
        state["card_human"] = None
        state["card_robot"] = strategy_robot(state)
        state["card_human"] = strategy_human(state)
        
        if state["card_robot"] >= state["card_human"]:
            state["point_robot"] += 1
        else:
            state["point_human"] += 1
    
    if state["point_robot"] > state["point_human"]:
        state["winner"] = "ROBOT"
    else:
        state["winner"] = "HUMAN"
    return state

##########################################
import strat 

#print(play(strat.coucou, strat.coucou )["winner"])

######################################

def plays(n, strategy_robot, strategy_human):            
    all_games = []
    win_count = {"ROBOT": 0, "HUMAN": 0}

    for j in range(n):
        result = play(strategy_robot, strategy_human)   #storing result from play function
        all_games.append(result)
        win_count[result["winner"]] += 1
    return all_games, win_count
        
n = 1000        
n_games, n_wins = plays(n, strat.random_card, strat.random_card)
# = plays(10000, strat.random_card, strat.random_card)

robot_win = n_wins["ROBOT"]
human_wins = n_wins["HUMAN"]
win_ratio = (robot_win / n) * 100

print(f"Robot win ratio for 1000 games: {win_ratio} %")

n = 10000
n_games, n_wins = plays(n, strat.random_card, strat.random_card)
win_ratio_10000 = ((n_wins["ROBOT"]) / n) * 100

print(f"Robot win ratio for 10,000 games: {win_ratio_10000} %")

results = []
for n in [1000, 10000]:
    strategy_robot = "random_card"
    strategy_human = "random_card"
    n_games, n_wins = plays(n, strat.random_card, strat.random_card)
    win_ratio = ((n_wins["ROBOT"]) / n) * 100
    results.append({
        "no_of_games": n,
        "strategy_robot": strategy_robot,
        "strategy_human": strategy_human,
        "robot_win_ratio": win_ratio
        })

pprint(results)