"""

              (01)----→ (21)↓
(00) ---------↑             ------
              (20)----→ (21)↑

"""

w = [0] * (5 * 10 ** 8)     # tablica n elementów typu "int" zabiera 8 * n B pamięci...
input('ready')


b = [[0, 0, 0, 1], [1, 0, 2, 3], [0, 1, 2, 4], [0, 0, 0, 0]]    # 16 * 8 = 128 B

"""
00 0
10 1  --> 3 bity na pozycję; łącznie 16 * 3 = 48 bitów... 6B 

-------------------------
[1234]
[1243]
...
[4312]
[4321]  4! ... 24... permutacji... 5bitów... [0..31] ... i to numeruje permutację... 
zapisanie zer jednego rzędu...
[0110]  1: tam jest cyfra; 0: nie ma cyfry... ====> 5bitów + 4bity ==> 9bitów na rząd... 

redukcja biorąca pod uwagę rząd i kolumnę  "podwójna"
-o--  
 |
 |
 |
 
redukcja biorąca pod uwagę tylko rząd lub kolumnę "pojedyncza"
1034  => 0 musi być 2 (w sudoku) 
 
 
"""