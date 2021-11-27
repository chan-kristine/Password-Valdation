# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
#ex.
#input: Bahala kayo dyan
#output:
#words: 3
#vowels: 6
#consonants: 8


#Step 1 - Ask for a sentence
Sentence = input(" \33[32m\33[1mEnter you sentence here:\33[0m ")

#Step 2 - display the number of words, vowels and consonants
n_words = len(Sentence.split())
n_vowels = 0
n_consonants = 0
n_space = 0

for counting in Sentence:
    if counting == "a" or counting == "e" or counting == "i" or counting == "o" or counting == "u" or \
        counting == "A" or counting == "E" or counting == "I" or counting == "O" or counting == "U":
        n_vowels = n_vowels + 1 #Added vowels to be counted
    elif counting == " ":
        n_space = n_space + 1    #Added space num
    else:
        n_consonants = n_consonants + 1   #Added Consonants to be counted

#Step3- Display everything
print (f"Number of \33[32m\33[1mwords\33[0m in the sentence :\33[1m\33[95m {n_words}\33[0m" )
print (f"Number of \33[32m\33[1mvowels\33[0m in the sentence :\33[1m\33[95m {n_vowels}\33[0m")
print (f"Number of \33[32m\33[1mconsonants\33[0m in the sentence :\33[1m\33[95m {n_consonants}\33[0m")
