class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for st in strs:
            freq_map = [0] * 26

            for ch in st:
                freq_map[ord(ch) - ord('a')] += 1

            anagrams[tuple(freq_map)].append(st)

        return list(anagrams.values())
