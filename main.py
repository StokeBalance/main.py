# Check if two words are anagrams 

# Example:

# find_anagrams("hello", "check") --> False

# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    word = input("Enter first word")
    anagram = input("Enter second word")
    D_word = word.lower()
    D_anagram = anagram.lower()
    if len(word) == len(anagram):

        if  sorted(D_word) == sorted(D_anagram): 

           print('True')

        else:

            print('False')   

    else:

           print('The words are not of the same lenght!')   

           return True
find_anagram(percussion, supersonic)
