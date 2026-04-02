class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict for simplifying edge cases
        anagrams = defaultdict(list)

        for st in strs:
            # build frequency map for string
            freq_map = [0] * 26
            for ch in st:
                freq_map[ord(ch) - ord('a')] += 1
            # use frequency map as key
            anagrams[tuple(freq_map)].append(st)

        return list(anagrams.values())
            