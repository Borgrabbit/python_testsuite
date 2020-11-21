from collections import deque

def decimal_to_binary(num: int) -> list:
    rx_deque = deque()
    print(num)

    dix_rx = divmod(num, 2)
    print(dix_rx)

    while True:
        div_rx = divmod(num,2)
        quotient = div_rx[0]
        remainder = div_rx[1]
        if quotient == 0:
            rx_deque.appendleft(remainder)
            break;
        else:
            rx_deque.appendleft(remainder)
        num = quotient


    print(rx_deque)
    return rx_deque