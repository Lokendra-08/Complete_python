class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return "Queue is empty"
        
    def size(self):
        return len(self.items)
    
    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            return "Queue is empty"
        
queue=Queue()

while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Size")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        item = int(input("Enter the item: "))
        queue.enqueue(item)
    elif choice==2:
        print(queue.dequeue())
    elif choice==3:
        print(queue.peek())
    elif choice==4:
        print(queue.size())
    elif choice==5:
        break
    else:
        print("Invalid choice")