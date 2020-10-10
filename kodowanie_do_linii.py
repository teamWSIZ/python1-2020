u = 'user8'
s = 12

linia = f'{u},{s}'
print(linia)

g = linia.split(',')
uu = g[0]
ss = int(g[1])
print(f'odkodowałem u={uu}, s={ss}')