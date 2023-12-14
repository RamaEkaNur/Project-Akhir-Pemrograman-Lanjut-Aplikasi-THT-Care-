import tkinter as tk
from tkinter import messagebox
import webbrowser

# Membuat list index angka dari checkboxes
def nama_gejala():
    penyakit = []
    for i in range(1, 21):
        if eval("gejala" + str(i)).get() == 1:
            penyakit.append(i)
    return penyakit

def show_causes():
    penyakit = nama_gejala()

    causes = ""
    if set(penyakit) == {1, 3, 7, 12, 13, 15, 16}:
        causes = "Influenza disebabkan oleh virus influenza, berkontak langsung dengan penderita, dan perubahan cuaca."
    elif set(penyakit) == {3, 12, 13, 15, 16}:
        causes = "Sinusitis disebabkan oleh infeksi virus atau bakteri pada sinus."
    elif set(penyakit) == {1, 5, 7, 11, 13, 14, 15, 20}:
        causes = "ISPA (Infeksi Saluran Pernapasan Akut) dapat disebabkan oleh berbagai virus, asap rokok, dan polusi udara."
    elif set(penyakit) == {1, 7, 8, 9, 17, 18}:
        causes = "Radang Tenggorokan (Tonsilitis) dapat disebabkan oleh infeksi bakteri atau virus."
    elif set(penyakit) == {4, 5, 6, 8, 11, 17, 18}:
        causes = "Faringitis dapat disebabkan oleh infeksi virus atau bakteri."
    elif set(penyakit) == {1, 5, 9, 10, 14}:
        causes = "Laringitis dapat disebabkan oleh infeksi virus atau overuse pada pita suara."
    elif set(penyakit) == {1, 2, 5, 6}:
        causes = "Sakit Tenggorokan Biasa dapat disebabkan oleh infeksi virus, asap rokok, gejala influenza, dan terlalu banyak minum air dingin."
    elif set(penyakit) == {1, 5, 11, 15, 16, 18}:
        causes = "Demam Biasa dapat disebabkan oleh infeksi virus dan perubahan cuaca."
    else:
        causes = "Penyebab gejala Anda tidak dapat diidentifikasi dengan pasti."

    messagebox.showinfo("Penyebab Penyakit", causes)

def check():
    penyakit = nama_gejala()

    if set(penyakit) == {1, 3, 7, 12, 13, 15, 16}:
        result = "Kamu mungkin terjangkit Influenza."
    elif set(penyakit) == {3, 12, 13, 15, 16}:
        result = "Kamu mungkin terjangkit Sinusitis."
    elif set(penyakit) == {1, 5, 7, 11, 13, 14, 15, 20}:
        result = "Kamu mungkin terjangkit ISPA."
    elif set(penyakit) == {1, 7, 8, 9, 17, 18}:
        result = "Kamu mungkin terjangkit Radang Tenggorokan (Tonsilitis)."
    elif set(penyakit) == {4, 5, 6, 8, 11, 17, 18}:
        result = "Kamu mungkin terjangkit Faringitis."
    elif set(penyakit) == {1, 5, 9, 10, 14}:
        result = "Kamu mungkin terjangkit Laringitis."
    elif set(penyakit) == {1, 2, 5, 6}:
        result = "Kamu mungkin terjangkit Sakit Tenggorokan Biasa."
    elif set(penyakit) == {1, 5, 11, 15, 16, 18}:
        result = "Kamu mungkin terjangkit Demam Biasa."
    else:
        result = "Gejala Anda tidak sesuai dengan penyakit yang diketahui."

    messagebox.showinfo("Hasil Diagnosis", result)

