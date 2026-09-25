import tkinter as tk
from AG_naptar import AGNaptar

def lekerdezes():
    try:
        ev = int(ev_mezo.get())
        honap = int(honap_mezo.get())

        naptar = AGNaptar(ev, honap)

        ev_jo, honap_jo = naptar.AG_ervenyes_adatok()

        if not ev_jo:
            eredmeny.config(text="Hibás év!\nAz év pozitív szám legyen.")
            return

        if not honap_jo:
            eredmeny.config(text="Hibás hónap!\nA hónap 1 és 12 közötti szám legyen.")
            return

        eredmeny.config(
            text=f"Szökőév: {naptar.szokoev()}\n"
                 f"Napok száma: {naptar.napok_szama()}\n"
                 f"Első nap: {naptar.elso_nap()}"
        )

    except ValueError:
        eredmeny.config(text="Hibás adat!\nAz év és a hónap szám legyen.")

root = tk.Tk()
root.title("Naptári információk")
root.geometry("350x300")

app = tk.Frame(root)
app.pack()

tk.Label(app, text="Év:").pack()
ev_mezo = tk.Entry(app)
ev_mezo.pack()

tk.Label(app, text="Hónap:").pack()
honap_mezo = tk.Entry(app)
honap_mezo.pack()

tk.Button(app, text="Lekérdezés", command=lekerdezes).pack(pady=15)

eredmeny = tk.Label(app, text="")
eredmeny.pack()

root.mainloop()