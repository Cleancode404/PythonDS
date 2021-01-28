def build_heap(self, alist):
    i = len(alist)//2
    self.current_size = len(alist)
    self.heap_list = [0] + alist[:]
    while (i>0):
        self.perc_down(i)
        i = i - 1