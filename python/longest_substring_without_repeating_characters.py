def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        charSet = set()
        left = 0
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                max_len = max(max_len, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        return max_len