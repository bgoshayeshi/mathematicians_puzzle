# We will use a set to store primes for efficiency.
# This allows O(1) lookups, making it faster to check if a number is prime.
prime_set = set()

def find_factors(n):
    """
    Find all factors of a number.
    
    Args:
        n: The number to find factors of.
        
    Returns:
        A list of tuples, each containing a pair of factors.
    """
    factors = []
    
    # The largest factor of n is at most sqrt(n),
    # so we only need to iterate up to that point.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.append((i, n//i))
    return factors
            
def is_prime(n):
    if n < 2:
        return False
    
    # The largest factor of n is at most sqrt(n),
    # so we only need to check up to that point.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
        
def is_not_prime_cube(num):
    # If the number itself is prime, add it to the set and return False.
    if is_prime(num):
        prime_set.add(num)
        return False

    # Check if the number is a square of a prime.
    square = num**0.5
    if square == int(square) and is_prime(int(square)):
        prime_set.add(int(square))
        return False

    # Check if the number is a cube of a prime.
    cube = num**(1./3.)
    if cube == int(cube) and is_prime(int(cube)):
        prime_set.add(int(cube))
        return False

    factors = find_factors(num)

    # Check if each pair of factors are both prime.
    for fact in factors:
        if (fact[0] in prime_set) and (fact[1] in prime_set):
            return False
        if is_prime(fact[0]) and is_prime(fact[1]):
            prime_set.add(fact[0])
            prime_set.add(fact[1])
            return False
    return True


def find_valid_combinations(num, p_list):
   
    valid_pairs = []

    for i in range(2, int(num/2) + 1):
        if i * (num - i) in p_list:
            valid_pairs.append((i, num - i))
        else: 
            return False
    return valid_pairs


def only_one_combination(the_list, key):
    unique_key = {}
    key_iter = set()
    for pair in the_list:
        product = pair[key]
        if product in key_iter:
            continue
        if product in unique_key:
            key_iter.add(product)
            unique_key.pop(product)
            continue
        unique_key[product] = pair

    return [unique_key[key] for key in unique_key]

p_list = []
s_list = []
for i in range(4,2500):
    if is_not_prime_cube(i):
        p_list.append(i)

for i in range(6,100):
    pairs = find_valid_combinations(i, p_list)
    if pairs:
        for pair in pairs: 
            s_list.append({'x': pair[0], 'y': pair[1], 's': pair[0]+pair[1], 'p': pair[0]*pair[1]})

import pandas as pd

p_d = only_one_combination(s_list, 'p')

s_d = only_one_combination(p_d, 's')
print("The answer is: ")
print(s_d)
