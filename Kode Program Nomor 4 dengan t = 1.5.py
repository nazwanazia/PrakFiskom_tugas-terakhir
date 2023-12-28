import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan variabel
a = 50
panjang = 0.5
waktu = 1.5
node = 50

dx = panjang / node
dy = panjang / node
dt = min(dx**2 / (4 * a), dy**2 / (4 * a))
t_nodes = int(waktu / dt)
u = np.zeros((node, node)) + 20

u[0, :] = 0
u[-1, :] = 100
u[:, 0] = np.linspace(0, 100, node)
u[:, -1] = np.linspace(0, 100, node)

fig, ax = plt.subplots()
ax.set_ylabel("y (cm)")
ax.set_xlabel("x (cm)")
pcm = ax.pcolormesh(u, cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=ax)

counter = 0
suhu_rata_rata = []  # Menyiapkan list untuk menyimpan suhu rata-rata

while counter < waktu:
    w = u.copy()
    for i in range(1, node-1):
        for j in range(1, node-1):
            dd_ux = (w[i-1, j] - 2*w[i, j] + w[i+1, j]) / dx**2
            dd_uy = (w[j, i-1] - 2*w[i, j] + w[j, i+1]) / dy**2
            u[i, j] = dt * a * (dd_ux + dd_uy) + w[i, j]

    t_mean = np.mean(u)
    suhu_rata_rata.append(t_mean)  # Menyimpan suhu rata-rata

    pcm.set_array(u)
    ax.set_title(f"Distribusi suhu t: {counter:.3f}s, suhu rata-rata={t_mean:.2f}")
    plt.pause(0.01)
    counter += dt

plt.show()

# Plot waktu (sumbu x) terhadap suhu rata-rata (sumbu y)
plt.plot(np.linspace(0, waktu, len(suhu_rata_rata)), suhu_rata_rata)
plt.xlabel('Waktu (s)')
plt.ylabel('Suhu Rata-rata (Celcius)')
plt.title('Perubahan Suhu Rata-rata terhadap Waktu')
plt.grid(True)
plt.show()
