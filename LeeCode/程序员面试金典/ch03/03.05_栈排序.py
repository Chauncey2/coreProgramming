class SortedStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.swim(len(self.stack)-1)

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack[0], self.stack[-1] = self.stack[-1], self.stack[0]
        self.stack.pop()
        self.sink(0)

    def peek(self) -> int:
        return self.stack[-1] if not self.stack else -1

    def isEmpty(self) -> bool:
        return not self.stack

    def sink(self, index):
        """
        元素下沉
        :param index:
        :return:
        """
        n = len(self.stack)
        while 2*index+1 < n:
            j = 2*index+1
            if j < n-1 and self.stack[j] > self.stack[j+1]:
                j += 1
            if self.stack[index] <= self.stack[j]:
                break
            self.stack[index], self.stack[j] = self.stack[j], self.stack[index]
            index = j

    def swim(self, index):
        """
        元素上浮
        :param index:
        :return:
        """
        while index > 0 and self.stack[index] < self.stack[(index-1)//2]:
            self.stack[index], self.stack[(index-1)//2] = self.stack[(index-1)//2], self.stack[index]
            index = (index-1)//2


class SortedStack2:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stack.reverse()

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()

    def peek(self) -> int:
        return self.stack and self.stack[0] or -1

    def isEmpty(self) -> bool:
        return not self.stack
