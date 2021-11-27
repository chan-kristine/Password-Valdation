# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
#ex.
#input: Bahala kayo dyan
#output:
#words: 3
#vowels: 6
#consonants: 8


#Step 1 - Ask for a sentence
Sentence = input("Enter you sentence here: ")

#Step 2 - display the number of words, vowels and consonants
n_words = len(Sentence.split())
n_vowels = 0
n_consonants = 0
n_space = 0

for counting in Sentence:
    if counting == "a" or counting == "e" or counting == "i" or counting == "o" or counting == "u" or \
        counting == "A" or counting == "E" or counting == "I" or counting == "O" or counting == "U":
        n_vowels = n_vowels + 1 #Added vowels to be counted
    elif counting == "":
        n_space = n_space + 1    #Added space num
    else:
        n_consonants = n_consonants + 1   #Added Consonants to be counted

#Step3- Display everything
print (f"The result says that the number of words in the sentence is :{n_words}")
print (f"The result says that the number of vowels in the sentence is :{n_vowels}")
print (f"The result says that the number of consonants in the sentence is :{n_consonants}")





