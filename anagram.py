python3

#This method can be used to check if two strings are anagrams. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
from collections import Counter
print 1,2,3,4,5,6,7,8,
def anagram(first, second):
    return Counter(first) == Counter(second)


anagram("abcd3", "3acdb") # True
