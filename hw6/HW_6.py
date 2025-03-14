#1
import numpy as np

arr = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])

def is_prime(n):
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def row_contains_prime(row):
    return any(is_prime(n) for n in row)

def containsPrimes(arr):
    primes = np.apply_along_axis(row_contains_prime, axis=1, arr=arr)
    return arr[primes]
    
print(containsPrimes(arr))

#
print("-------------------------------------------------")

#2
import numpy as np

def board():
    return np.zeros((8, 8), dtype = int)
    
print(board())

#
print("-------------------------------------------------")
#2.2
import numpy as np

def board2():
    board2 = np.zeros((8, 8), dtype=int)
    board2 [::2, ::2] = 1  
    return board2
print(board2())

#
print("-------------------------------------------------")

#2.3
def board3():
    board3 = np.zeros((8, 8), dtype=int)
    board3 [::2, ::2] = 1 
    board3 [1::2, 1::2] = 1 
    return board3
print(board3())

#
print("-------------------------------------------------")

#2.4
def board4():
    board4 = np.zeros((8, 8), dtype=int)
    board4 [::1, ::2] = 1 
    board4 [::2, ::1] = 1 
    board4 [::2, ::2] = 0 
    return board4
print(board4())

#
print("-------------------------------------------------")

#3
import numpy as np

def expansion(strings,space):
    def expand_word(i):
        return(' '* space).join(i)
    
    expanded_words = np.array([expand_word(i) for i in strings])
    return expanded_words
    
universe = np.array(['galaxy', 'clusters'])
print(expansion(universe, 3))

print("-------------------------------------------------")

#4
import numpy as np

def secondDimmest(stars):
     sorted = np.sort(stars, axis=0)
     return sorted[1]
    
np.random.seed(123)
stars = np.random.randint(500, 2000, (5, 5))
print(stars)
print(secondDimmest(stars))



