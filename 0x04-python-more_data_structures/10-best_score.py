#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    result = list(a_dictionary.keys())[0]
    best_score = list(a_dictionary.values())[0]
    for k, v in a_dictionary.items():
        if v > best_score:
            best_score = v
            result = k
    return (result)
