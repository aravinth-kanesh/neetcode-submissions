class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = defaultdict(int)
        
        for ch in s:
            count_s[ch] += 1
        
        for ch in t:
            if ch in count_s:
                count_s[ch] -= 1
            else:
                return False

        for occ in count_s.values():
            if occ != 0:
                return False
        
        return True