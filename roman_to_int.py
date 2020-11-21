def roman_to_int(s) -> int:
    map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'SIG_L': 0
    }
    skip_flag = False
    rx = 0
    for i in range(len(s)-1, -1, -1):
        cc = s[i]
        nix = i-1
        if i != 0:
            nc = s[nix]
            # print(f' {i} {nc} {cc} {rx}')
            if map[nc] < map[cc]:
                if skip_flag:
                    skip_flag = False
                else:
                    rx += map[cc] - map[nc]
                    skip_flag = True
            else:
                if skip_flag:
                    skip_flag = False
                else:
                    rx += map[cc]
        else:
            if skip_flag:
                skip_flag = False
            else:
                rx += map[cc]

    return rx