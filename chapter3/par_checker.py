#use data structure stack to check if parentheses are right

from pythonds.basic.stack import Stack #import the Stack class as previously defined

def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)

        else:
            s.pop()

    index = index + 1

    if balanced and s.is_empty():
        return True
    
    else:
        return False

print(par_checker('((()))'))
print(par_checker('())'))
