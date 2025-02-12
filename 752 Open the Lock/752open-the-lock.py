class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        def next_posibilities(node: str) -> List[str]:
            ans = []
            for i in range(4):
                num = int(node[i])
                for change in [-1, 1]:
                    x = (num + change) % 10
                    ans.append(node[:i] + str(x) + node[i + 1:])
            return ans


        seen = set(deadends)
        queue = deque([('0000', 0)])

        while queue:
            node, turns = queue.popleft()
            
            if node == target:
                return turns

            for nxt in next_posibilities(node):
                if nxt not in seen:
                    queue.append((nxt, turns + 1))
                    seen.add(nxt)

        return -1

