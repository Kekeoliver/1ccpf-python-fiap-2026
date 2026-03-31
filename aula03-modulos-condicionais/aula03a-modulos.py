import math
#from math import sqrt

num = 4
raiz = math.sqrt(num)
print(f'A raiz de {num} é {raiz:.2f}')

graus = 90
radiano = graus / 180 * math.pi
seno = math.sin(radiano)

print(f'{seno:.2f}')

import random

num_rand = random.random()
print(num_rand*10)

num_rand_int = random.randint( 1, 10 )
print(num_rand_int)

