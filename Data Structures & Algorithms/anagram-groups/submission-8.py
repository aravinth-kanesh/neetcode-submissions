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

        # time - loop through every string, and every char in the string
        # - O(n * k), where n is the number of strings and k is the max
        # length of any of the strings
        
        # space - frequency map for each string is O(1). All of the
        # original strings and the characters they have are stored in
        # the output list, so time complexity is O(n * k) as well

        # better than sorting method which would be O(n * klogk)
            