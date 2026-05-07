from IPython.display import HTML
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# =========================
# TITIK AWAL
# =========================
points = {
    "A": (2, 3),
    "B": (2, 4),
    "C": (3, 4),
    "D": (3, 3),
    "I": (2, 2),
    "J": (3, 2),
    "K": (2, 1),
    "L": (3, 1),
    "M": (2, -1),
    "N": (3, -1),
    "O": (2, -2),
    "P": (3, -2),
    "E": (2, -3),
    "F": (3, -3),
    "G": (2, -4),
    "H": (3, -4)
}

# =========================
# MEMBUAT FIGURE
# =========================
fig, ax = plt.subplots(figsize=(8,8))

titik_asli = {}
titik_cermin = {}

# =========================
# MEMBUAT TITIK
# =========================
for nama, (x, y) in points.items():

    # Titik asli
    p1 = ax.plot(x, y, 'bo', markersize=8)[0]
    t1 = ax.text(x + 0.1, y + 0.1, nama)

    # Titik cermin
    p2 = ax.plot(-x, y, 'ro', markersize=8)[0]
    t2 = ax.text(-x + 0.1, y + 0.1, nama + "'")

    titik_asli[nama] = (p1, t1)
    titik_cermin[nama] = (p2, t2)

# =========================
# TAMPILAN GRAFIK
# =========================
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

ax.axhline(0, color='black')
ax.axvline(0, color='black')

ax.grid(True)

plt.title("Animasi Transformasi Cermin Bertukar Tempat")

# =========================
# FUNGSI ANIMASI
# =========================
def animate(frame):

    # Gerak maju lalu kembali
    if frame <= 100:
        t = frame / 100
    else:
        t = (200 - frame) / 100

    for nama, (x, y) in points.items():

        # Transformasi refleksi sumbu Y
        x_asli = x + (-x - x) * t
        x_cermin = -x + (x + x) * t

        # Update titik asli
        titik_asli[nama][0].set_data([x_asli], [y])
        titik_asli[nama][1].set_position((x_asli + 0.1, y + 0.1))

        # Update titik cermin
        titik_cermin[nama][0].set_data([x_cermin], [y])
        titik_cermin[nama][1].set_position((x_cermin + 0.1, y + 0.1))

# =========================
# MEMBUAT ANIMASI
# =========================
animasi = FuncAnimation(
    fig,
    animate,
    frames=201,
    interval=40,
    repeat=True
)

# =========================
# SIMPAN OUTPUT
# =========================
plt.savefig("hasil_transformasi.png")

animasi.save(
    "animasi_transformasi.gif",
    writer="pillow"
)

# =========================
# TAMPILKAN
# =========================
HTML(animasi.to_jshtml())

plt.show()