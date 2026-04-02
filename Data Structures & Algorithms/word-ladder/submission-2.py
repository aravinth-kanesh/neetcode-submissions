class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        if beginWord == endWord:
            return 1

        words = set(wordList)
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            for _ in range(len(queue)):
                word, steps = queue.popleft()

                if word == endWord:
                    return steps

                for i in range(len(word)):
                    for ch in alphabet:
                        newWord = word[:i] + ch + word[i+1:]

                        if newWord in words and newWord not in visited:
                            visited.add(newWord)
                            queue.append((newWord, steps + 1))

        return 0


