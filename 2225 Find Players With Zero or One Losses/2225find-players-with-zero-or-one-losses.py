class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = dict()
        
        for winner, losser in matches:
            if winner not in players:
                players[winner] = 0
            if losser not in players:
                players[losser] = 0
            players[losser] += 1
            
        ans = [[], []]
        
        for player, count in players.items():
            if count == 0:
                ans[0].append(player)
            if count == 1:
                ans[1].append(player)
                
        ans[0].sort()
        ans[1].sort()

        return ans
            