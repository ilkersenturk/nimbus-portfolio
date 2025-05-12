data_structures = [
    {
        "title": "1️⃣ Strings",
        "short_title": "Strings",
        "why": "Used for storing and processing text. Immutable, fast, and powerful for slicing and searching.",
        "when": "Text parsing, logs, filenames, URLs, NLP, etc.",
        "algorithms": ["Reversal", "Concatenation", "KMP", "Regex matching"],
        "mistakes": ["Modifying strings in-place", "Using '+' repeatedly"],
        "considerations": "Use `.join()` for performance; remember immutability.",
        "example": '''# String Operations
s = "hello world"
print("Original:", s)
print("Reversed:", s[::-1])
print("Uppercase:", s.upper())
print("Find 'world':", s.find("world"))
print("Replace 'world' with 'Python':", s.replace("world", "Python"))''',
        "real_life": "Example: Editing a sentence in a document. You could use a list of characters, but strings are optimized for performance and built-in operations like search and slice."
    },
    {
        "title": "2️⃣ Lists",
        "short_title": "Lists",
        "why": "A flexible, mutable collection. Random access, append/pop, sorting.",
        "when": "General-purpose containers, iteration, stack/queue base.",
        "algorithms": ["Sorting", "Slicing", "Searching"],
        "mistakes": ["Appending inside loop inefficiently", "Modifying while iterating"],
        "considerations": "Use comprehensions and avoid unnecessary copies.",
        "example": '''# List Operations
lst = [1, 2, 3]
lst.append(4)
lst.insert(0, 0)
lst.remove(2)
print("List:", lst)
print("Sorted:", sorted(lst))''',
        "real_life": "Example: Grocery list. You could use a dictionary with indexes as keys, but a list is easier and faster for ordered collections that grow dynamically."
    },
    {
        "title": "3️⃣ Linked Lists",
        "short_title": "Linked Lists",
        "why": "Efficient at inserting and removing elements, especially at the beginning.",
        "when": "Used in streaming data, memory-efficient operations, undo features.",
        "algorithms": ["Traversal", "Reversal", "Cycle Detection", "Merge Sorted Lists"],
        "mistakes": ["Losing track of next node", "Null pointer errors"],
        "considerations": "Singly vs doubly linked, manual memory in lower-level languages.",
        "example": '''class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete_value(self, value):
        curr = self.head
        if curr and curr.value == value:
            self.head = curr.next
            return
        prev = None
        while curr and curr.value != value:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next

    def display(self):
        curr = self.head
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")

# Example Usage
ll = LinkedList()
ll.insert_at_head(3)
ll.insert_at_end(5)
ll.insert_at_head(1)
ll.display()        # 1 -> 3 -> 5 -> None
ll.delete_value(3)
ll.display()        # 1 -> 5 -> None''',
        "real_life": "Example: Music playlist with skip and previous. A list works too, but a linked list handles frequent insertions and deletions better without shifting elements."
    },
    {
        "title": "4️⃣ Stacks",
        "short_title": "Stacks",
        "why": "LIFO data structure great for reversing, undo operations, DFS.",
        "when": "Used in parsing, recursion emulation, balancing symbols.",
        "algorithms": ["Push/Pop", "Reverse Polish Notation", "Backtracking"],
        "mistakes": ["Popping from empty stack", "Not using built-in types"],
        "considerations": "Use list or collections.deque for performance.",
        "example": '''# Stack Implementation
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if not self.is_empty() else None

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example
s = Stack()
s.push(1)
s.push(2)
print("Top:", s.peek())
print("Popped:", s.pop())''',
        "real_life": "Example: Undo button in Word. You could use a list and track indexes, but a stack naturally supports LIFO behavior where the last action is reversed first."
    },
    {
        "title": "5️⃣ Queues",
        "short_title": "Queues",
        "why": "FIFO structure ideal for scheduling, buffering, and task processing.",
        "when": "Used in printer queues, CPU scheduling, BFS.",
        "algorithms": ["Enqueue", "Dequeue", "Circular Queue", "Priority Queue"],
        "mistakes": ["Inefficient list operations", "Queue overflow in fixed-size"],
        "considerations": "Use `collections.deque` or `queue.Queue`.",
        "example": '''# Queue Implementation
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.popleft() if not self.is_empty() else None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example
q = Queue()
q.enqueue(10)
q.enqueue(20)
print("Dequeued:", q.dequeue())''',
        "real_life": "Example: Customers lining up at a counter. You could pop from a list's start, but that’s slow — a queue ensures fast and fair processing in FIFO order."
    },
    {
        "title": "6️⃣ Trees",
        "short_title": "Trees",
        "why": "Hierarchical data model. Efficient searching, sorting, and classification.",
        "when": "Used in file systems, databases, decision trees, parsers.",
        "algorithms": ["DFS", "BFS", "Traversal (Inorder/Pre/Post)", "BST operations"],
        "mistakes": ["Null reference errors", "Incorrect child assignments"],
        "considerations": "Binary trees vs N-ary, balance, recursion stack depth.",
        "example": '''# Binary Tree with Inorder Traversal
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Example
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
inorder(root)  # Output: 5 10 20''',
        "real_life": "Example: Folder structure in your computer. You could use nested dictionaries, but trees naturally represent parent-child relationships with efficient traversal."
    },
    {
        "title": "7️⃣ Heaps",
        "short_title": "Heaps",
        "why": "Priority queues. Fastest way to get min/max element in O(1).",
        "when": "Used in task schedulers, Dijkstra’s algorithm, load balancing.",
        "algorithms": ["Heapify", "Insert", "Extract Min/Max"],
        "mistakes": ["Confusing max/min heaps", "Indexing errors"],
        "considerations": "Use `heapq` for min-heap, simulate max-heap with negative values.",
        "example": '''# Min Heap using heapq
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

print("Min element:", heapq.heappop(heap))''',
        "real_life": "Example: Job queue where high-priority tasks are processed first. A sorted list is slower to update — heaps give fast priority access."
    },
    {
        "title": "8️⃣ Graphs",
        "short_title": "Graphs",
        "why": "Represent relationships, networks, and connections.",
        "when": "Used in maps, social networks, dependency resolution.",
        "algorithms": ["DFS", "BFS", "Dijkstra", "Topological Sort"],
        "mistakes": ["Infinite loops in cyclic graphs", "Unvisited nodes"],
        "considerations": "Directed vs undirected, adjacency list vs matrix.",
        "example": '''# Graph DFS Traversal
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)

# Example
dfs('A', set())''',
        "real_life": "Example: Finding a route on Google Maps. You could use a grid, but graphs model connections and weights more effectively for navigation and optimization."
    }
]
