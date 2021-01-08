from pythonds.basic.queue import Queue 

q = Queue()
print((q.enqueue('hello')))

print((q.enqueue('dog')))
print((q.enqueue(3)))

print((q.dequeue()))