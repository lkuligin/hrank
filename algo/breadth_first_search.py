# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque 

ONE_STEP = 6


def bfs(graph, source):
    queue = deque()
    queue.append((source, 0))
    visited = set([source])
    paths = [-1]*len(graph)

    while queue:
        cur_node, cur_dist = queue.popleft()
        for neighbour in graph[cur_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                new_dist = cur_dist + ONE_STEP
                paths[neighbour] = new_dist
                queue.append((neighbour, new_dist))
    return paths
            

q = int(raw_input().strip())
for i in xrange(q):
    n, m = map(int, raw_input().strip().split())
    graph = [[] for j in range(n)]
    for j in xrange(m):
        a,b = map(int, raw_input().strip().split())
        a, b = a-1, b-1
        graph[a].append(b)
        graph[b].append(a)
    source = int(raw_input().strip()) - 1
    paths = bfs(graph, source)
    print ' '.join(map(str, paths[:source] + paths[(source+1):]))
