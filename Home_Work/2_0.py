# 1. На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

nCoin = int(input("Enter the number of coins\n "))
i = attempt = eagle = tails = 0
while i < nCoin:
    attempt = int(input("Eagle  or tails? (0 или 1)\n "))
    i += 1
    if attempt == 0:
        eagle += 1
    else:
        tails += 1
if eagle > tails:
    print("minimum number of coins to flip = ", nCoin - eagle)
else:
    print("minimum number of coins to flip = ", nCoin - tails)