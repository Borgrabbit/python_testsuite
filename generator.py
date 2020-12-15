from datetime import datetime
import time
import memory_profiler


def generator(ls):
    for i in ls:
        yield i


def process():
    print(f'process ')

    SancList = [n for n in range(1000000)]
    LgList = [11, 22]
    total_cnt = len(SancList) * len(LgList)
    print(f'outer {total_cnt}')
    st = time()
    for sancIdx, sancFullNm in enumerate(SancList):
        for lgIdx, lgFullNm in enumerate(LgList):
            tmp = sancFullNm + lgFullNm
            # print(f'outer {sancFullNm} inner {lgFullNm}')
    print(f'loop {time() - st}')
    st = time()
    for x in generator(SancList):
        for z in generator(LgList):
            tmp = x + z
            # print(f' {x} {z}')
    print(f'generator {time() - st}')


def check_even_gen(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num * num


def check_even_loop(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num * num)

    return even


if __name__ == '__main__':
    # process()

    m1 = memory_profiler.memory_usage()

    st = time.time_ns()
    cubes = check_even_gen(range(100000000))
    # cubes = check_even_loop(range(100000000))
    ed = time.time_ns()
    m2 = memory_profiler.memory_usage()
    time_diff = ed - st
    mem_diff = m2[0] - m1[0]
    print(f"It took {time_diff} Secs and {mem_diff} Mb to execute this method")


    for check_even in (
        check_even_list_append,
        check_even_generator_yield,
        check_even_list_comprehension,
        check_even_generator_expression,
    ):
    t1 = time.time()
    cubes = check_even(range(size))
    result = sum(cubes)  # this is the big difference with the original article
    t2 = time.time()
    print(f"function: {check_even.__name__:31} duration:{t2 - t1:8.4f} s size:{sys.getsizeof(cubes):10}")

