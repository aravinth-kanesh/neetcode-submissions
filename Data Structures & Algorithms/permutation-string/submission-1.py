class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count_s1 = [0] * 26

        for ch in s1:
            count_s1[ord(ch) - ord('a')] += 1
        
        count_s2 = [0] * 26
        left = 0
        for right in range(len(s2)):
            count_s2[ord(s2[right]) - ord('a')] += 1

            if (right - left + 1) > len(s1):
                count_s2[ord(s2[left]) - ord('a')] -= 1
                left += 1

            if count_s1 == count_s2:
                return True

        return False

            

