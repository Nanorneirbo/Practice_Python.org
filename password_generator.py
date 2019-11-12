import random

print("This is a password Generator")
generated_password = ""
generated_password2 = ""


def pick_a_digit():
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    special = "!£$%^&*~:#"

    char = [caps, lower, numbers, special]

    type = char[random.randrange(0, 3)]

    if type == 0 or type == 1:
        char_max = 25
    else:
        char_max = 9

    pick = random.randrange(0, char_max)

    return type[pick]

type_of_password = input("Do you want a (S)trong or (W)eak password?")

if type_of_password == "S" or type_of_password == "s":
    no_of_digits = input("How many digits do you need?")

    n = 0
    while n < int(no_of_digits):
        generated_password += pick_a_digit()
        n += 1

    j = 0
    for j in range(int(no_of_digits)):
        generated_password2 += pick_a_digit()
    print("For loop password", generated_password2)


else:
    word_list = ["these", "are", "stupidly", "easy", "passwords"]
    generated_password = word_list[random.randrange(4)]


print("You password is", generated_password)

