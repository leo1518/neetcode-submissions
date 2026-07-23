class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        temp = {}
        longest = 0
        for i in range(len(s)):

            if s[i] in temp:
                start = max(start, temp[s[i]] + 1)

            temp[s[i]] = i

            longest = max(longest, i - start + 1)

        return longest