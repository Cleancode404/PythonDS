#the book has many typo so make sure you dont just copy the code
#test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,] , "," should not exist after 42 in the list

#this is sequential search expect number in the list are in order. 
#Becase of that, compliexity decreases 

def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42] 
print(ordered_sequential_search(testlist, 3))
