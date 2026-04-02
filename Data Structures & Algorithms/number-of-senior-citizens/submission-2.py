class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum([int(person[11:13]) > 60 for person in details])
