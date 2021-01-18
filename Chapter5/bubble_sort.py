def bubble_sort(alist):
    #loop through the list from left to right 
    for pass_num in range(len(alist)-1 , 0, -1):  
        for i in range(pass_num):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(alist)
print(alist)

