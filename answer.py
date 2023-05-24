prime_list = set()


def FindFact(n):
    factors = []
    for i in range(2, int(n/2)+1):
        if n % i == 0:
           factors.append((i, n/i))
    return factors
            
           
def prime(n):
    """
    Check if a number is prime.

    Args:
        n: The number to check.

    Returns:
        True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True



def s_knew(num,p_cannot_list):
    pairs = []
    for i in range(2,int(num/2)+1):
        if (i*(num-i) in p_cannot_list):
            pairs.append((i, num-i))
            continue
        else: 
            return False
    return pairs
        

def p_cannot(num):
    if prime(num):
        prime_list.add(num)
        return False
    squre = num**(0.5)
    if squre == int(squre) and prime(squre):
        prime_list.add(squre)
        return False

    cube = num**(1./3.)
    if cube == int(cube) and prime(cube):
        prime_list.add(cube)
        return False
   
    factors = FindFact(num)
    
    for fact in factors:
        if (fact[0] in prime_list) and (fact[1] in prime_list):
            return False
        if prime(fact[0]) and prime(fact[1]):
            prime_list.add(fact[0])
            prime_list.add(fact[1])
            return False
    return True

def p_s_determine_list(the_list, key):
    p_unique = {}
    p_iter = set()
    for pair in the_list:
        product = pair[key]
        if product in p_iter:
            continue
        if product in p_unique:
            p_iter.add(product)
            p_unique.pop(product)
            continue
        p_unique[product] = pair

    return [p_unique[key] for key in p_unique]



if __name__ == '__main__': 
    p_list = []
    s_list = []
    for i in range(4,2500):
        if p_cannot(i):
            p_list.append(i)
    
    for i in range(6,100):
        pairs = s_knew(i, p_list)
        if pairs:
            for pair in pairs: 
                s_list.append({'x': pair[0], 'y': pair[1], 's': pair[0]+pair[1], 'p': pair[0]*pair[1]})
     
    # print("------------------------------------")
    p_d = p_s_determine_list(s_list, 'p')
    print(p_d)
    s_d = p_s_determine_list(p_d, 's')

    print("Adn the answer is: ")
    print(s_d)