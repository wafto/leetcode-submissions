class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        seen = {startGene}
        bank = set(bank)

        def mutate(gene: str) -> List[str]:
            mutations = []
            for i in range(8):
                for molecule in ['A', 'C', 'G', 'T']:
                    if molecule == gene[i]:
                        continue
                    mut = gene[:i] + molecule + gene[i + 1:]
                    if mut in bank:
                        mutations.append(mut)
            return mutations

        while queue:
            gene, generation = queue.popleft()

            if gene == endGene:
                return generation

            for mutation in mutate(gene):
                if mutation in seen:
                    continue
                queue.append((mutation, generation + 1))
                seen.add(mutation)

        return -1
