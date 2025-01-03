class Node:

    def __init__(self, data):
        self.data= data
        self.next= None

class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, data):
        new_node=Node(data)

        if not self.head:
            self.head = new_node
        else:
            curr=self.head
            while curr.next:
                curr = curr.next
            curr.next= new_node

    def display(self):
        curr=self.head
        while curr:
            print(curr.data, end="->")
            curr=curr.next
        print()

    def delete(self, data):
        if not self.head:
            return "List is empty"

        if self.head.data == data:
            self.head = self.head.next
            return "Deleted"

        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current:
            prev.next = current.next
            return "Deleted"

linkedlist=LinkedList()

while True:
    print("1. Add")
    print("2. Display")
    print("3. Delete")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        item = int(input("Enter the item: "))
        linkedlist.add(item)
    elif choice==2:
        linkedlist.display()
    elif choice==3:
        item = int(input("Enter the item to be deleted: "))
        print(linkedlist.delete(item))
    elif choice==4:
        break
    else:
        print("Invalid choice")