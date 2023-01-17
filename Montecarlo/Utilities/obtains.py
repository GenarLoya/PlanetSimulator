from pandas import read_csv
import random as rnd

def interval(file:str) -> list:
    csv = read_csv(file)
    probs = csv[['valor','inferior', 'superior']]
    probs_list = probs.values.tolist()
    return probs_list

def list_filter(list_interval: list) -> int:
    rand = rnd.random()
    value = 0

    for i in list_interval:
        if rand >= i[1] and rand < i[2]:
            value = i[0]
    
    return value
