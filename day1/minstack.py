"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

class MinStackUsingTwoStacks:
    # Time: O(1) for all operations
    # Space: O(2n) => O(n)
    def __init__(self):
        self.min_stack = []
        self.min_value_stack = []
        MAX_INTEGER = float('inf')
        self.min_value_stack.append(MAX_INTEGER)

    def push(self, val):
        if val < self.min_value_stack[-1]:
            self.min_value_stack.append(val)
        else:
            self.min_value_stack.append(self.min_value_stack[-1])
        
        self.min_stack.append(val)
        


    def top(self):
        return self.min_stack[-1]

    def get_min(self):
        return self.min_value_stack[-1]

    def pop(self):
        self.min_value_stack.pop()
        self.min_stack.pop()

class MinStackUsingOneStack:
    # Time: O(1) for all operations
    # Space: O(2n) => O(n)
    def __init__(self):
        self.min_stack = []
        MAX_INTEGER = float('inf')
        self.min_value = MAX_INTEGER

    def push(self, val):
        if val <= self.min_value:
            self.min_stack.append(self.min_value)
            self.min_value = val
        self.min_stack.append(val)


    def top(self):
        return self.min_stack[-1]

    def get_min(self):
        return self.min_value

    def pop(self):
        curr_top = self.min_stack.pop()
        if curr_top == self.min_value:
            self.min_value = self.min_stack.pop()

if __name__ == "__main__":
    min_stack = MinStackUsingOneStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.get_min())
    min_stack.pop()
    print(min_stack.top())
    print(min_stack.get_min())
    

