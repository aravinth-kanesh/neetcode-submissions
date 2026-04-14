class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        if n == 1:
            return True

        s_list = list(s)

        if s_list == s_list[::-1]:
            return True

        for i in range(n):
            if i == 0:
                new_list = s_list[1:]
            elif i == n - 1:
                new_list = s_list[:n]
            else:
                new_list = s_list[:i] + s_list[i + 1:]

            if new_list == new_list[::-1]:
                return True

        return False