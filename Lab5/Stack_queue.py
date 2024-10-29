class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

# Test the Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Should print 3
print(stack.peek())  # Should print 2
print(stack.size())  # Should print 2


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

# Test the Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Should print 1
print(queue.front())  # Should print 2
print(queue.size())  # Should print 2


def is_balanced(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

# Test the function
print(is_balanced("((()))"))  # Should print True
print(is_balanced("(()"))  # Should print False


def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# Test the function
print(reverse_string("Hello, World!"))  # Should print "!dlroW ,olleH"


def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()

# Test the function
names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
print(hot_potato(names, 7))  

##
# Stack class for use in postfix evaluation
class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

# Postfix expression evaluator
def evaluate_postfix(expression):
    stack = Stack()
    for token in expression.split():
        if token.isdigit():
            stack.push(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.push(operand1 + operand2)
            elif token == '-':
                stack.push(operand1 - operand2)
            elif token == '*':
                stack.push(operand1 * operand2)
            elif token == '/':
                stack.push(int(operand1 / operand2))
    return stack.pop()

# Queue using two stacks
class QueueUsingStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):
        self.stack_in.append(item)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            raise IndexError("Queue is empty")
        return self.stack_out.pop()

    def is_empty(self):
        return not self.stack_in and not self.stack_out

    def size(self):
        return len(self.stack_in) + len(self.stack_out)

# Task Scheduler using queue
from collections import deque

class TaskScheduler:
    def __init__(self):
        self.task_queue = deque()

    def add_task(self, task_name):
        self.task_queue.append(task_name)
        print(f"Task '{task_name}' added to the scheduler.")

    def process_tasks(self):
        print("\nStarting task processing...")
        while self.task_queue:
            current_task = self.task_queue.popleft()
            print(f"Processing task: {current_task}")
        print("All tasks have been processed.")

# Test postfix evaluation
print(evaluate_postfix("2 3 +")) 
print(evaluate_postfix("5 1 2 + 4 * + 3 -")) 

# Test queue with two stacks
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue()) 
print(queue.dequeue())  

# Test task scheduler
scheduler = TaskScheduler()
scheduler.add_task("Task 1")
scheduler.add_task("Task 2")
scheduler.process_tasks()


# Function to convert infix expression to postfix
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = Stack()
    postfix = []
    
    for token in expression.split():
        if token.isdigit():  
            postfix.append(token)
        elif token == '(':  
            stack.push(token)
        elif token == ')': 
            top_token = stack.pop()
            while top_token != '(':
                postfix.append(top_token)
                top_token = stack.pop()
        else:  # Token is an operator
            while (not stack.is_empty()) and (precedence[stack.items[-1]] >= precedence[token]):
                postfix.append(stack.pop())
            stack.push(token)
    
    while not stack.is_empty():
        postfix.append(stack.pop())
    
    return ' '.join(postfix)

# Test the function
print(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 )"))  
print(infix_to_postfix("10 + 3 * 5 / ( 16 - 4 )")) 



