def perc_down(self, i ):
    while (i * 2) <= self.current_size:
        mc = self.min_child(i)
        if self.heap_list[i] > self.heap_list[mc]:
            tmp = self.heal_list[i]
            self.heap_list[i] = self.heap_list[mc]
            self.heap_list[mc] = tmp
        i = mc

def min_child(self, i):
    if i*2 + 1 > self.current_size:
        return i*2
    else:
        if self.heap_list[i*2] < self.heap_list[i*2 + 1]:
            return i*2
        else:
            return i*2 + 1