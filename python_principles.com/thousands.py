
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

    # do the string - first 1, 2, 3 digits
    if check_number == True:
        first_comma_position = no_0f_digits % 3

        if no_0f_digits > 3:
            if first_comma_position == 0:
                new_string = new_string + number[0] + number[1] + number[2] + ","
            elif first_comma_position == 1:
                new_string = new_string + number[0] + ","
            else:
                new_string = new_string + number[0] + number[1] + ","

        else:
            new_string = number

        # rest of the number

        end_number_string = ""

        #todo: change first comma position to 3 - will allow to build same loop for all three scenarios

        if first_comma_position == 0:
            no_of_commas = int(no_0f_digits/3)
            # skip first comma
            for i in range(1, no_of_commas):
                end_number_string = end_number_string + number[0+(i*3)] + number[1+(i*3)] + number[2+(i*3)] + ","
        elif first_comma_position == 1:
            no_of_commas = int((no_0f_digits-1)/3)
            for i in range(no_of_commas):
                end_number_string = end_number_string + number[1+(i*3)] + number[2+(i*3)] + number[3+(i*3)] + ","
        # first comma pos 2
        else:
            no_of_commas = int((no_0f_digits - 2) / 3)
            for i in range(no_of_commas):
                end_number_string = end_number_string + number[2 + (i * 3)] + number[3 + (i * 3)] + number[
                    4 + (i * 3)] + ","


    else:
        print("please enter a real number")

    new_string = new_string + end_number_string

    return new_string



print(format_number(input(" Enter a number please")))
