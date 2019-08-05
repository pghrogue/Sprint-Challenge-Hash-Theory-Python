#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    index = 0

    # Fill in the hash table
    for weight in weights:    
        hash_table_insert(ht, weight, index)
        index += 1

    for x in range(length - 1, 0, -1):
        print(f"x: {x} limit {limit} - weight {weights[x]}")
        diff = limit - weights[x]
        print(f"Diff {diff}")
        if diff > 0:
            weightKey = hash_table_retrieve(ht, weights[x])
            hayKey = hash_table_retrieve(ht, diff)
            print(f"w: {weightKey} h: {hayKey}")
            if weightKey is not None and hayKey is not None:
                return(weightKey, hayKey)
        
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
