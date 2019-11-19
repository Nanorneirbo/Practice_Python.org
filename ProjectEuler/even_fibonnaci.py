total = 0
first_digit = 1
second_digit = 2
output = 2

while first_digit < 4000000:
    total = first_digit + second_digit
    first_digit = second_digit
    second_digit = total

    if total % 2 == 0:
        output += total

print(output)
