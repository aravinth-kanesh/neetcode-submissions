class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = "".join(char.lower() for char in s if char.isalnum())
        left, right = 0, len(filtered_string) - 1
        while left <= right:
            if filtered_string[left] != filtered_string[right]:
                return False
            left += 1
            right -= 1
        return True
