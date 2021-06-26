

x = 107 #seed
s = set()

for i in range(10000):
    x = (x * 37 + 103) % 1013
    # print(sim_annealing)
    s.add(x)

print(len(s))
