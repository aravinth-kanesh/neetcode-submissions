class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for st in strs:
            key = [0] * 26
            for ch in st:
                key[ord(ch) - ord('a')] += 1
            anagrams[tuple(key)].append(st)

        return list(anagrams.values())