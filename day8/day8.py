class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i

            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            self.num_sets -= 1
            return True
        return False


with open("input.txt", 'r') as f:
    lines = f.readlines()

points = [tuple(map(int, line.split(','))) for line in lines]

n = len(points)
edges = []

for i in range(n):
    for j in range(i + 1, n):
        p1 = points[i]
        p2 = points[j]
        dist = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
        edges.append((dist, i, j))

edges.sort(key=lambda x: x[0])

dsu1 = UnionFind(n)
pairs = edges[:1000]

for _, u, v in pairs:
    dsu1.union(u, v)

sizes = []
roots = set()

for i in range(n):
    root = dsu1.find(i)
    if root not in roots:
        sizes.append(dsu1.size[root])
        roots.add(root)

sizes.sort(reverse=True)
res1 = sizes[0] * sizes[1] * sizes[2]

dsu2 = UnionFind(n)
res2 = 0
for dist, u, v in edges:
    if dsu2.union(u, v):
        if dsu2.num_sets == 1:
            p_u = points[u]
            p_v = points[v]
            res2 = p_u[0] * p_v[0]
            break

print(res1)
print(res2)
