
number = 13195
max_prime = 1

for i in range(1, int(number/2)):
    if number % i == 0:
        max_prime = i

print(max_prime)
