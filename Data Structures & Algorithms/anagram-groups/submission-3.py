class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            res[tuple(freq)].append(word)

        return list(res.values())