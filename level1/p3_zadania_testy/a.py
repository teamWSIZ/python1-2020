w = [1, 2, 3, 4, 5, 6]

print(w[2:4])   # podlista z `w` zawierająca elementy od 2go (liczone od 0) do 4 wyłączonego, czyli [3, 4]
print(w[2:-1])  # podlista od elementu 2 do ostatniego, wyłączonego, [3, 4, 5]

print(w[:-1])   # podlista od początku do ostatniego, wyłączonego [1, 2, 3, 4, 5]

print(sum(w[:3]))
