import subprocess
from dataclasses import dataclass
from typing import List, Dict, Set

# output = subprocess.check_output('traceroute 1.1.1.1', shell=True).decode('UTF-8')
# output = subprocess.check_output('traceroute 8.8.8.8', shell=True).decode('UTF-8')
# output = subprocess.check_output('traceroute 91.200.38.109', shell=True).decode('UTF-8')
from level1.p10_routes.line_parser import TracerouteNode, parse_traceroute_line_linux

"""
Zadanie: zrobić strukturę (klasę) która będzie trzymała informację o grafie sieci internet, 
i miała metody update'owania tej informacji wg. wyników działania komendy traceroute. 

Powinna istnieć też metoda exportowania grafu w postacji png'ka. 
"""


class NetworkRouteMonitor:
    net: Dict[str, Set] = {}

    def insert_edge(self, ip_from: str, ip_to: str):
        if ip_from not in self.net:
            self.net[ip_from] = set()
        self.net[ip_from].add(ip_to)

    def insert_route(self, nodes: List[TracerouteNode]):
        # przejść przez listę i pododawać linki
        n = len(nodes)
        for i in range(1, n):
            self.insert_edge(nodes[i - 1].ip, nodes[i].ip)

    def use_target(self, ip):
        output = subprocess.check_output(f'traceroute {ip}', shell=True).decode('UTF-8')
        lines = output.splitlines()[1:]
        nodes = []
        for line in lines:
            nodes.append(parse_traceroute_line_linux(line))
        self.insert_route(nodes)



monitor = NetworkRouteMonitor()
monitor.use_target('1.1.1.1')
monitor.use_target('91.200.38.109')
# monitor.use_target('google.pl')
print(monitor.net)
for (k,v) in monitor.net.items():
    print(f'{k} --> {v}')
