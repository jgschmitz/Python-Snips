python3
#The following method checks whether the given list has duplicate elements. It uses the property of set() which removes duplicate elements from the list.
#checkes it
def all_unique(lst):
    return len(lst) == len(set(lst))


x = [1,1,2,2,3,2,3,4,5,6]
y = [1,2,3,4,5]
all_unique(x) # So False
all_unique(y) # True
