from dataclasses import dataclass



@dataclass
class TracerouteNode:
    ip: str
    hostname: str
    rt_time: int
    hidden: bool = False


instancja = TracerouteNode('1.1.1.1', 'one.one.one.one', 12)
print(instancja)
