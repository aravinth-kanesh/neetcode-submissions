class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) # frequency map of string -> [anagram1, anagram2]
        
        # loop through all strings
        for st in strs:
            # convert string to frequency map representation
            key = [0] * 26 # each index represents a lowercase char

            for ch in st:
                key[ord(ch) - ord('a')] += 1

            key = tuple(key) # array cannot be used as a dictionary key
            anagrams[key].append(st) # append original string

        return list(anagrams.values()) # .values() returns a dict_values object

