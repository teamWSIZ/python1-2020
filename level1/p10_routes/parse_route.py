import subprocess
from typing import List, Dict, Set
from igraph import Graph, plot

# output = subprocess.check_output('traceroute 1.1.1.1', shell=True).decode('UTF-8')
# output = subprocess.check_output('traceroute 8.8.8.8', shell=True).decode('UTF-8')
# output = subprocess.check_output('traceroute 91.200.38.109', shell=True).decode('UTF-8')
from level1.p10_routes.graph_utils import default_style
from level1.p10_routes.line_parser import TracerouteNode, parse_traceroute_line_linux

"""
Zadanie: zrobić strukturę (klasę) która będzie trzymała informację o grafie sieci internet, 
i miała metody update'owania tej informacji wg. wyników działania komendy traceroute. 

Powinna istnieć też metoda exportowania grafu w postacji png'ka. 
"""


class NetworkRouteMonitor:
    net: Dict[str, Set] = {}
    nodes: Dict[str, TracerouteNode] = {}

    def insert_edge(self, ip_from: str, ip_to: str):
        if ip_from not in self.net:
            self.net[ip_from] = set()
        self.net[ip_from].add(ip_to)

    def insert_route(self, trace_nodes: List[TracerouteNode]):
        # przejść przez listę i pododawać linki
        n = len(trace_nodes)
        first = trace_nodes[0]
        if not first.hidden:
            self.nodes[first.ip] = first
        for i in range(1, n):
            previous, current = (trace_nodes[i - 1], trace_nodes[i])
            if previous.hidden or current.hidden:  # hidden node blokuje linki (ale pozostałe dalej są OK)
                continue
            self.insert_edge(previous.ip, current.ip)
            self.nodes[current.ip] = current

    def use_target(self, ip, limit_range = 20):
        """
        Wykonuje traceroute na `ip`, i dane wynikowe zapamiętuje w strukturze sieci
        """
        output = subprocess.check_output(f'traceroute {ip}', shell=True).decode('UTF-8')
        lines = output.splitlines()[1:]
        nodes = []
        for line in lines:
            nodes.append(parse_traceroute_line_linux(line))
        self.insert_route(nodes)

    def plot(self, filename='network.png'):
        g = Graph(directed=True)
        n = len(self.nodes)
        g.add_vertices(n)

        # ponumerujmy wszystkie node'y
        number = {}  # ip -> number
        x = 0
        for node in self.nodes.values():
            print(f'adding node: {node}')
            g.vs[x]['id'] = x
            g.vs[x]['label'] = node.ip + f'({node.hostname})'
            number[node.ip] = x
            x += 1

        # Add edges
        edges = []
        for (ip, children) in self.net.items():
            for ch in children:
                edges.append((number[ip], number[ch]))

        print(edges)

        g.add_edges(edges)
        out_name = filename
        plot(g, out_name, **default_style(g))


monitor = NetworkRouteMonitor()
ips = ['1.1.1.1', '8.8.8.8', '91.200.38.109', 'google.pl',  '100.0.0.1', '31.13.81.36']
for ip in ips:
    monitor.use_target(ip, limit_range=5)
# monitor.use_target('1.1.1.1')
# # for i in range(8):
# monitor.use_target('8.8.8.8')
# monitor.use_target('91.200.38.109')
# monitor.use_target('google.pl')

monitor.plot('net1.png')
monitor.plot('net2.png')
monitor.plot('net3.png')
monitor.plot('net4.png')