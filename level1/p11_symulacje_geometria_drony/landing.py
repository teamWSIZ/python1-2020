import random

x = 10  # dron wisi na wysokości 10m
v = 0
a = -9.81  # przyspieszenie grawitacyjne w dół
t = 0
dt = 0.01

while x > 0:
    x += v * dt
    v += a * dt
    t += dt
    v += random.gauss(0, 0.005)  # lekki losowy wiatr w pionie

    # todo: napisać coś, co ustawia wartość `a` w zależności od sim_annealing, v; załóżmy, że abs(a) < 20
    if v < 0:
        if x < 7:
            a = 11.1
        if x < 3:
            a = 5
    else:
        a = -0.1

    print(f't={t:.3f}\tx={x:.6f}\tv={v:.3f}')

if abs(v) > 0.1:
    print('crash')
else:
    print('landed; well done!')
