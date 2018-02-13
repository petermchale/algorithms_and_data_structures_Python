# https://www.youtube.com/watch?v=VmogG01IjYc

from heaps import Min_Heap, Max_Heap


def add_number(number, lowers, highers):
    if lowers.size() == 0 or number < lowers.top():
        lowers.push(number)
    else:
        highers.push(number)


def smaller_bigger_heaps(lowers, highers):
    smaller_heap = highers if lowers.size() > highers.size() else lowers
    bigger_heap = lowers if lowers.size() > highers.size() else highers

    return smaller_heap, bigger_heap


def rebalance(lowers, highers):
    smaller_heap, bigger_heap = smaller_bigger_heaps(lowers, highers)

    if bigger_heap.size() > smaller_heap.size() + 1:
        smaller_heap.push(bigger_heap.pop())


def median(lowers, highers):
    smaller_heap, bigger_heap = smaller_bigger_heaps(lowers, highers)

    if bigger_heap.size() == smaller_heap.size():
        return 0.5 * (bigger_heap.top() + smaller_heap.top())
    else:
        return bigger_heap.top()


def get_medians():
    lowers = Max_Heap()
    highers = Min_Heap()

    n = int(raw_input().strip())
    for i in xrange(n):
        number = int(raw_input().strip())
        add_number(number, lowers, highers)
        rebalance(lowers, highers)
        print '%1.1f' % median(lowers, highers)


if __name__ == '__main__':
    get_medians()
