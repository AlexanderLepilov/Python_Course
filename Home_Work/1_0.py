# Найдите сумму цифр трехзначного числа.

num = int(input())
sum = 0

while num:
    sum += num % 10
    num //= 10

print(sum)
