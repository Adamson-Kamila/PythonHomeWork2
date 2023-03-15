import random

a = ['emblem', 'tails']

coins = random.randint(1, 10)
coins_array: list[str] = []

for i in range(coins):
    coins_array.append(a[random.randint(0, 1)])

print(coins_array)

emblem_count = 0
tails_count = 0

for i in coins_array:
    if i == 'emblem':
        emblem_count += 1
    else:
        tails_count += 1

if (emblem_count == 1 and tails_count == 0) or (emblem_count == 0 and tails_count == 1):
    print(0)
elif emblem_count == tails_count:
    print(0)
elif emblem_count < tails_count:
    print(f'Переверните монетки с гербом  {emblem_count}')
else:
    print(f'Переверните монетки с решкой {tails_count}')
