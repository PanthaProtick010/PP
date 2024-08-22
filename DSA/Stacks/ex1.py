from collections import deque
class Stack:
    def __init__(self):
        self.container=deque()
    def push(self,value):
        self.container.append(value)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def isEmpty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)

def paraBalance(open,close):
    if((open=='('and close==')') or (open=='{'and close=='}') or (open=='['and close==']')):
        return True
    else:
        return False

def isBalanced(string):
    st=Stack()
    for char in string:
        if char=='(' or char=='{' or char=='[':
            st.push(char)
        elif char==')' or char=='}' or char==']':
            if st.isEmpty() or (not paraBalance(st.peek(),char)):
                return False
            else:
                st.pop()
    return st.isEmpty()
if __name__=="__main__":
    string="[a+b]*(x+2y)*{gg+kk}"
    print(isBalanced(string))