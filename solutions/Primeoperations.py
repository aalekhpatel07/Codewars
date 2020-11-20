from math import sqrt
from collections import Counter
from functools import reduce


def prime_factorization(num):
    '''
    Given a positive int,
    compute its prime factorization
    and return a dictionary
    where keys represent the primes
    and values represent its powers.
    '''
    temp = num
    res = dict()
    p = 2
    
    # Only check for primes that are <= sqrt(num)
    # Since any prime greater than sqrt(num) is complementary to a factor < sqrt(num)
    # we can obtain a complete prime factorization of num using a much faster approach.
    
    while p <= sqrt(temp):
        # Can implement a log-search to find the largest power of p that divides num
        # but that is probably overkill.

        # Use a linear-search instead:
        while temp % p == 0:
            if p in res:
                res[p] += 1
            else:
                res[p] = 1
            temp //= p
        p += 1
    
    check = reduce(lambda acc, x: acc * (x ** res[x]), res, 1)

    # Don't operate on num directly. Use a copy.
    temp = num
    
    # This is the part where we find complementary prime factors that
    # are > sqrt(num).
    
    # If the current factorization is not complete:
    if check != temp:
        candidate = temp // check
        res[candidate] = 1
        temp //= candidate
        while temp % candidate == 0:
            res[candidate] += 1
            temp //= candidate
    
    return res
    

def prime_operations(x, y):
    '''
    Given two positive ints, compute
    the minimum number of operations needed
    to transform x into y where an operation is of the form:
    
    1) Multiply x by any prime p.
    2) Divide x by any prime p.
    '''
    # Compute the prime factorization of x and y.
    a, b = prime_factorization(x), prime_factorization(y)
    
    # Create a Counter for both the dictionaries so that
    # we can compute their symmetric difference quite easily.
    
    ca, cb = Counter(a), Counter(b)
    # The symmetric difference of their prime factors removes all the common
    # primes and their powers that divide them both (because we don't need to include
    # them to get a minimum number of operations).
    
    sym_diff = (ca - cb) + (cb - ca)
    # The sum of the powers of primes in the symmetric difference is the
    # minimum number of primes required to transform x into y.
    return sum(sym_diff.values())


def solve(a, b):
    """
    Solve the problem here.
    :return: The expected output.
    """
    return prime_operations(a, b)


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.
    """
    a, b = list(map(int, input().split(' ')))
    result = solve(a, b)
    print(result)
    return result


def main():
    return driver()


if __name__ == '__main__':
    main()
