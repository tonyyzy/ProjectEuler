# a = [[131, 673, 2379, 103, 18],
#      [201, 96, 3792, 965, 150],
#      [630, 803, 7796, 7922, 111],
#      [537, 699, 7997, 121, 956],
#      [805, 732, 5279, 37, 331]]
a = []
with open('p083_matrix.txt') as matrix:
    for i in matrix.readlines():
        b = []
        for j in i.split(','):
            b.append(int(j))
        a.append(b)

from dijkstar import Graph, find_path
graph = Graph()
# counter = 0
# graph.add_edge(1, 2, {'cost': 1})
# graph.add_edge(2, 3, {'cost': 2})
cost_func = lambda u, v, e, prev_e: e['cost']
# print(find_path(graph, 1, 3, cost_func=cost_func))

for i in range(80):
    for j in range(80):
        if 0 < i < 79 and 0 < j < 79:
            graph.add_edge((i, j), (i - 1, j), {'cost': a[i - 1][j]})
            graph.add_edge((i, j), (i, j - 1), {'cost': a[i][j - 1]})
            graph.add_edge((i, j), (i + 1, j), {'cost': a[i + 1][j]})
            graph.add_edge((i, j), (i, j + 1), {'cost': a[i][j + 1]})
        if 0 < i < 79 and j == 0:
            graph.add_edge((i, j), (i - 1, j), {'cost': a[i - 1][j]})
            graph.add_edge((i, j), (i + 1, j), {'cost': a[i + 1][j]})
            graph.add_edge((i, j), (i, j + 1), {'cost': a[i][j + 1]})
        if 0 < i < 79 and j == 79:
            graph.add_edge((i, j), (i - 1, j), {'cost': a[i - 1][j]})
            graph.add_edge((i, j), (i + 1, j), {'cost': a[i + 1][j]})
            graph.add_edge((i, j), (i, j - 1), {'cost': a[i][j - 1]})
        if i == 0 and 0 < j < 79:
            graph.add_edge((i, j), (i, j - 1), {'cost': a[i][j - 1]})
            graph.add_edge((i, j), (i + 1, j), {'cost': a[i + 1][j]})
            graph.add_edge((i, j), (i, j + 1), {'cost': a[i][j + 1]})
        if i == 79 and 0 < j < 79:
            graph.add_edge((i, j), (i - 1, j), {'cost': a[i - 1][j]})
            graph.add_edge((i, j), (i, j + 1), {'cost': a[i][j + 1]})
            graph.add_edge((i, j), (i, j - 1), {'cost': a[i][j - 1]})
        if i == 79 and j == 0:
            graph.add_edge((i, j), (i - 1, j), {'cost': a[i - 1][j]})
            graph.add_edge((i, j), (i, j + 1), {'cost': a[i][j + 1]})
        if i == 79 and j == 79:
            graph.add_edge((i, j), (i - 1, j), {'cost': a[i - 1][j]})
            graph.add_edge((i, j), (i, j - 1), {'cost': a[i][j - 1]})
        if i == 0 and j == 79:
            graph.add_edge((i, j), (i + 1, j), {'cost': a[i + 1][j]})
            graph.add_edge((i, j), (i, j - 1), {'cost': a[i][j - 1]})
        if i == 0 and j == 0:
            graph.add_edge((i, j), (i + 1, j), {'cost': a[i + 1][j]})
            graph.add_edge((i, j), (i, j + 1), {'cost': a[i][j + 1]})

print(find_path(graph, (0, 0), (79, 79), cost_func=cost_func).total_cost + a[0][0])
# print(find_path(graph, (79, 79), (1, 0), cost_func=cost_func).costs)