def show_medicine():
    penyakit = nama_gejala()

    if set(penyakit) == {1, 3, 7, 12, 13, 15, 16}:
        medicine = "Influenza dapat diredakan dengan meminum Decolgen atau OBH Flu."
    elif set(penyakit) == {3, 12, 13, 15, 16}:
        medicine = "Sinusitis dapat diredakan dengan meminum Ibuprofen, Dekongestan, atau Amoxicillin jika penyebabnya infeksi bakteri."
    elif set(penyakit) == {1, 5, 7, 11, 13, 14, 15, 20}:
        medicine = "ISPA dapat diredakan dengan meminum lemon/madu hangat dan berkumur dengan air garam hangat jika diikuti sakit tenggorokan. Ibuprofen atau Paracetamol digunakan untuk meredakan Demam dan nyeri otot."
    elif set(penyakit) == {1, 7, 8, 9, 17, 18}:
        medicine = "Radang Tenggorokan (Tonsilitis) dapat diredakan dengan meminum lemon/madu hangat dan berkumur dengan air garam hangat. Minum Amoxicillin atau Paracetamol untuk meredakan nyeri."
    elif set(penyakit) == {4, 5, 6, 8, 11, 17, 18}:
        medicine = "Faringitis dapat diredakan dengan meminum Gramicidin jika masih gejala ringan. Benzocaine bisa diminum untuk meredakan sakit tenggorokan dan sulit menelan. Ibuprofen atau Paracetamol untuk meredakan nyeri dan menurunkan demam."
    elif set(penyakit) == {1, 5, 9, 10, 14}:
        medicine = "Laringitis dapat diredakan dengan meminum Ibuprofen dan Paracetamol untuk pereda nyeri. Perbanyak minum air putih lalu dibantu dengan berkumur dengan air garam hangat."
    elif set(penyakit) == {1, 2, 5, 6}:
        medicine = "Sakit Tenggorokan Biasa dapat diredakan dengan meminum FG Troches Meiji dan jauhi makanan kering/berminyak."
    elif set(penyakit) == {1, 5, 11, 15, 16, 18}:
        medicine = "Demam Biasa dapat diredakan dengan meminum Panadol."
    else:
        medicine = "Tidak diketahui Obat yang cocok untuk Anda berdasarkan Gejala yang Anda alami."

    messagebox.showinfo("Rekomendasi Obat", medicine)


class MapApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Map Viewer")

        # List of locations (latitude, longitude, location name)
        self.locations = [
            (-7.960818440530058, 112.61332056639891, "Apotek Sutami"),
            (-7.965310805269022, 112.61348220900562, "Apotek Sumber Waras"),
            (-7.966549301871388, 112.61344551191301, "Apotek Efata"),
            (-7.957472756127353, 112.6060854834687, "Apotek Sigura-Gura"),
            (-7.9566900410854045, 112.60557371251726, "Apotek Mahameru"),
            (-7.954734861701998, 112.61114589432005, "Apotek Telaga Nabi"),
            (-7.951924228881902, 112.60901971875393, "Apotek K-24 Gajayana Malang"),
            (-7.951313253338103, 112.60868357178236, "Apotek Green Pharmacy"),
            (-7.957185289857003, 112.61846336979914, "Apotek Plus"),
        ]

        # Create buttons for each location and pack them
        frame_apotek = tk.Frame(master)
        frame_apotek.pack(padx=20, pady=20)

        for i, (latitude, longitude, location_name) in enumerate(self.locations):
            button = tk.Button(frame_apotek, text=location_name, command=lambda lat=latitude, lon=longitude: self.view_location(lat, lon))
            button.grid(row=i // 3, column=i % 3, pady=5, padx=5)

    def view_location(self, latitude, longitude):
        # Open Google Maps in the default web browser with the specified location and marker
        url = f"https://www.google.com/maps?q={latitude},{longitude}&z=15&t=m"
        webbrowser.open(url)


def open_main_window():
    login_window.destroy()

    window = tk.Tk()
    window.title("THT - Care")
    window.geometry("500x700")

    # Frame buat checkboxes
    frame_checkbox = tk.Frame(window)
    frame_checkbox.pack(padx=20, pady=20)

    label_check = tk.Label(window, text="Tolong pilih gejala yang selama ini kamu alami.")
    label_check.pack(padx=20, pady=20)

    checkbox(frame_checkbox)

    # Frame buat buttons
    frame_buttons = tk.Frame(window)
    frame_buttons.pack(padx=20, pady=20)

    button_check = tk.Button(frame_buttons, text="Check", command=check)
    button_check.grid(row=0, column=0, pady=20, padx=20)

    button_causes = tk.Button(frame_buttons, text="Penyebab", command=show_causes)
    button_causes.grid(row=0, column=1, pady=20, padx=20)

    button_medicine = tk.Button(frame_buttons, text="Obat", command=show_medicine)
    button_medicine.grid(row=1, column=0, pady=20, padx=20)

    button_map = tk.Button(frame_buttons, text="Pembelian", command=lambda: MapApp(window))
    button_map.grid(row=1, column=1, pady=20, padx=20, rowspan=2)

    global label_result
    label_result = tk.Label(window, text="")
    label_result.pack(padx=20, pady=20)

    window.mainloop()

# Cek login akun
def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "samadi" and password == "tersedak_lontong":
        open_main_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def checkbox(frame):
    gejala = [("Batuk Kering", 1), ("Batuk Berdahak Bening", 2), ("Batuk Berdahak Kuning/Hijau", 3), ("Batuk Kering Menarik Diafragma", 4),
             ("Tenggorokan Kering", 5), ("Tenggorokan Gatal", 6), ("Nyeri Tenggorokan", 7), ("Sulit Menelan", 8),
             ("Suara Serak", 9), ("Hilang Suara", 10), ("Mual Muntah", 11), ("Hidung Tersumbat", 12),
             ("Hidung Berlendir", 13), ("Gangguan Pernapasan", 14), ("Gangguan Penciuman", 15), ("Gangguan Pengecapan", 16),
             ("Demam", 17), ("Sakit Kepala", 18), ("Nyeri Perut", 19), ("Nyeri Dada", 20)]

    global gejala1, gejala2, gejala3, gejala4, gejala5, gejala6, gejala7, gejala8, gejala9, gejala10, gejala11, gejala12, gejala13, gejala14, gejala15, gejala16, gejala17, gejala18, gejala19, gejala20
    gejala1 = tk.IntVar()
    gejala2 = tk.IntVar()
    gejala3 = tk.IntVar()
    gejala4 = tk.IntVar()
    gejala5 = tk.IntVar()
    gejala6 = tk.IntVar()
    gejala7 = tk.IntVar()
    gejala8 = tk.IntVar()
    gejala9 = tk.IntVar()
    gejala10 = tk.IntVar()
    gejala11 = tk.IntVar()
    gejala12 = tk.IntVar()
    gejala13 = tk.IntVar()
    gejala14 = tk.IntVar()
    gejala15 = tk.IntVar()
    gejala16 = tk.IntVar()
    gejala17 = tk.IntVar()
    gejala18 = tk.IntVar()
    gejala19 = tk.IntVar()
    gejala20 = tk.IntVar()

    # Bikin Checkbutton 2x2
    for i in range(len(gejala)):
        tk.Checkbutton(frame, text=gejala[i][0], variable=eval("gejala" + str(i + 1))).grid(row=i//2, column=i%2, sticky=tk.W)

# Create login window
login_window = tk.Tk()
login_window.title("Login Screen")
login_window.geometry("400x300")

# Setting background color to login window
bg_color = "#f0f0f0"
login_window.configure(bg=bg_color)

# Widgets
tk.Label(login_window, text="Welcome to THT - Care", font=("Helvetica", 16), bg=bg_color).pack(pady=10)
tk.Label(login_window, text="Username:", bg=bg_color).pack(pady=5)
username_entry = tk.Entry(login_window)
username_entry.pack(pady=5)

tk.Label(login_window, text="Password:", bg=bg_color).pack(pady=5)
password_entry = tk.Entry(login_window, show="*")  # Show asterisks to hide the password
password_entry.pack(pady=5)

login_button = tk.Button(login_window, text="Login", command=validate_login)
login_button.pack(pady=10)

# Mainloop
login_window.mainloop()
