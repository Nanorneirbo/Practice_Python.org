i = 0
j = 0
largest_palindrome = 0

for i in range(99, 999):
    for j in range(99, 999):
        num = i * j
        number = str(num)
        reverse = ""
        for k in range(len(number)):
            reverse += number[len(number)-k-1]
        if reverse == number and num > largest_palindrome:
            largest_palindrome = num


print(largest_palindrome)