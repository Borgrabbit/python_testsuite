class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # self.stack = collections.deque()
        self.stack = []
        self.min = float('inf')

    def push(self, x: int) -> None:
        if x <= self.min:
            self.min = x
        self.stack.append(x)

    def pop(self) -> None:
        if self.min == self.stack[-1]:
            stack = self.stack
            stack = sorted(stack, reverse=True)
            del stack[-1]
            if len(stack) == 0:
                self.min = float('inf')
            else:
                self.min = stack[-1]
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # s1
        # return min(self.stack)

        # s2
        # if len(self.stack) == 0:
        #     return self.stack
        # else:
        #     self.stack = sorted(self.stack, reverse=True)
        #     return self.stack[-1]

        # s3
        return self.min