import tkinter as tk
from tkinter import ttk
from AG_naptar import AGNaptar

def lekerdezes():
    try:
        ev = int(ev_mezo.get())
        honap = int(honap_mezo.get())
        nap = int(nap_mezo.get())

        naptar = AGNaptar(ev, honap, nap)

        ev_jo, honap_jo, nap_jo = naptar.AG_ervenyes_adatok()

        if not ev_jo:
            eredmeny.config(text="Hibás év!\nAz év pozitív szám legyen.")
            return

        if not honap_jo:
            eredmeny.config(text="Hibás hónap!\nA hónap 1 és 12 közötti szám legyen.")
            return

        if not nap_jo:
            eredmeny.config(text="Hibás nap!\nA megadott hónapban nincs ilyen nap.")
            return

        eredmeny.config(
            text=f"Szökőév: {naptar.szokoev()}\n"
                 f"Napok száma: {naptar.napok_szama()}\n"
                 f"Hónap első napja: {naptar.elso_nap()}\n"
                 f"A megadott dátum napja: {naptar.datum_napja()}"
        )

    except ValueError:
        eredmeny.config(text="Hibás adat!\nAz év és a hónap szám legyen.")

root = tk.Tk()
root.title("Naptári információk")
root.geometry("420x460")
root.resizable(False, False)

app = ttk.Frame(root, padding=25)
app.pack(fill="both", expand=True)

style = ttk.Style()
style.configure("Cim.TLabel", font=("Segoe UI", 16, "bold"))
style.configure("Eredmeny.TLabel", font=("Segoe UI", 10))

cim = ttk.Label(app, text="Naptári információk", style="Cim.TLabel")
cim.grid(row=0, column=0, columnspan=2, pady=(0, 25))

ttk.Label(app, text="Év:").grid(row=1, column=0, sticky="w", padx=(0, 15), pady=8)
ev_mezo = ttk.Entry(app, width=20)
ev_mezo.grid(row=1, column=1, pady=8)

ttk.Label(app, text="Hónap:").grid(row=2, column=0, sticky="w", padx=(0, 15), pady=8)
honap_mezo = ttk.Entry(app, width=20)
honap_mezo.grid(row=2, column=1, pady=8)

ttk.Label(app, text="Nap:").grid(row=3, column=0, sticky="w", padx=(0, 15), pady=8)
nap_mezo = ttk.Entry(app, width=20)
nap_mezo.grid(row=3, column=1, pady=8)

lekerdezes_gomb = ttk.Button(app, text="Lekérdezés", command=lekerdezes)
lekerdezes_gomb.grid(row=4, column=0, columnspan=2, pady=20)

ttk.Separator(app, orient="horizontal").grid(
    row=5, column=0, columnspan=2, sticky="ew", pady=10
)

eredmeny = ttk.Label(app, text="", style="Eredmeny.TLabel", justify="left")
eredmeny.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()