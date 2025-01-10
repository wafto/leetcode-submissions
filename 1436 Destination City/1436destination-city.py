class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        routing = { s: e for s, e in paths }
        curr = paths[0][0]

        while curr in routing:
            curr = routing[curr]

        return curr
