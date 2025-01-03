class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return self.data

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root= Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self,node, data):

        if data<node.data:
            if node.left is None:
                node.left=Node(data)
            else:
                self._insert_recursive(node.left, data)

        elif data>node.data:
            if node.right is None:
                node.right= Node(data)
            else:
                self._insert_recursive(node.right, data)

    def search(self, data):
        self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if node is None or node.data == data:
            return node
        elif data<node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
        
bst=BinarySearchTree()

while True:
    print("1. Insert")
    print("2. Search")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter data to insert: "))
        bst.insert(data)
    elif choice == 2:
        data = int(input("Enter data to search: "))
        if bst.search(data):
            print("Data found")
        else:
            print("Data not found")
    elif choice == 3:
        break
    else:
        print("Invalid choice")