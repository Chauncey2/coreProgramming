"""
Python 多线程编程示例

1.多线程是一个好东西，但是由于Python的GIL的限制，
python中的多线程适合I/O密集型应用，不适合计算密集型应用

2.对于计算密集型应用，为了实现更好的并行性，需要使用多进程，
以便让CPU的其他内核来执行

3.线程的替代方案
    1. subprocess 模块
    2.multiprocessing 模块
    3.concurrent.futures 模块
"""
