from collections import defaultdict, Counter


class Solution:
    def commonChars(self, words):
        # words(lower case)
        letter_cnt = Counter(words[0])
        for word in words[1:]:
            next_cnt = Counter(word)
            letter_cnt = {key: min(letter_cnt[key], next_cnt[key]) for key, val in letter_cnt.items()}

        results = []
        for key, val in letter_cnt.items():
            if val > 0:
                results.extend([key] * val)
        return results


if __name__ == '__main__':
    s = Solution()
    assert (s.commonChars(['bella', 'label', 'roller']) == ['e', 'l', 'l'])
    assert (s.commonChars(["cool", "lock", "cook"]) == ["c", "o"])
