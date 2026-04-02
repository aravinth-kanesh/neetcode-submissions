class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = []

        for ch in s:
            if ch.isalnum():
                st.append(ch.lower())

        final_st = "".join(st)

        left, right = 0, len(final_st) - 1
        while left <= right:
            if final_st[left] != final_st[right]:
                return False
            left += 1
            right -= 1

        return True
