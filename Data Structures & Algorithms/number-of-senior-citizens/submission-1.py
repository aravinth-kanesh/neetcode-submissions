class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ages = [int(details[i][11:13]) for i in range(len(details))]
        seniors = 0
        for age in ages:
            if age > 60:
                seniors += 1
        return seniors
