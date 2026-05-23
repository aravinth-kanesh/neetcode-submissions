class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # maps frequency map -> list of anagrams
        anagrams = defaultdict(list)

        # loop through all the strings
        for st in strs:
            # frequency map
            count = [0] * 26

            # populate the frequency map
            for ch in st:
                count[ord(ch) - ord('a')] += 1

            anagrams[tuple(count)].append(st)

        return list(anagrams.values())

            