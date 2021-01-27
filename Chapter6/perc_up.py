def perc_up(self, i):
    while i // 2 >0:
        if self.heap_list[i] < self.heap_list[i //2]:
            tmp = self.heap_list[i //2]
            self.heap_list[i //2 ]  = self.heap_list[i]
            self.heap_list[i]  = tmp

        i = //2