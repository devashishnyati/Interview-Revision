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
    

