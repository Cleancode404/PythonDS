#classic binary search
#will not work if dataset is not in order

def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last)  // 2
        if alist[midpoint] == item:
            found = True
        else: 
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint  + 1
    return found #this indentation is wrong in the book

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42] 
print(binary_search(testlist, 2))
