
'''Thousands separator
Write a function named format_number that takes a non-negative number as its only parameter.
Your function should convert the number to a string and add commas as a thousands separator.
For example, calling format_number(1000000) should return "1,000,000".'''




def format_number(number):
    number = str(number)
    no_0f_digits = len(number)

    # set up a string to check that all of the numbers are actually numbers
    actual_numbers = "0123456789"

    check_number = False

    new_string = ""

    for i in range(no_0f_digits):
        if number[i] in actual_numbers:
            check_number = True
        else:
            check_number = False

    # do the string - modding off the back 3
    if check_number == True:
        first_comma_position = no_0f_digits % 3

        if no_0f_digits > 3:
            if first_comma_position == 0:
                new_string = new_string + number[0] + number[1] + number[2] + ","
            elif first_comma_position == 1:
                new_string = new_string + number[0] + ","
            else:
                new_string = new_string + number[0] + number[1] + ","



        print(new_string)


    else:
        print("please enter a real number")

    return new_string



format_number(input(" Enter a number please"))
