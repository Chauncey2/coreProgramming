"""
栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。
最多只能使用一个其他的临时栈存放数据，但不得将元素复制到别的数据结构（如数组）中。
该栈支持如下操作：push、pop、peek 和 isEmpty。当栈为空时，peek 返回 -1。

解题思路：
根据题目描述，是只要将最小元素置于栈顶即可，不需要其他位置有序

"""


class SortedStack:

    def __init__(self):
        self.min_val = 0
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            # 如果栈为空；
            self.stack.append(val)
            self.min_val=val
        if self.min_val:
            pass

    def pop(self) -> None:
        pass

    def peek(self) -> int:
        pass

    def isEmpty(self) -> bool:
        pass
