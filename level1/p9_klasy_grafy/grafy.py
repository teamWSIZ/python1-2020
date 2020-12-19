"""
Graf składa się z węzłów (ang. node lub vertex)
i krawędzi (ang edge).

Najprostsze grafy to "drzewa":
- istnieje dokładnie jedna "ścieżka" między dowolnymi dwoma node'ami
"""

"""
Najprostszy opis grafu-drzewa:
- w sposób dowolny wybieramy jakoś "node" i nazywamy go "korzeniem"
- dla każdego node'u podajemy kto jest jego "ojcem"
"""

"""
Rozpatrzmy drzewo z 5-cioma node'ami; niech 0 będzie korzeniem
"""

parent = [-1, 0, 0, 2, 2]


# ↑↑ to wystarcza...

# zadanie: stworzyć "lisę list", children, gdzie children[2] to lista dzieci elementu 2

def get_children(parents):
    n = len(parents)
    res = [[] for i in range(n)]
    for p in range(n):
        # przeglądamy każdy węzeł
        for i in range(n):
            if parents[i] == p:
                res[p].append(i)
    return res


print(get_children([-1, 0, 0]))
print(get_children([-1, 0, 0, 2, 2]))
