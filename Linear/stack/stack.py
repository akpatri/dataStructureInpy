stack=[]
def push(data):
    stack.append(data)
def pop():
    if(len(stack)!=0):
        return stack.pop()
def peek():
    if(len(stack)!=0):
        return stack[-1]
    
def matchParanthesis(string):
    stack.clear()
    matchPair={'[':']','{':'}','(':')'}
    for s in string:
        if(s in matchPair.keys()):
            push(s)
        elif(s in matchPair.values()):
            if(s!=matchPair[pop()]):
                return 0
    if(len(stack)!=0):
        return 0
    else:
        return 1
    
def reverseString(string):
    stack.clear()
    rev=''
    for s in string:
        push(s)
    for s in string:
        rev+=pop()
    print(rev)

def infixToPostfix(string):
    postfix=''
    stack.clear()
    def priority(char):
        if(char=='+' or char=='-'):
            return 1
        elif(char=='/' or char=='*'):
            return 2
        elif(char=='('):
            return 0
    for s in string:
        if(str(s).isdigit()):
            postfix+=s
        else:
            while(len(stack)!=0 and priority(peek())>priority(s)):
                postfix+=pop()
            push(s)
    while(len(stack)!=0):
        postfix+=pop()
    return postfix


def postfixEvulate(string):
    stack.clear()
    for s in string:
        if(str(s).isdigit()):
            push(s)
        else:
            n2=int(pop())
            n1=int(pop())
            match(s):
                case '+':
                    push(str(n2+n1))
                case '-':
                    push(str(n2-n1))
                case '*':
                    push(str(n2*n1))
                case '/':
                    push(str(n2/n1))
    return pop()
