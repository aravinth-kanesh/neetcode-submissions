class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # edge case
        if not strs:
            return []

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
            # list is not hashable so must cast to hashable tuple
            anagrams[tuple(freq_map)].append(st)

        # return grouped anagrams
        return list(anagrams.values())

        # time - O(m * n), where m is the number of strings and n is the
        # length of the longest string

        # space - stores all original strings in the output list, so also
        # O(m * n)

    def test_group_anagrams():
        s = Solution()

        # normal
        assert s.groupAnagrams(["act","pots","tops","cat","stop","hat"]) == [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        # empty input
        assert s.groupAnagrams([]) == []

        # single string
        assert s.groupAnagrams(["x"]) == [["x"]]

        # more tests for all strings are anagrams, none are anagrams, etc.

