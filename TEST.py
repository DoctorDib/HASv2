from math import sqrt

# DICTIONARY

numbers = {'1': {0.1}, '2': {2}, '3': {3}, "4": {4}, "5": {5}, "6": {6}, "7": {7}, "8": {8}, "9": {9}}




#PEARSONS

def sim_pearson(prefs, p1, p2):
    # Get the list of mutually rated items
    si ={}

    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item]=1

    # Find the number of elements
    n = len(si)

    # If they are no ratings in common, return 0
    if n == 0:
        return 0

    # Add up all of the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p1][it] for it in si])

    # Sum up the squares
    sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

    # Sum up the products
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

    # Calculate Pearson score
    num=pSum-(sum1*sum2)
    den=sqrt((sum1Sq-pow(sum1,2))*(sum2Sq-pow(sum2,2)))
    if den == 0:
        return 0

    r = num/den

    return r
