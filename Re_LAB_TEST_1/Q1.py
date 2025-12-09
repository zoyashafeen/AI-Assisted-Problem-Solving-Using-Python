class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Delete a node by value
    def delete_node(self, key):
        temp = self.head

        # If head node contains the key
        if temp and temp.data == key:
            self.head = temp.next
            return

        # Search for key
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # If node not found
        if temp is None:
            print("Node not found!")
            return

        prev.next = temp.next

    # Display list
    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ---------------------------
# Demonstration / Menu System
# ---------------------------

linked_list = LinkedList()

while True:
    print("\n--- Linked List Operations ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete a Node")
    print("4. Display List")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter value: "))
        linked_list.insert_at_beginning(val)

    elif choice == 2:
        val = int(input("Enter value: "))
        linked_list.insert_at_end(val)

    elif choice == 3:
        val = int(input("Enter value to delete: "))
        linked_list.delete_node(val)

    elif choice == 4:
        linked_list.display()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
