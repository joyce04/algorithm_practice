from collections import defaultdict


# from enum import Enum

# class Directions(Enum):
#     TOP_LEFT = -17
#     TOP_RIGHT = -15
#     BOTTOM_LEFT = 15
#     BOTTOM_RIGHT = 17
#     RIGHT_TOP = -6
#     RIGHT_BOTTOM = 10
#     LEFT_TOP = -10
#     LEFT_BOTTOM = 6

# knight can move to 8 different positions on the chess board at max
# chessboard is numbered from 0 to 63
def inside_board(cur, direction):
    q, r = divmod(cur, 8)
    next_pos = cur + direction
    q2, r2 = divmod(next_pos, 8)
    if 0 <= next_pos <= 63 and abs(q - q2) < 3 and abs(r - r2) < 3:
        return True, next_pos
    else:
        return False, 0


def solution(src, dest):
    queue = [(src, 0)]
    visited = defaultdict(int)
    visited[src] = 1

    while len(queue) > 0:
        cur = queue.pop(0)
        cur_pos, cur_dist = cur[0], cur[1]

        if cur_pos == dest:
            return cur_dist

        for direction in [-17, -15, 15, 17, -6, 10, -10, 6]:
            on_board, pos = inside_board(cur_pos, direction)
            if on_board and visited[pos] == 0:
                visited[pos] = 1
                queue.append((pos, cur_dist + 1))


if __name__ == '__main__':
    assert (solution(0, 1) == 3)
    assert (solution(19, 36) == 1)
    assert (solution(12, 28) == 2)
    assert (solution(0, 9) == 4)
    assert (solution(9, 18) == 2)
    assert (solution(0, 63) == 6)
    assert (solution(0, 55) == 5)
    assert (solution(63, 0) == 6)
    assert (solution(1, 18) == 1)
    assert (solution(45, 45) == 0)
