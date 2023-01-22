#Problem :  https://leetcode.com/problems/number-of-provinces/description/



from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            print("graph[node] : ", graph[node])
            for neighbours in graph[node]:
                if neighbours not in seen:
                    seen.add(neighbours)
                    dfs(neighbours)

        n = len(isConnected)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        print(graph)
        seen = set()
        ans = 0
        for i in range(n):
            if i not in seen:
                ans +=1 
                seen.add(i)
                dfs(i)
        return ans
