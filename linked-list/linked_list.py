from node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def insertNode(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head=new_node
        elif value <= self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            previous = self.head
            runner = self.head.next

            while (runner is not None ) and value > runner.value:
                previous = runner
                runner = runner.next

            new_node.next= runner
            previous.next =new_node

    def display_list(self):
        runner= self.head

        while runner is not None:
            if runner.next is not None:
                print(runner.value, end=" -> ")
            else:
                print(runner.value)
            runner= runner.next

    def count_nodes(self):
        counter = 0
        curr_node = self.head
        while curr_node is not None:
            counter+= 1
            curr_node=curr_node.next
        return counter
    

    def find_node(self, target_node):
        curr_node = self.head

        while curr_node is not None:
            if curr_node.value ==  target_node:
                print("Node found")
                break
            curr_node=curr_node.next

        else:
            print("Node not found")

    def delete_head_node(self, target_value):
        if self.head is None:
            return False
        elif self.head.value == target_value:
            self.head = self.head.next
            return True
        
    def delete_middle_node(self, target_value):
        previous=self.head
        runner = self.head.next

        while runner.value is not None:
            if runner.value == target_value:
                previous.next = runner.next
                return True
            else:
                previous= runner
                runner= runner.next
        return False

    def reverse_list(self):
        
        prev= None
        curr=self.head
        
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

        self.display_list()
