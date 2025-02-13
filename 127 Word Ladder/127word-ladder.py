class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        idx_chars = defaultdict(set)
        wordList = set(wordList)

        for word in wordList:
            for i, c in enumerate(word):
                idx_chars[i].add(c)

        def posibilities(word: str) -> List[str]:
            pos = []
            for i in range(len(word)):
                for c in idx_chars[i]:
                    if word[i] == c:
                        continue
                    w = word[: i] + c + word[i + 1:]
                    if w in wordList:
                        pos.append(w)
            return pos

        queue = deque([(beginWord, 1)])
        seen = {beginWord}

        while queue:
            node, steps = queue.popleft()
            if node == endWord:
                return steps
            for nei in posibilities(node):
                if nei in seen:
                    continue
                queue.append((nei, steps + 1))
                seen.add(nei)

        return 0