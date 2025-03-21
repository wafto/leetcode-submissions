class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        cookable = {s: True for s in supplies}
        recipe_index = {r: i for i, r in enumerate(recipes)}

        def dfs(r: str) -> bool:
            if r in cookable:
                return cookable[r]

            if r not in recipe_index:
                return False

            cookable[r] = False

            for nei in ingredients[recipe_index[r]]:
                if not dfs(nei):
                    return False

            cookable[r] = True
            return cookable[r]

        return [r for r in recipes if dfs(r)]
        