class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # test : "" => "" --
        # test : "a" => "a" --
        # test : "ab" => "a" --
        # test : 'aa' => "aa"
        # test : "babad" => "bab"
        # test : "abcba" => "abcba"
        # test : "xybccbzy" => "bccb"

        if len(s) < 2:
            return s

        #         longest_p = ''
        #         for i in range(0, len(s)):
        #             for j in range(1, len(s)+1):
        #                 if s[i:j] == s[i:j][::-1] and j-i > len(longest_p):
        #                     longest_p = s[i:j]

        #         return longest_p

        def expand_from_middle(s, left, right):
            if left > right:
                return 0

            while left > 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left, right

        start_idx = 0
        end_idx = 0
        s_left, l_right = len(s), 0
        for i in range(len(s)):
            l1, r1 = expand_from_middle(s, i, i)
            # len2 = expand_from_middle(s, i, i + 1)
            # longer_len = len1  # max(len1, len2)
            if s_left > l1 and l_right < r1:
                s_left = l1
                l_right = r1
                # if longer_len % 2 == 0:
                #     start_idx = i - (longer_len / 2)
                #     end_idx = i + (longer_len / 2)
                # else:
                #     start_idx = i - longer_len
                #     end_idx = i + longer_len
                #     if start_idx < 0:
                #         start_idx = 0

        return s[int(s_left):int(l_right)]


if __name__ == '__main__':
    s = Solution()
    # print(s.longestPalindrome('aba'))
    print(s.longestPalindrome('babad'))
    print(s.longestPalindrome('abba'))
    print(s.longestPalindrome('xybccbzy'))
    print(s.longestPalindrome('a'))
    print(s.longestPalindrome('ac'))
    print(s.longestPalindrome('bcb'))
    print(s.longestPalindrome('abcbx'))
    print(s.longestPalindrome('cbb'))
