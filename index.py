import random
import time

print('Quem vai vencer as eleições de 2022?')
x = random.randint(1,2)
s = time.sleep(3)

if x == 1:
    print('Bolsonaro!')
elif x == 2:
    print('Lula!')