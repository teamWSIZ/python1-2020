
cities = ['Bielsko', 'Jasienica', 'Szczyrk', 'Kozy', 'Kęty', 'Kobiernice', 'Czechowice']
while True:
    i = input('podaj pierwsze 2 litery miasta> ')
    print(f'wpisałeś: [{i}]')
    matching = []
    for c in cities:
        if c.startswith(i):
            matching.append(c)
    print(f'Pasujące miasta: {matching}')