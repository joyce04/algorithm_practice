# access code lucky triple (x, y, z): y%x==0 & z%y==0

# def solution(l):
#     if len(l) < 3:
#         return 0
#     l = sorted(l)
#     total_count = 0
#     for i in range(len(l) - 2):
#         for j in range(i + 1, len(l) - 1):
#             for z in range(j + 1, len(l)):
#                 if l[z] % l[j] == 0 and l[j] % l[i] == 0:
#                     total_count += 1
#     return total_count


# if same number included >= 3 : triplet +1
# if same number included >= 2 : num_size * num_multiples
# if same number included == 1: combination with multiples
from collections import defaultdict


def solution(l):
    cnt = 0
    multiple_cnt = defaultdict(int)
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[j] % l[i] == 0:
                multiple_cnt[j] += 1
                cnt += multiple_cnt[i]

    return cnt


if __name__ == '__main__':
    assert (solution([1, 2, 3, 4, 5, 6]) == 3)  # => [1, 2, 4], [1, 2, 6], [1, 3, 6] 3
    assert (solution([1, 1, 1]) == 1)
    assert (solution([7, 1, 8, 8, 1, 1, 3, 4]) == 8)  # => [111, 113, 114, 117, 118, 148, 188, 488]
    assert (solution([2, 2, 4]) == 1)
    assert (solution([2, 2, 4, 4]) == 4)
