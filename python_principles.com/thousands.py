
'''Thousands separator
Write a function named format_number that takes a non-negative number as its only parameter.
Your function should convert the number to a string and add commas as a thousands separator.
For example, calling format_number(1000000) should return "1,000,000".'''


number_input = int(input("enter a number"))



string_input = str(number_input)

no_0f_digits = len(string_input)

# set up a string to check that all of the numbers are actually numbers
actual_numbers = "0123456789"

check_number = False

for i in range(no_0f_digits):
    if string_input[i] in actual_numbers:
        check_number = True
    else:
        check_number = False

# do the sring
if check_number == True:

else:
    print("please enter a real number")

print(no_0f_digits)

