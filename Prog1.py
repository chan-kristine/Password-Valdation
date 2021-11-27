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




