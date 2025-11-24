class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            raise IndexError("Cannot dequeue: Queue is empty.")
        return self.items.pop(0)

    def peek(self):
        if len(self.items) == 0:
            raise IndexError("Cannot peek: Queue is empty.")
        return self.items[0]


# ---------------------------------
# User Input Program
# ---------------------------------

queue = Queue()

print("Queue Operations:")
print("Commands:")
print("  enqueue <value>")
print("  dequeue")
print("  peek")
print("  exit")

while True:
    command = input("\nEnter command: ").strip()

    if command.startswith("enqueue"):
        # Extract value after 'enqueue '
        parts = command.split(" ", 1)
        if len(parts) == 2:
            value = parts[1]
            queue.enqueue(value)
            print(f"Enqueued: {value}")
        else:
            print("Error: Please specify a value. Example: enqueue 10")

    elif command == "dequeue":
        try:
            item = queue.dequeue()
            print("Dequeued:", item)
        except IndexError as e:
            print(e)

    elif command == "peek":
        try:
            item = queue.peek()
            print("Front item:", item)
        except IndexError as e:
            print(e)

    elif command == "exit":
        print("Exiting program.")
        break

    else:
        print("Invalid command. Try: enqueue <value>, dequeue, peek, exit")
