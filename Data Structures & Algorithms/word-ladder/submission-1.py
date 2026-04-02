class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 1. for each word, change each letter to a - z and see if it
        # exists in wordList transformed to a set.
        # 2. If it exists, then the words are different by one position
        # and they are "neighbours" in the graph
        # 3. "Build the graph" for all the words
        # 4. Perform "bfs" from the start word and return when and if
        # the end word is reached

        # edge case - return 0 if no word list given
        if not wordList:
            return 0

        # change wordList into a set for efficiency - O(1) membership
        words = set(wordList)

        # edge case - transformation not possible if end word is not
        # in the list
        if endWord not in words:
            return 0

        # edge case - begin word is the end word
        if beginWord == endWord:
            return 1

        # for when trying different words where only one position has
        # been changed
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        queue = deque([(beginWord, 1)]) # deque for bfs, track "steps"
        visited = set([beginWord]) # set to prevent repeated computations

        while queue:
            for _ in range(len(queue)):
                word, steps = queue.popleft()

                if word == endWord:
                    return steps

                # transform each word by changing a single position
                # check if new word in words
                for i in range(len(word)):
                    for ch in alphabet:
                        newWord = word[:i] + ch + word[i+1:]
                        if newWord in words and newWord not in visited:
                            visited.add(newWord)
                            queue.append((newWord, steps + 1))

        return 0

        # space - O(n x l) for words, O(26) = O(1) for alphabet, O(n x l)
        # for queue and visited as well, where n is number of words and
        # l is the length of words

        # time complexity - for each word of length l, change each position
        # to 26 different characters, and repeat for n words - O(n x l x 26)
        # = o(n x l)



