# stackSize=3
# d=[0]*stackSize + [stackSize * 3, 2, 1, 0]
# print(d)
# print(d[~2])
# print(~10)

stack=[1,2,3]
stack2=[]
for i in range(3):
    x=stack.pop()
    stack2.append(x)

print(stack2)
