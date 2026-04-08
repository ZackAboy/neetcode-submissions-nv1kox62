class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mostfreq = 0
        freq = [0]*26
        length = 0
        l = 0
        for r in range(len(s)):
            i = ord(s[r].lower()) - ord('a')
            freq[i]+=1
            mostfreq = max(freq)
            while (r-l+1) - mostfreq > k:
                i = ord(s[l].lower()) - ord('a')
                freq[i]-=1
                l+=1
            length = max(length, (r-l+1))
        return length