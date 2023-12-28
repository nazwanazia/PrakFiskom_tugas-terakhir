import numpy as np
import matplotlib.pyplot as plt

# Variabel yang diminta
a = 500
panjang = 2.5
waktu = 1.5
node = 50

dx = panjang / node
dt = 0.5 * dx**2 / a
t_n = int(waktu / dt)
u = np.zeros(node) + 20

# Kondisi batas
u[0] = 1
u[-1] = 100

# Menyiapkan list untuk menyimpan suhu rata-rata
suhu_rata_rata = []

for t in range(t_n):
    w = u.copy()
    for i in range(1, node-1):
        u[i] = (dt * a * (w[i-1] - 2*w[i] + w[i+1]) / dx**2) + w[i]
    suhu_rata_rata.append(np.mean(u))

# Plot waktu (sumbu x) terhadap suhu rata-rata (sumbu y)
plt.plot(np.linspace(0, waktu, t_n), suhu_rata_rata)
plt.xlabel('Waktu (s)')
plt.ylabel('Suhu Rata-rata (Celcius)')
plt.title('Perubahan Suhu Rata-rata terhadap Waktu')
plt.grid(True)
plt.show()
