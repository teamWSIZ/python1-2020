
#
# class Element:
#     voltage: float
#     source: ...     #źródło zasilania
#     drains: List    #podłączone kolejne elemnty
#     pass
from level1.p14_inheritance_electronics.declarations import ChainNode


class ChainNode:
    previous: ChainNode
    next: ChainNode


c = ChainNode()

