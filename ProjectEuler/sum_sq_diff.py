sum_squares = 0
sum = 0

for i in range(101):
    print("Sum of Squares " + str(sum_squares) + "Sum " + str(sum))
    sum_squares += i**2
    sum += i

print(str(abs(sum_squares-(sum**2))))

