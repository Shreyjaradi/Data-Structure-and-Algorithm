


# Problem : https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(node):
            for neighbours in rooms[node]:
                if neighbours not in seen:
                    seen.add(neighbours)
                    dfs(neighbours)

        
        seen = set()
        seen.add(0)
        dfs(0)
        return len(seen) == len(rooms)
