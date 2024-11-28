def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        print(f"Pass {i+1}: {arr}")
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [14, 33, 27, 10, 35, 19]
bubble_sort(arr)
print("Sorted array:", arr)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Step {i}: {arr}")

arr = [12, 11, 13, 5, 21, 56]
insertion_sort(arr)
print("Sorted array:", arr)

# Implement a stack using an array with operations to push(), pop(), and display() the
# elements. Modify the stack implementation to check for underflow and overflow
# conditions. Test it with a stack of size 4 and perform 5 push() operations.
class stack:
    def __init__(self,size) -> None:
        self.size =size
        self.array = []
        self.count =0

    def push (self,data):
        if (self.count==self.size):
            print("stack-overflow")
        else:
            self.array.append(data)
            self.count+=1

    def pop(self):
        if(self.count==0):
            print("stack-underflow")
        else:
            self.array.pop()
            self.count-=1

    def display(self):
        for i in self.array:
            print(i,end="-->")
        print()

stk = stack(5)
stk.pop()
stk.push(10)
stk.push(20)
stk.push(30)
stk.display()
stk.pop()
stk.display()
stk.pop()
stk.display()
stk.pop()
stk.display()
stk.pop()
stk.display()

#3) a) Write a program to check if a given integer is a power of 2.
# b) Implement a function to count the number of set bits (1s) in a given integer. Test it
# with the number 29.
# c) Write a program that swaps two numbers using bitwise XOR without using any
# additional variables.
n = int(input())
if ((n&(n-1))!=0):
    print("not power of 2")
else:
    print("power of 2")

# b)
n = int(input())
count=0
while(n):
    n=(n&(n-1))
    count+=1
print(count)

#c)
a = int(input())
b= int(input())
print(f"{a} {b}")
a= a^b
b=a^b
a=a^b
print(f"{a} {b}")

def bfs(graph, start_node):
    visited = set()
    queue = [start_node]
    bfs_order = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            bfs_order.append(node)
            queue.extend(graph[node] - visited)

    return bfs_order

def get_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes in the graph: "))

    for i in range(num_nodes):
        node = input(f"Enter the name of node {i+1}: ")
        neighbors = input(f"Enter the neighbors of {node} separated by space: ").split()
        graph[node] = set(neighbors)

    return graph

graph = get_graph()
start_node = input("Enter the start node for BFS: ")
bfs_result = bfs(graph, start_node)
print("BFS traversal order:", bfs_result)

def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    dfs_order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            dfs_order.append(node)
            stack.extend(graph[node] - visited)

    return dfs_order

def get_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes in the graph: "))

    for i in range(num_nodes):
        node = input(f"Enter the name of node {i+1}: ")
        neighbors = input(f"Enter the neighbors of {node} separated by space: ").split()
        graph[node] = set(neighbors)

    return graph

graph = get_graph()
start_node = input("Enter the start node for DFS: ")
dfs_result = dfs(graph, start_node)
print("DFS traversal order:", dfs_result)

class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data

class LL:
    def __init__(self) -> None:
        self.head = None

    def addAtBeginning(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def addAtEnd(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(data)

    def addBeforeVal(self, before, data):
        if not self.head:
            print("No element found")
            return

        current_node = self.head

        if current_node.data == before:
            self.addAtBeginning(data)
            return

        while current_node.next and current_node.next.data != before:
            current_node = current_node.next

        if current_node.next:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print(f"No node with value {before} found")

    def display(self):
        if not self.head:
            print("Linked list is empty")
        else:
            curr_node = self.head
            while curr_node:
                print(curr_node.data, end=" --> ")
                curr_node = curr_node.next
            print("None")

ll = LL()
ll.addAtBeginning(10)
ll.display()
ll.addAtBeginning(20)
ll.display()
ll.addAtEnd(20)
ll.display()
ll.addAtEnd(30)
ll.display()
ll.addBeforeVal(30, 40)
ll.display()

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            removed_data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return removed_data

    def printqueue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            current = self.front
            while current is not None:
                print(current.data, end=" --> ")
                current = current.next
            print("None")

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.printqueue()

q.dequeue()
q.dequeue()
q.printqueue()

q.enqueue(5)
q.printqueue()
