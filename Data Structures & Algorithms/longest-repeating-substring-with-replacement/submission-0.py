class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s = s.lower()
        freq = [0]*26
        l = 0
        max_len = 0
        for r in range(len(s)):
            freq[ord(s[r]) - ord('a')] += 1
            max_freq = max(freq)
            while ((r-l+1) - max_freq) > k:
                freq[ord(s[l]) - ord('a')] -= 1
                l+=1
            max_len = max(max_len, (r-l+1))
        return max_len