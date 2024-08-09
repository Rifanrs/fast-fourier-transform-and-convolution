from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve

def perform_fft():
    # Ambil nilai parameter dari input fields
    latitude = float(latitude_input.get())
    longitude = float(longitude_input.get())
    kedalaman = float(kedalaman_input.get())
    magnitudo = float(magnitudo_input.get())

    # Lakukan perhitungan FFT sesuai dengan parameter yang diambil
    x = np.linspace(0, 10, 1000)
    y = np.sin(2 * np.pi * x) * magnitudo * np.exp(-0.1 * x)  # Contoh perhitungan FFT

    # Gantilah perhitungan FFT di atas sesuai dengan parameter-parameter yang diambil
    # Sebagai contoh, Anda dapat menggantinya dengan:
    # y = np.sin(2 * np.pi * x) * magnitude * np.exp(-0.1 * x) * np.exp(-0.1 * kedalaman)
    # atau perhitungan lainnya yang sesuai dengan parameter yang ingin digunakan.

    fft_result = np.fft.fft(y)
    N = len(y)
    frequencies = np.fft.fftfreq(N)
    positive_frequencies = frequencies[:N//2]
    magnitude = np.abs(fft_result[:N//2])

    # Hapus data grafik FFT yang ada sebelumnya
    ax_fft.cla()

    # Lakukan plotting ulang pada grafik FFT dengan hasil perhitungan yang baru
    ax_fft.plot(positive_frequencies, magnitude)
    ax_fft.set_title('Grafik FFT')
    ax_fft.set_xlabel('Frekuensi (Hz)')
    ax_fft.set_ylabel('Magnitude')
    ax_fft.grid(True)

    # Memanggil canvas_fft.draw() untuk menampilkan grafik yang telah diperbarui
    canvas_fft.draw()

def perform_konvolusi():
    # Ambil nilai parameter dari input fields
    latitude = float(latitude_input.get())
    longitude = float(longitude_input.get())
    kedalaman = float(kedalaman_input.get())
    magnitudo = float(magnitudo_input.get())

    # Data yang akan dikonvolusi (misalnya, data_array)
    data_array = np.random.rand(1000)  # Data acak sebagai contoh

    # Kernel konvolusi (sesuaikan dengan kebutuhan)
    kernel = np.array([latitude, longitude, kedalaman, magnitudo])

    # Lakukan konvolusi pada data
    result = convolve(data_array, kernel, mode='same')

    # Hapus data grafik konvolusi yang ada sebelumnya
    ax_konvolusi.cla()

    # Lakukan plotting ulang pada grafik konvolusi dengan hasil perhitungan yang baru
    ax_konvolusi.plot(result)
    ax_konvolusi.set_title('Grafik Konvolusi')
    ax_konvolusi.set_xlabel('Indeks Data')
    ax_konvolusi.set_ylabel('Nilai Konvolusi')
    ax_konvolusi.grid(True)

    # Memanggil canvas_konvolusi.draw() untuk menampilkan grafik yang telah diperbarui
    canvas_konvolusi.draw()

def resetgrafik():
    global ax_fft, ax_konvolusi

    ax_fft.clear()
    ax_fft.set_title('Grafik FFT')
    ax_fft.set_xlabel('Frekuensi (Hz)')
    ax_fft.set_ylabel('Magnitude')
    ax_fft.grid(True)

    ax_konvolusi.clear()
    ax_konvolusi.set_title('Grafik Konvolusi')
    ax_konvolusi.set_xlabel('Indeks Data')
    ax_konvolusi.set_ylabel('Nilai Konvolusi')
    ax_konvolusi.grid(True)

    canvas_fft.draw()
    canvas_konvolusi.draw()

root = Tk()
root.title("Aplikasi FFT dan Konvolusi")
root.resizable(width=False, height=False)

WIDTH = 1400
HEIGHT = 700
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='lightblue')
canvas.pack()

frameInput = Frame(root, bg='#074447')
frameInput.place(relx=0.025, rely=0.5, relwidth=0.25, relheight=0.7, anchor='w')

# Menambahkan input fields untuk parameter-parameter yang ingin diubah
latitude_label = Label(frameInput, bg='#074447', text='Latitude (°S)', fg='white')
latitude_label.place(relx=0.12, rely=0, relwidth=0.26, relheight=0.125, anchor='n')
latitude_input = Entry(frameInput)
latitude_input.place(relx=0.5, rely=0.025, relwidth=0.52, relheight=0.08, anchor='n')

longitude_label = Label(frameInput, bg='#074447', text='Longitude (°E)', fg='white')
longitude_label.place(relx=0.12, rely=0.125, relwidth=0.26, relheight=0.125, anchor='n')
longitude_input = Entry(frameInput)
longitude_input.place(relx=0.5, rely=0.15, relwidth=0.52, relheight=0.08, anchor='n')

kedalaman_label = Label(frameInput, bg='#074447', text='Kedalaman (km)', fg='white')
kedalaman_label.place(relx=0.12, rely=0.25, relwidth=0.26, relheight=0.125, anchor='n')
kedalaman_input = Entry(frameInput)
kedalaman_input.place(relx=0.5, rely=0.275, relwidth=0.52, relheight=0.08, anchor='n')

magnitudo_label = Label(frameInput, bg='#074447', text='Magnitudo', fg='white')
magnitudo_label.place(relx=0.12, rely=0.375, relwidth=0.26, relheight=0.125, anchor='n')
magnitudo_input = Entry(frameInput)
magnitudo_input.place(relx=0.5, rely=0.4, relwidth=0.52, relheight=0.08, anchor='n')

# Tombol "Submit" untuk memproses input FFT
submit_button_fft = Button(frameInput, text='Submit FFT', command=perform_fft)
submit_button_fft.place(relx=0.5, rely=0.6, relwidth=0.4, relheight=0.1, anchor='n')

# Tombol "Submit" untuk memproses input Konvolusi
submit_button_konvolusi = Button(frameInput, text='Submit Konvolusi', command=perform_konvolusi)
submit_button_konvolusi.place(relx=0.5, rely=0.75, relwidth=0.4, relheight=0.1, anchor='n')

# Tombol "Reset" untuk mereset grafik
reset_button = Button(frameInput, text='Reset', command=resetgrafik)
reset_button.place(relx=0.5, rely=0.9, relwidth=0.4, relheight=0.1, anchor='n')

# Membuat area untuk menampilkan grafik FFT
frameGrafik_fft = Frame(root, bg='white')
frameGrafik_fft.place(relx=0.3, rely=0.5, relwidth=0.3, relheight=0.7, anchor='w')

# Menentukan ukuran figur untuk grafik FFT
figsize_fft = (8, 4)  # Ubah sesuai dengan ukuran yang Anda inginkan (panjang, tinggi)
f_fft = Figure(figsize=figsize_fft)

ax_fft = f_fft.add_subplot(111)

ax_fft.set_title('Grafik FFT')
ax_fft.set_xlabel('Frekuensi (Hz)')
ax_fft.set_ylabel('Magnitude')
ax_fft.grid(True)

canvas_fft = FigureCanvasTkAgg(f_fft, frameGrafik_fft)
canvas_fft.get_tk_widget().place(relheight=1, relwidth=1)

# Membuat area untuk menampilkan grafik konvolusi
frameGrafik_konvolusi = Frame(root, bg='white')
frameGrafik_konvolusi.place(relx=0.63, rely=0.5, relwidth=0.3, relheight=0.7, anchor='w')

# Menentukan ukuran figur untuk grafik konvolusi
figsize_konvolusi = (8, 4)  # Ubah sesuai dengan ukuran yang Anda inginkan (panjang, tinggi)
f_konvolusi = Figure(figsize=figsize_konvolusi)

ax_konvolusi = f_konvolusi.add_subplot(111)

ax_konvolusi.set_title('Grafik Konvolusi')
ax_konvolusi.set_xlabel('Indeks Data')
ax_konvolusi.set_ylabel('Nilai Konvolusi')
ax_konvolusi.grid(True)

canvas_konvolusi = FigureCanvasTkAgg(f_konvolusi, frameGrafik_konvolusi)
canvas_konvolusi.get_tk_widget().place(relheight=1, relwidth=1)


# Membuat area untuk menampilkan grafik konvolusi
frameGrafik_konvolusi = Frame(root, bg='white')
frameGrafik_konvolusi.place(relx=0.63, rely=0.5, relwidth=0.3, relheight=0.7, anchor='w')

f_konvolusi = Figure()
ax_konvolusi = f_konvolusi.add_subplot(111)

ax_konvolusi.set_title('Grafik Konvolusi')
ax_konvolusi.set_xlabel('Indeks Data')
ax_konvolusi.set_ylabel('Nilai Konvolusi')
ax_konvolusi.grid(True)

canvas_konvolusi = FigureCanvasTkAgg(f_konvolusi, frameGrafik_konvolusi)
canvas_konvolusi.get_tk_widget().place(relheight=1, relwidth=1)

root.mainloop()
