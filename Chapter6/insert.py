def insert(self, k):
    self.heap_list.append(k)
    self.current_size = self.current_size  + 1
    self.perc_up(self.current_size)