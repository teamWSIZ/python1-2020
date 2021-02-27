
"""
Robot reaguje na trzy komendy: "L", "R", i "F";
L - wykonuje skręt w lewo o 90 stopni
R - wykonuje skręt w prawo o 90 stopni
F - "forward" - przemieszcza się o 1 metr do przodu

Napisać funkcję która dla podanego zestawu komend odpowiada "True" jeśli robot wrócił do pozycji wyjściowej
(niezależnie od aktualnego ukierunkowania), lub "False", gdy po wykonaniu komend robot znajduje się w miejscu
innym niż początkowe.

Przykłady:
"LR" → True
"FLFLFLF" → True
"FFFFLFFF" → False
"FFFLLFFF" → True
"""