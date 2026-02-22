



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

    def type(self,word):
        global text
        self.word = word
        text = text + word
        self.stack.append(word)

    def undo(self):
        self.stack.pop(-1)
        global text
        text = ""
        for i in self.stack:
            text = text+i



    


stack1 = Stack(10000)

'''x = input("Enter a word")

for i in x:
    stack1.push(i)

res = str()

for i in range(len(stack1.stack),0,-1):
    res = res + stack1.stack[-1]
    stack1.pop()

print(res)'''


'''x = input("Enter a word")

for i in x:
    stack1.push(i)

res = str()

for i in range(len(stack1.stack),0,-1):
    res = res + stack1.stack[-1]
    stack1.pop()



if res == x:
    print("Word is a palindrome")
else: 
    print("word is not palindrome")'''

stackhistory = Stack(100)
text = ""
x = input("ENter a word")
stackhistory.type(x)

y = input("enter a word")

stackhistory.type(y)
print(stackhistory.stack)

stackhistory.undo()

print(stackhistory.stack)
print(text)

