def line_6(k, b):
    count_num = [0]
    def create_y(x):
        count_num[0] += 1
        print("这是第%d次执行，当x=%d时，y=%d" % (count_num[0], x, k * x + b))
    return create_y


line_6_1 = line_6(1, 2)
line_6_1(1)
line_6_1(2)
line_6_1(3)
