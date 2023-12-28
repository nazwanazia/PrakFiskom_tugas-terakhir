import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan variabel
a = 500
panjang = 2.5
waktu = 1.5
node = 60

dx = panjang / node
dt = 0.5 * dx**2 / a
t_n = int(waktu / dt)
u = np.zeros(node)

# Kondisi awal dan batas
u[0] = 1  # Syarat batas t[0]
u[-1] = 100  # Syarat batas t[-1]

# Perhitungan distribusi suhu pada t=0.000
for t in range(t_n):
    w = u.copy()
    for i in range(1, node-1):
        u[i] = (dt * a * (w[i-1] - 2*w[i] + w[i+1]) / dx**2) + w[i]

# Visualisasi pada t=0.000
fig, ax = plt.subplots()
ax.set_xlabel("x (cm)")
pcm = ax.pcolormesh([u], cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=ax)
ax.set_ylim([-2, 3])

print("Suhu rata-rata: {:.2f} Celcius".format(np.mean(u)))

pcm.set_array([u])
ax.set_title("Distribusi Suhu pada t: 0.000 s")
plt.show()
