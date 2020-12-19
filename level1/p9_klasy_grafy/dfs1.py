# zadajemy informację o "dzieciach" w grafie:

g = [[1, 2], [], [3, 4], [], []]
wealth = [100, 20, 20, 1, 1]

sum_wealth = [0]

# Przejście przez graf przy pomocy metody "DFS" (czyli depth-first-search)
def go(node_number):
    print(f'start of processing for {node_number}')
    sum_wealth[0] += wealth[node_number]
    for child in g[node_number]:
        go(child)
    print(f'end of processing for {node_number}')


go(2)
print(sum_wealth[0])
