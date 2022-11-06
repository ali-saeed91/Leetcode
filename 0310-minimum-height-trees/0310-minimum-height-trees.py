class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        queue, degrees = [], {}
        for node, neighbors in adj.items():
            degrees[node] = len(neighbors)
            # Insert all leaves into our priority queue.
            if degrees[node] == 1:
                queue.append(node)
        ans = []
        while queue:
            nodes = []
            while queue:
                nodes.append(queue.pop())
            ans = nodes
            for node in nodes:
                degrees[node] -= 1
                for neighbor in adj[node]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        queue.append(neighbor)
        return ans