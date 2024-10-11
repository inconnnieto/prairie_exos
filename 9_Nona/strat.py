import random

def coucou(state):
    # if i'm the human
    if state["card_robot"] != None: #robot has played 

        #i play winning card
        for card in state["hand_human"]:
            if card > state["card_robot"]:
                state["hand_human"].remove(card)
                return card
        
        #else play my weakest card
        card = min(state["hand_human"])
        state["hand_human"].remove(card)
        return card
    else:
        #if i'm the Robot
        #I play my highest card
        carte = max(state["hand_robot"])
        state["hand_robot"].remove(carte)
        return carte

def random_card(state):
    #human
    if state["card_robot"] != None: 
        #i play a random card
        for card in state["hand_human"]:
            card = random.choice(state["hand_human"])
            state["hand_human"].remove(card)
            return card
    else: 
        #robot
        carte = random.choice(state["hand_robot"])
        state["hand_robot"].remove(carte)
        return carte
        
def pop(state):
    #human
    if state["card_robot"] != None:
        #i play the last card in my hand .pop() default last
        for card in state["hand_human"]:
            card = (state["hand_human"]).pop() #last item by default
            return card
    else:
        #robot
        carte = (state["hand_robot"]).pop()
        return carte
   
def max_card(state):
    #human
    if state["card_robot"] != None:
        #i play max card
        for card in state["hand_human"]:
            card = max(state["hand_human"])
            state["hand_human"].remove(card)
            return card
    else:
        #robot
        carte = max(state["hand_robot"])
        state["hand_robot"].remove(carte)
        return carte

def min_card(state):
    #human
    if state["card_robot"] != None:
        #i play max card
        for card in state["hand_human"]:
            card = min(state["hand_human"])
            state["hand_human"].remove(card)
            return card
    else:
        #robot
        carte = min(state["hand_robot"])
        state["hand_robot"].remove(carte)
        return carte

