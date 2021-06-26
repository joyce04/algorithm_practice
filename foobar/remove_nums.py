from collections import defaultdict


# remove nums included more than n times
def solution(data, n):
    if n == 0:
        data.clear()
        return data

    in_list = defaultdict(int)
    i = 0
    while 0 <= i < len(data):
        d = data[i]
        acc_count = in_list[d]
        if acc_count == 0:
            in_list[d] = 1
            i += 1
        elif acc_count + 1 > n:
            data.pop(i)  # only need to remove itself
            if acc_count == n:  # first check larger than n
                j = i - 1
                while j >= 0:
                    if data[j] == d:
                        data.pop(j)
                        i -= 1
                    j -= 1
            in_list[d] += 1
        else:
            in_list[d] += 1
            i += 1

    return data


def solution2(data, n):
    result = {}

    for minion in data:
        if minion not in result:
            result[minion] = 1
        else:
            result[minion] += 1

    for minion, cnt in result.items():
        if cnt > n:
            for i in range(cnt):
                data.remove(minion)
    return data


if __name__ == '__main__':
    assert (solution([5, 10, 15, 10, 7], 1) == [5, 15, 7])
    # assert (solution([5, 10, 15, 10, 7, 10], 1) == [5, 15, 7])
    # assert (solution([5, 10, 7, 10, 15, 7, 7], 2) == [5, 10, 10, 15])
    # assert (solution([1, 2, 3], 0) == [])
    # assert (solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1) == [1, 4])
    # assert (solution([1, 2, 2, 3, 3, 3, 4, 5, 5, 3], 3) == [1, 2, 2, 4, 5, 5])
    # assert (solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 3) == [1, 2, 2, 3, 3, 3, 4, 5, 5])

    assert (solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 3) == solution2([1, 2, 2, 3, 3, 3, 4, 5, 5], 3))
    assert (solution([1, 22, 21, 3, 3, 3, 41, 5, 5], 2) == solution2([1, 22, 21, 3, 3, 3, 41, 5, 5], 2))
    # assert (solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 3) == solution2([1, 2, 2, 3, 3, 3, 4, 5, 5], 3))
    # assert (solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 3) == solution2([1, 2, 2, 3, 3, 3, 4, 5, 5], 3))
    # assert (solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 3) == solution2([1, 2, 2, 3, 3, 3, 4, 5, 5], 3))
