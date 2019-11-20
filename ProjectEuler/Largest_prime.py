
number = 600851475143

max_prime = 1

all_prime_array = [1, 2, 3, 5, 7, 11]

for i in range(2, 10000):
    j = 0
    if (i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0) and (i % 7 != 0) and (i % 11 != 0):
        all_prime_array.append(i)
        print(i)
        j += 1

factors = []
remaining_number = number

for i in range(1, int(len(all_prime_array))):
    if remaining_number % all_prime_array[i] == 0:
        factors.append(all_prime_array[i])
        remaining_number = remaining_number/all_prime_array[i]
        print(remaining_number)

max_prime = (max(factors))
print("Maximimum prime factor should be: ", max_prime)
