class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList) # for faster membership checks
        print(f"Word set: {word_set}")

        # early return
        if beginWord == endWord:
            return 1

        # edge case
        if endWord not in word_set:
            return 0

        """start with beginWord. bfs implemenation - start with beginWord 
        in queue iterate through every char in the word, changing it to a - z. 
        if it becomes a word in word_set, append it to the queue. attach the 
        sequence length at each step. if the transformed word is the endWord, 
        return the sequence length. if the queue is empty, return 0 since that 
        means beginWord cannot be transformed to endWord."""

        # define all lowercase letters
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        queue = deque([(beginWord, 1)]) # (word, sequence_length)

        visited = set() # prevents infinite loops

        while queue:
            word, length = queue.popleft()

            # iterate through every char in the word
            for i in range(len(word)):
                # iterate through all possible lowercase letters
                for ch in alphabet:
                    # don't want to overwrite existing word
                    new_word = word[:i] + ch + word[i + 1:]

                    if new_word in visited:
                        continue

                    # check if transformed word is the endWord
                    if new_word == endWord:
                        return length + 1

                    # check if transformed word is in word_set
                    if new_word in word_set:
                        visited.add(new_word)
                        queue.append((new_word, length + 1))

        # beginWord cannot be transformed to endWord
        return 0

                

            



        
            

        