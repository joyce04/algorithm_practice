# major, minor, revision
# major 1, 2, 3
# minor new feature 1.0, 1.1, 1.2
# revision small fix 1.1.1, 1.1.2
# 0.1, 0.5... pre-release versions

def get_length(version_str):
    nums = version_str.split('.')
    num_size = len(nums)
    if num_size == 3:
        return len(nums[0]), len(nums[1]), len(nums[2])
    elif num_size == 2:
        return len(nums[0]), len(nums[1]), 0
    else:
        return len(nums[0]), 0, 0


def solution(l):
    # l: list of elevator versions as string
    # return the same list sorted in asceding order by major, minor, revision

    # max # of digits relies on the max length of each numbers
    # "1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2" => length: 1,1,1, 1,1,0, 1,1,1, 1,1,2, 1,1,1 => (1,1,1,1,1), (1,1,1,1,1), (1,0,1,2,1)
    lens = list(zip(*map(lambda x: get_length(x), l)))
    max_lens = [max(lens[1]), max(lens[2]), 0]

    # if maxlen == 1 : possible numbers 0-9[10] = 10^1
    # if maxlen == 2 : possible numbers 0-99[100] ... = 10^2
    # range of ranks -> 0 ~ 10^(major_len + minor_len + version_len)
    def convert_to_rank(version_str):
        nums = version_str.split('.')
        rank = 0
        for i in range(len(nums)):
            rank += (int(nums[i]) + 1) * (10 ** sum(max_lens[i:]))
        return rank

    return sorted(l, key=convert_to_rank)


if __name__ == '__main__':
    assert (solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]) == ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"])
    assert (solution(["1", "1.0", "1.0.0"]) == ["1", "1.0", "1.0.0"])
    assert (solution(["1.0", "1", "1.0.0"]) == ["1", "1.0", "1.0.0"])
    # print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
    assert (solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]) == ['0.1', '1.1.1', '1.2', '1.2.1', '1.11', '2', '2.0', '2.0.0'])
