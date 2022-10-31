class Solution:
    def dfs(self, graph, start, end, visited):
        if start == end:
            return True
        visited[start] = True
        for i in graph[start]:
            if visited[i] == False:
                path = self.dfs(graph, i, end, visited)
                if path == True:
                    return True
        return False

    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = [False for _ in range(n)]
        # print(graph.items())
        return self.dfs(graph, start, end, visited)
