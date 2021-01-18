#recursive binary search
#will not work if dataset is not in order
def recursive_binary_search(alist, item):
    if len(alist) == 0:
        return False #again indentation in the book is wrong from this line below
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return recursive_binary_search(alist[: midpoint], item)
            else:
                return recursive_binary_search(alist[midpoint + 1: 1], item )
    

testlist = [0, 2, 32, 8, 13, 17, 19, 32, 42] 
print(recursive_binary_search(testlist, 2))
