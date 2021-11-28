# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex.
# input: P@ssw0rd+P@ssw0rd
# output: Valid
# Tip: loop through each character of the input then process it letter by letter

#Step1 
Password = input("PLease enter your PASSWORD : ") #Ask for the password

#Step2
num_character = len(Password)
special, lower, upper, digit = 0, 0, 0, 0

if (len(Password) >= 15):
    for me in Password:
        if (me.isdigit()):
            digit += 1
        if (me.islower()):
            lower += 1
        if (me.isupper()):
            upper += 1
        if(me == "#" or me == "!" or me == "$" or me == "&" or me == "%" or me == "'" or me == "*" or me == "()" or me == "+ " or me == "." \
        or me == """|""" or me == """^""" or me == "{" or me == "}" or me == "_" or me == "~" or me == """+""" ):
            special =+ 1
    if (lower >= 1 and upper >= 1 and special >= 1 and digit >= 1):
                print("Your PASSWORD is VALID!")  
    else:
        print("Sorry! The PASSWORD you have entered is INVALID ❌")
