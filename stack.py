



class Stack:
    def __init__(self,n):
        self.stack = []
        self.n = n
    
    def push(self,i):
        if len(self.stack) < self.n:
            self.stack.append(i)
        else:
            print("Stack full")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack empty, cant pop")
        else:
            self.stack.pop(-1)
    
    def top(self):
        if len(self.stack) == 0:
            print("stack is empty")
        else:
            print(self.stack[-1])
    
    def display(self):
        print(self.stack)
    


stack1 = Stack(6)

x = input("Enter a word")

for i in x:
    stack1.push(i)

res = str()

for i in range(len(stack1.stack),0,-1):
    res = res + stack1.stack[-1]
    stack1.pop()

print(res)    