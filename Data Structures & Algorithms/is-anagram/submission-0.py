class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letter_arr = [_ for _ in s]

        for letter in t:
            if letter in letter_arr:
                letter_arr.remove(letter)
            else:
                return False

        return True
        