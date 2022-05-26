# Check if two words are anagrams 

# Example:

# find_anagrams("hello", "check") --> False

# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):

    if len(word) == len(anagram):

        if  sorted(word) == sorted(anagram): 

           print('True')

        else:

            print('False')   

    else:

           print('The words are not of the same lenght!')   

           return True
