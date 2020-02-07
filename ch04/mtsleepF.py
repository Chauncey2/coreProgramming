from atexit import register
from threading import Thread, Lock, currentThread
from random import randrange
from time import sleep, ctime


class clean_output_set(set):
    def __str__(self):
        return '. '.join(x for x in self)


lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = clean_output_set()


def loop(nsec):
    my_name = currentThread().name  # 保存当前执行该线程的线程名
    lock.acquire()  # 获取锁
    remaining.add(my_name)  # 添加线程名到remaining集合
    print("[{0}] Started {1}".format(ctime(), my_name))
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(my_name)
    print("  (remainning:{0})".format(remaining))
    lock.release()


def main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()


@register
def _atexit():
    print("All done at:{0}".format(ctime()))


if __name__ == '__main__':
    main()
