w = [1, 2, 3, 2, 1]
# w = [1]
# w = []
# w = [1,1]

"""
Cel programu: sprawdzić czy lista wygląda tak samo czytana od początku 
i od końca (wspak).  
"""

is_ok = True
for i in range(len(w)):
    print(f'z lewej: {w[i]}, z prawej: {w[-1-i]}')
    if w[i] != w[-1-i]:
        is_ok = False

print(f'lista jest ok? {is_ok}')
