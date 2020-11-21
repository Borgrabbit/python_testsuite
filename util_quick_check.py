import time
import copy
import collections
import re
import dis

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    a = [1,2]

    print(f'Hi, {a is None}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(f'Hi, {a.index(2)}')  # Press Ctrl+F8 to toggle the breakpoint.

    collections.defaultdict()


def test_collections():
    a = collections.defaultdict(int)
    a['a'] = 1
    print(f"a : {a['b']}")

    b = dict()
    try:
        b['a'] += 1
    except KeyError:
        pass
        # print(KeyError)

    tmp_list = [ 5,5,5,2,3,1,1]
    print( collections.Counter(tmp_list))


def leftextend():

    a = [1,2,3,4,5,6,7]
    b = [8,9,10,11,12,13,14]

    a_deque = collections.deque(a)
    print(f'{a_deque}')
    b_deque = collections.deque(b)
    print(f'{b_deque}')

    etd = a_deque.extendleft(b)
    print(f'{a_deque}')


if __name__ == '__main__':
    pass
    # leftextend()
    # a=256
    # b=256
    # print(a is b)
    # a=257
    # b=257
    # print(a is b)
    # a, b =257,257
    # print(a is b)
    # print( dis.dis(romanToInt) )
    # print( dis.show_code(romanToInt) )

