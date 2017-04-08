import heapq


# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m, k = map(int, raw_input().split())

class Supermarkets(object):
    def __init__(self):
        self.supermarkets = {}

    def visit_node(self, node, mask):
        new_mask = mask
        for fish in self.supermarkets.get(node, []):
            new_mask = new_mask | 1 << fish
        return new_mask

    def __getitem__(self, key):
        return self.supermarkets.get(key, None)

    def __setitem__(self, key, value):
        self.supermarkets[key] = value

    def __contains__(self, item):
        return item in self.supermarkets

    def __len__(self):
        return len(self.supermarkets)

    def __str__(self):
        return str(self.supermarkets)


def dijkstra(graph, source, target, supermarkets, mask_wished = None):
    dist = {}
    source_mask = supermarkets.visit_node(source, 0)
    dist[source] = {}
    queue = []
    for x in range(target+1):
        dist[x] = {}
    dist[source][source_mask] = 0

    heapq.heappush(queue, (0, source, source_mask))

    while queue:
        cur_dist, min_dist_node, mask = heapq.heappop(queue)

        for neighbour, vertex_dist in graph[min_dist_node]:
            #if cur_dist + vertex_dist
            alt = cur_dist + vertex_dist
            new_mask = supermarkets.visit_node(neighbour, mask)
            #print min_dist_node, neighbour, mask, new_mask, alt, dist
            if alt < dist[neighbour].get(new_mask, float('inf')):
                dist[neighbour][new_mask] = alt
                heapq.heappush(queue, (alt, neighbour, new_mask))
                #print dist
    return dist[target]

def best_dist(target, k):
    mask_wished = 2 ** k 
    best_dist = float('inf')
    for cat1 in xrange(mask_wished):
        for cat2 in xrange(cat1, mask_wished, 1):
            if cat1 | cat2 == mask_wished-1 and cat1 in target and cat2 in target:
                best_dist = min(best_dist, max(target[cat1],target[cat2]))
    return best_dist

def reverse_path(path, source, target):
    res = []
    cur_node = target
    while cur_node:
        res.append(cur_node)
        cur_node = path.get(cur_node)
    return res[::-1]


supermarkets = Supermarkets()
roads = {}
for i in xrange(n):
    roads[i] = []
distances = {}

for i in xrange(n):
    input = map(int, raw_input().split())
    if input[0] > 0:
        supermarkets[i] = [j-1 for j in input[1:]]

for i in xrange(m):
    a, b, c = map(int, raw_input().split())
    roads[a-1].append((b-1,c))
    roads[b-1].append((a-1,c))

full_path = dijkstra(roads, 0, n-1, supermarkets)

#print supermarkets
#print full_path
print best_dist(full_path, k)