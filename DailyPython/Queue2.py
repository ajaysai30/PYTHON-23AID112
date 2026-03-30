from collections import deque

queue = deque()

while True:
    print("\n1. Add Person")
    print("2. Serve Person")
    print("3. Show Queue")
    print("4. Exit")
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        name = input("Enter name: ")
        queue.append(name)
        print(name, "added to queue")
    
    elif choice == 2:
        if queue:
            served = queue.popleft()
            print(served, "is served")
        else:
            print("Queue is empty")
    
    elif choice == 3:
        print("Queue:", list(queue))
    
    elif choice == 4:
        print("Exiting...")
        break
    
    else:
        print("Invalid choice")
