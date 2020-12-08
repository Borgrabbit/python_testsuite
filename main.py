import time
import copy
import collections
import re
import dis

from decimal_to_binary import decimal_to_binary
from counting_bits_388 import counting_one_in_binary
from bttmt_121 import max_profit_sol, max_profit, max_profit_brute
from roman_to_int import roman_to_int
from minstack import MinStack



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
    counting_one_in_binary(5)
    counting_one_in_binary(2)
    counting_one_in_binary(64)
    # counting_one_in_binary(634)
    # counting_one_in_binary(511)
    # counting_one_in_binary(1)

    # print(max_profit([7,1,5,6,4]))
    # print(max_profit([7,6,4,3,1]))
    # print(max_profit([2,4,1]))
    # print(max_profit([3,2,6,5,0,3]))
    # print(max_profit([1,4,1,4,3,1]))
    # print(max_profit([2,1,2,0,1]))
    # print(max_profit([]))
    # print(max_profit_brute([7,1,5,6,4]))
    # print(max_profit_brute([7,6,4,3,1]))
    # print(max_profit_brute([2,4,1]))
    # print(max_profit_brute([3,2,6,5,0,3]))
    # print(max_profit_brute([1,4,1,4,3,1]))
    # print(max_profit_brute([2,1,2,0,1]))
    # print(max_profit_brute([]))
    # print(max_profit_sol([7,1,5,6,4]))
    # print(max_profit_sol([7,6,4,3,1]))
    # print(max_profit_sol([2,4,1]))
    # print(max_profit_sol([3,2,6,5,0,3]))
    # print(max_profit_sol([1,4,1,4,3,1]))
    # print(max_profit_sol([2,1,2,0,1]))
    # print(max_profit_sol([]))

    # leftextend()
    # valid_palindrome()
    # lengthOfLongestSubstring("abcabcbb")
    # lengthOfLongestSubstring("bbbbb")
    # lengthOfLongestSubstring("pwwkew")
    # roman_to_int("III")
    # roman_to_int("IV")
    # roman_to_int("IX")
    # roman_to_int("LVIII")
    # roman_to_int("MCMXCIV")

    # ["MinStack", "push", "push", "push", "top", "pop", "getMin", "pop", "getMin", "pop", "push", "top", "getMin",
    #  "push", "top", "getMin", "pop", "getMin"]
    # [[], [2147483646], [2147483646], [2147483647], [], [], [], [], [], [], [2147483647], [], [], [-2147483648], [], [],
    #  [], []]

    # stack = MinStack()
    # stack.push(-2)
    # stack.push(0)
    # stack.push(-3)
    # print(stack.stack)
    # stack.top()
    # stack.pop()
    # stack.pop()
    # stack.pop()
    # print(stack.stack)
    # print(stack.getMin())
    #
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
    # print(stack.getMin() )

