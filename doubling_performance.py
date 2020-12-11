import time
import dis
from collections import deque
# import textdistance

class Performance:
    def __init__(self):
        self.test = 0

# def test1():
#     ham1 = textdistance.Levenshtein()
#     st1 = time.perf_counter()
#     rx = round(ham1.normalized_similarity('pyxdameraul wwevenshtein', 'damerau_levenserhtein_distance') * 100)
#     ed1 = time.perf_counter()
#     print(f'[rx]: {rx} {ed1 - st1}')
#
#
# def test2():
#     ham2 = textdistance.Levenshtein()
#     st2 = time.perf_counter()
#     rx = round(ham2.normalized_similarity('pyxdameraul wwevenshtein', 'damerau_levenserhtein_distance') * 100)
#     ed2 = time.perf_counter()
#     print(f'[rx with extra]: {rx} {ed2 - st2}')

def doubling_list(num=1):
    rx = []
    st = time.perf_counter()
    for n in range(num):
        rx.append([n])
    print(f'list.append([{num}]) {time.perf_counter() - st}')

    rx = []
    temp = [None] * 5
    st = time.perf_counter()
    for n in range(num):
        temp[0] = n
        rx.append(temp)
    print(f'list.append({num}) {time.perf_counter() - st} rxArray separated')

    st = time.perf_counter()
    # rx = [n for n in [z for z in range(num)]]
    rx = [temp[0] for n in range(num)]
    print(f'list.append({num}) {time.perf_counter() - st} list_comprehension[list_comprehension]')

    st = time.perf_counter()
    rx = [(z for z in range(num))]
    print(f'list.append({num}) {time.perf_counter() - st} list_comprehension[generator]')

    rx = []
    st = time.perf_counter()
    for n in range(num):
        rx.append(n)
    print(f'list.append({num}) {time.perf_counter() - st}')

    # str = ''
    # st = time.perf_counter()
    # for el in rx:
    #     str = el
    # print(f'list unpack ({len(rx)}) {time.perf_counter() - st} | {str}')


def doubling_deque(num=1):
    rx = deque()
    st = time.perf_counter()
    for n in range(num):
        rx.append([n])
    print(f'deque.append([{num}]) {time.perf_counter() - st}')

    rx = deque()
    temp = [None] * 5
    st = time.perf_counter()
    for n in range(num):
        temp[0] = n
        rx.append(temp)
    print(f'deque.append({num}) {time.perf_counter() - st} rxArray separated')

    rx = deque()
    st = time.perf_counter()
    for n in range(num):
        temp[0] = n
        rx.append(n)
    print(f'deque.append({num}) {time.perf_counter() - st}')

    # str = ''
    # st = time.perf_counter()
    # for el in rx:
    #     str = el
    # print(f'deque unpack ({len(rx)}) {time.perf_counter() - st} | {str}')


if __name__ == '__main__':
    # test1()
    # test2()
    doubling_list(3_000_000)
    doubling_list(2_500_000)
    doubling_list(2_000_000)
    doubling_deque(3_000_000)
    doubling_deque(2_500_000)
    doubling_deque(2_000_000)
    # dis.dis(doubling_list)
    # dis.dis(doubling_deque)
