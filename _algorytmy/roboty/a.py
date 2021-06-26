# pozycje:
x = [5, 10, 15]
t = "RLR"

# symulacja w czasie...
"""
5 10 15
6 9 16
7 8 17
7 8 18 
6 9 19 ...
-------------
t = "RLR"
x = [6, 10, 16]
7 9 17
8 8 18  💥💥💥 eksplozja 💥💥💥   2 roboty znikają!
19
20 
30 
"""


"""
Zadanie 1)
Mając dane "x" i "t" narysować oś z robotami ... roboty przedstawić symbolami → ... i ← w zależności od kierunku ruchu
def print_robots(x, t): ....

Zadanie 2)
Mając dane początkowe "x" i "t" wykonać pętlę w czasie symulując problem... włącznie ze zderzeniami robotów...
Wybuch proszę zaznaczyć symbolem '💥'. 


"""