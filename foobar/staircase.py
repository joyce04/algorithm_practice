from collections import defaultdict


# budget, types of bricks
# want to know # different types of staircases can be built

# constraints: should consists of 2 or more steps
# no two steps are at the same height-- each step must be lower than the previous one
# all steps must contain at least 1 brick
# A step's height = total amount of bricks that make up that step
# N = 3 => 2, 1
# N = 4 => 3, 1
# N=5 => 4,1 or 3,2
# N=6 => 51, 42, 123

def default_val():
    return -1


def solution(n):
    recursive_cache = defaultdict(default_val)

    def dfs(src, limit):
        if recursive_cache[(src, limit)] > -1:
            return recursive_cache[(src, limit)]

        if src - limit <= limit:
            return 0
        else:
            subnode_num = 0
            for sec in range(limit, int(src / 2) + 1):
                next_node = src - sec
                if next_node > sec:
                    node_num = 1 + dfs(src - sec, sec + 1)
                    subnode_num += node_num
            recursive_cache[(src, limit)] = subnode_num

            return subnode_num

    total_count = dfs(n, 1)

    return total_count


if __name__ == '__main__':
    assert (solution(3) == 1)
    assert (solution(4) == 1)
    assert (solution(5) == 2)
    assert (solution(6) == 3)
    assert (solution(7) == 4)
    assert (solution(8) == 5)
    assert (solution(10) == 9)  # 19    28    37    46    127 136 145 235 1234
    assert (solution(11) == 11)  # 19    28    37    46    127 136 145 235 1234
    assert (solution(200) == 487067745)  # 110 29 38
    # print(solution(200))
