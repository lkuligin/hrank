# Enter your code here. Read input from STDIN. Print output to STDOUT
N,l = map(int, raw_input().split())

def connected_components(graph):
    visited = set()
    def component(node):
        nodes = set([node])
        while nodes:
            node = nodes.pop()
            visited.add(node)
            nodes |= graph.get(node, set()) - visited
            yield node
    for node in graph:
        if node not in visited:
            yield component(node)

def count_comb(ar, ones):
    if len(ar) == 0:
        return ones*(ones-1)/2
    res = 0
    l = len(ar)

    for i, el in enumerate(ar):
        j = i + 1
        if j < l:
            res += el * (reduce(lambda x,y: x+y, ar[j:]) + ones)
        else:
            res += el * ones + ones*(ones-1)/2

    if False: '''
    def comb(lst, ones):
        return reduce(lambda x,y: x+y, lst) + ones
    
    def count_recursive(lst, ones):
        if len(lst) == 0:
            return ones * (ones-1) / 2
        elif len(lst) == 1:
            return lst[0] * ones + ones * (ones-1) / 2
        elif len(lst) == 2:
            return lst[0]*lst[1] + ones * (lst[0] + lst[1]) + ones * (ones-1) / 2
        else:
            return lst[0]*comb(lst[1:], ones) + count_(lst[1:], ones)
    '''
    return res
        

graph = {}

for i in xrange(l):
    a,b = map(int, raw_input().split())
    if a in graph:
        graph[a].add(b)
    else:
        graph[a]=set([b])
    if b in graph:
        graph[b].add(a)
    else:
        graph[b]=set([a])

components = []
nodes = set()
for component in connected_components(graph):
    amount = 0
    for el in component:
        nodes.add(el)
        amount += 1
    components.append(amount)

ones = 0
for i in xrange(N):
    if i not in nodes:
        ones += 1
# Compute the final result using the inputs from above
print count_comb(components, ones)
