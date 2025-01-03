class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return "Stack is empty"
        
    def size(self):
        return len(self.items)
    
stack=Stack()

while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Size")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        item = int(input("Enter the item: "))
        stack.push(item)
    elif choice==2:
        print(stack.pop())
    elif choice==3:
        print(stack.peek())
    elif choice==4:
        print(stack.size())
    elif choice==5:
        break
    else:
        print("Invalid choice")