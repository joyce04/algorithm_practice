def solution(n):
    total_steps = 0
    num = int(n)

    while num > 1:
        if num & 1 == 0:  # multiple of 2
            num >>= 1
        elif num == 3 or num % 4 == 1:  # multiple of 3 -> minus 1
            num = num - 1
        else:  # other odd -> plus 1
            num = num + 1

        total_steps += 1
    return total_steps


if __name__ == '__main__':
    assert (solution('15') == 5)
    assert (solution('4') == 2)
    assert (solution('33') == 6)
    assert (solution('0') == 0)
