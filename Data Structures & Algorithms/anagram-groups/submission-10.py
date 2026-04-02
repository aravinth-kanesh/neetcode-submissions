class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap to map frequency map of string -> list of anagrams
        # use defaultdict to simplify edge cases
        anagrams = defaultdict(list)

        # loop through strings
        for st in strs:
            # initialise frequency map for string
            freq_map = [0] * 26

            # loop through every character in the string
            for ch in st:
                # increment count for each character
                # words are all lowercase so can do this safely
                freq_map[ord(ch) - ord('a')] += 1

            # add string to list stored under frequency map
            anagrams[tuple(freq_map)].append(st)

        return list(anagrams.values())