from pythonds.basic.stack import Stack

def infix_to_postfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 3
    prec["-"] = 2
    prec["("] = 1
    opstack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)

        elif token == '(':
            opstack.push(token)

        elif token == ')':
            topToken = opstack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opstack.pop()

        else:
            while (not opstack.isEmpty()) and \
               (prec[opstack.peek()] >= prec[token]):
                  postfixList.append(opstack.pop())
            opstack.push(token)

    while not opstack.isEmpty():
        postfixList.append(opstack.pop())
    return " ".join(postfixList)

print(infix_to_postfix("A * B + C * D"))

print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))


