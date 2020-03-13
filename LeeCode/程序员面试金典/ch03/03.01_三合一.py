"""
三合一。描述如何只用一个数组来实现三个栈。
你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。
stackNum表示栈下标，value表示压入的值。
构造函数会传入一个stackSize参数，代表每个栈的大小。

"""


class TripleInOne:

    def __init__(self, stackSize: int):
        self.d = [0] * stackSize * 3 + [stackSize * 3, 2, 1, 0]

    def push(self, stackNum: int, value: int) -> None:
        if self.d[~stackNum] < self.d[~3]:
            self.d[self.d[~stackNum]] = value
            self.d[~stackNum] += 3

    def pop(self, stackNum: int) -> int:
        if self.d[~stackNum] >= 3:
            self.d[~stackNum] -= 3
            return self.d[self.d[~stackNum]]
        return -1

    def peek(self, stackNum: int) -> int:
        return self.d[~stackNum] < 3 and -1 or self.d[self.d[~stackNum] - 3]

    def isEmpty(self, stackNum: int) -> bool:
        return self.d[~stackNum] < 3


# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
