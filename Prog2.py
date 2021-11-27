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
Password = input("Enter your password : ") #Ask for password

#Step2
num_character = len(Password)
special,lower, upper, digit = 0, 0, 0, 0

if len(Password) >= 15):
    for me in Password:
        if (me.isdidgit()):
            digit += 1
        if (me.islower()):
            lower += 1
        if (me.isupper()):
            upper += 1
                    

