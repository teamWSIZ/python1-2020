import subprocess
from dataclasses import dataclass
from typing import List

# output = subprocess.check_output('ping -c 3 1.1.1.1', shell=True).decode('UTF-8')
# output = subprocess.check_output('traceroute 8.8.8.8', shell=True).decode('UTF-8')
output = subprocess.check_output('traceroute 91.200.38.109', shell=True).decode('UTF-8')
lines = output.splitlines()
print(lines)

@dataclass
class TracerouteNode:
    ip: str
    hostname: str
    rt_time: int
    hidden: bool = False  # node containing * * *

    @staticmethod
    def hidden_node():
        return TracerouteNode('', '', 0, True)


def parse_route(lines: List[str]):
    route = []
    for l in lines:
        if l.__contains__('*'):
            route.append(TracerouteNode.hidden_node())
            continue
        s = l.split(' ')
        print(s)
        rtt = sum([float(g) for g in (s[6], s[9], s[12])]) / 3
        tn = TracerouteNode(s[4][1:-1], s[3], rt_time=round(rtt))
        print(tn)
        route.append(tn)


parse_route(lines[1:])
