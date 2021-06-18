x = 0
v = 0
a = 1
t = 0
dt = 0.00001

while t < 1:
    x += v * dt
    v += a * dt
    t += dt
    print(f't={t:.3f}\tx={x:.6f}\tv={v:.3f}')



# sim_annealing = a * t**2 / 2
