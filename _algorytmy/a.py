for i in range(100):
    try:
        for j in range(100):
            # jeśli j = 30 weź następny i, ale nie kontynuuj dalej tego co jest pod pętlą po j
            if j == 30:
                raise RuntimeError()
        print('ok')  # nie chcemy by to wykonało...
    except:
        print('kontnuujemy dalej pętlę po i')

for i in range(100):
    ok = True
    for j in range(100):
        if j == 30:
            ok = False
            break
    if ok:
        print('pętla j skończyła się normalnie')
    else:
        print('wyszliśmy z pętli j przedwcześnie')

# albo --> for--else:
print('---------')
for i in range(200):
    for j in range(400):
        pass
        if j == 30:
            break
    else:
        print('pętla skończyła się normalnie')
