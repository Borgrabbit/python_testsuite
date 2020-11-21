from collections import Counter

"""
Given a non negative integer number num. 
For every numbers i in the range 0 ≤ i ≤ num calculate the number of 
1's in their binary representation and return them as an array.
"""
# def counting_one_in_binary(num: int) -> list: # 344ms  slower than 95% submission
#     rx = []
#     for n in range(0, num + 1):
#         noc = 0
#         while True:
#             div_rx = divmod(n, 2)
#             quotient = div_rx[0]
#             remainder = div_rx[1]
#             if quotient == 0:
#                 noc += 1 if remainder == 1 else 0
#                 break;
#             else:
#                 noc += 1 if remainder == 1 else 0
#             n = quotient
#         rx.append(noc)
#         # print(rx)
#     print(f'{num} {rx}')
#     return rx


def counting_one_in_binary(num:int)->list: # 256 ms
    rx = [0]
    for n in range(1, num + 1):
        print(Counter(bin(n)))
        cmap = Counter(bin(n))
        rx.append(cmap['1'])
    print(f'{num} {rx}')
    return rx


