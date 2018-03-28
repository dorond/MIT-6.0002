###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================
import random

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    #Iterative solution
    # egg_weights = sorted(egg_weights, reverse=True)
    # result = 0
    # total_eggs = 0
    # available_weight = target_weight

    # for weight in egg_weights:
    #     num_eggs = available_weight // weight
    #     total_eggs = total_eggs + num_eggs
    #     remaining_weight = available_weight % weight
    #     available_weight = remaining_weight

    # return total_eggs

    #Recursive solution   
    
    egg_weights = tuple(sorted(egg_weights, reverse=True))    
    
    total_eggs = 0
    available_weight = target_weight
    
    if egg_weights in memo:
        return memo[egg_weights]

    elif len(egg_weights) == 1:
        return egg_weights[0] * target_weight

    else:
        num_eggs = available_weight // egg_weights[0]
        remaining_weight = available_weight % egg_weights[0]
        available_weight = remaining_weight
        memo[egg_weights[0]] = num_eggs
        total_eggs = total_eggs + memo[egg_weights[0]] + dp_make_weight(egg_weights[1:], remaining_weight, memo)
    
    return total_eggs  

def buildRandomEggTuple(numItems, maxWeight):
    egg_weights = []
    for i in range(numItems):
        egg_weights.append(random.randint(1, maxWeight))
    return tuple(sorted(egg_weights))

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
    egg_weights = (1, 5, 10, 20)
    n = 99
    print("Egg weights = (1, 5, 10, 20)")
    print("n = 99")
    print("Expected ouput: 10 (4 * 20 + 1 * 10 + 1 * 5 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
    egg_weights = buildRandomEggTuple(50, 90)
    n = 99
    print("Egg weights =", egg_weights)
    print("n = 99")
    #print("Expected ouput: 10 (4 * 20 + 1 * 10 + 1 * 5 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()

