class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val: int) -> None:
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        """
        :rtype: void
        """
        self.stack.pop()


    def top(self) -> int:
        """
        :rtype: int
        """
        return self.stack[-1][0]


    def getMin(self) -> int:
        """
        :rtype: int
        """
        return self.stack[-1][1]
        
