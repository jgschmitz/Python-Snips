#This method gets vowels (‘a’, ‘e’, ‘i’, ‘o’, ‘u’) found in a string.
def get_vowels(string):
    return [each for each in string if each in 'aeiou'] 

print 1,2,3,4,5
get_vowels('foobar') # ['o', 'o', 'a']
get_vowels('gym') # []
