g = [[], [], []]  # dotychczas
# g = [set, set, set]

s = set()
s.add(10)
s.add(15)
s.add(38)
s.add(10)
s.add(10)

print(s)


di = {}
di['a'] = 'b'
di['b'] = 'c'
print(di)

#informacja o sąsiadach danego IP powinna być typu Dict[str,Set[str]]
net = dict()

net['1.1.1.1'] = set()
net['1.1.1.1'].add('2.2.2.2')
net['1.1.1.1'].add('3.3.3.3')

if not '1.1.1.2' in net:
    net['1.1.1.2'] = set()
net['1.1.1.2'].add('3.3.3.3')
