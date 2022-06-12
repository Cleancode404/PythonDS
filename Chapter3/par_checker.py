#use data structure stack to check if parentheses are right

from pythonds.basic.stack import Stack #import the Stack class as previously defined

def par_checker(symbolstring):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolstring) and balanced:
        symbol = symbolstring[index]
        if symbol == "(":
            s.push(symbol)

        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    
    else:
        return False

print(par_checker('((()))'))
print(par_checker('())'))
