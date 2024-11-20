from modul_pzk import OsztalyPZK, fuggveny_pzk  # Saját modul importálása
import tkinter as tk  # Tkinter modul a grafikus felülethez
from tkinter import messagebox, Toplevel  # Üzenetek és új ablakok
import os  # Operációs rendszer műveletekhez

def indit_app():
    """A Tkinter grafikus felület indítása."""
    root = tk.Tk()  # A fő Tkinter ablak létrehozása
    root.title("PZK App")  # Az ablak címe

    # Üdvözlő szöveg
    label = tk.Label(root, text="Üdvözöl a PZK fájlkezelő program!", font=("Arial", 14))
    label.pack(pady=10)

    # Fájlnév megadása mező
    fajl_nev_label = tk.Label(root, text="Fájl neve:", font=("Arial", 12))
    fajl_nev_label.pack(pady=5)

    fajl_nev_entry = tk.Entry(root, width=30)  # Szövegmező a fájlnévhez
    fajl_nev_entry.pack(pady=5)

    def fajl_ellenorzes():
        """Ellenőrzi, hogy a fájl létezik-e, és megjeleníti a tartalmát, ha igen."""
        fajl_nev = fajl_nev_entry.get()
        if fuggveny_pzk(fajl_nev):
            kezelo = OsztalyPZK(fajl_nev)
            tartalom = kezelo.olvas_fajl()
            megjelenit_fajl_tartalom(fajl_nev, tartalom)
        else:
            messagebox.showinfo("Fájl Ellenőrzés", f"A(z) '{fajl_nev}' fájl nem létezik.")
            uj_fajl = OsztalyPZK(fajl_nev)
            uj_fajl.ir_fajl("Ez egy automatikusan létrehozott fájl PZK.")
            messagebox.showinfo("Fájl Létrehozás", f"A(z) '{fajl_nev}' fájl létrehozva.")

    def megjelenit_fajl_tartalom(fajl_nev, tartalom):
        """Új ablakban jeleníti meg a fájl tartalmát."""
        uj_ablak = Toplevel(root)
        uj_ablak.title(f"Fájl tartalma: {fajl_nev}")
        szoveg = tk.Text(uj_ablak, wrap=tk.WORD, width=50, height=20)
        szoveg.pack(padx=10, pady=10)
        szoveg.insert(tk.END, tartalom)
        szoveg.config(state=tk.DISABLED)

    def uj_fajl_letrehozasa():
        """Új fájl létrehozása egy külön ablakban."""
        uj_ablak = Toplevel(root)
        uj_ablak.title("Új fájl létrehozása")

        tk.Label(uj_ablak, text="Fájl neve:", font=("Arial", 12)).pack(pady=5)
        fajl_nev_input = tk.Entry(uj_ablak, width=30)
        fajl_nev_input.pack(pady=5)

        tk.Label(uj_ablak, text="Fájl tartalma:", font=("Arial", 12)).pack(pady=5)
        fajl_tartalom_input = tk.Text(uj_ablak, wrap=tk.WORD, width=40, height=10)
        fajl_tartalom_input.pack(padx=10, pady=5)

        def ment_fajl():
            fajl_nev = fajl_nev_input.get()
            fajl_tartalom = fajl_tartalom_input.get("1.0", tk.END).strip()
            if fajl_nev:
                kezelo = OsztalyPZK(fajl_nev)
                eredmeny = kezelo.ir_fajl(fajl_tartalom)
                messagebox.showinfo("Mentés", eredmeny)
                uj_ablak.destroy()
            else:
                messagebox.showerror("Hiba", "A fájl neve nem lehet üres!")

        tk.Button(uj_ablak, text="Mentés", command=ment_fajl).pack(pady=10)
        tk.Button(uj_ablak, text="Mégse", command=uj_ablak.destroy).pack(pady=5)

    def torol_fajlt():
        """Külön ablakban listázza a fájlokat, amelyek közül választhatunk a törléshez."""
        uj_ablak = Toplevel(root)
        uj_ablak.title("Fájl törlése")

        tk.Label(uj_ablak, text="Válaszd ki a törlendő fájlt:", font=("Arial", 12)).pack(pady=5)

        fajlok = [f for f in os.listdir() if os.path.isfile(f)]
        lista = tk.Listbox(uj_ablak, width=50, height=10)
        lista.pack(padx=10, pady=5)

        for fajl in fajlok:
            lista.insert(tk.END, fajl)

        def torles():
            kivalasztott_fajl = lista.get(tk.ACTIVE)
            if kivalasztott_fajl:
                try:
                    os.remove(kivalasztott_fajl)
                    messagebox.showinfo("Törlés", f"A(z) '{kivalasztott_fajl}' fájl törölve.")
                    lista.delete(tk.ACTIVE)
                except Exception as e:
                    messagebox.showerror("Hiba", f"Nem sikerült törölni a fájlt: {e}")
            else:
                messagebox.showerror("Hiba", "Nincs kiválasztott fájl!")

        tk.Button(uj_ablak, text="Törlés", command=torles).pack(pady=10)
        tk.Button(uj_ablak, text="Mégse", command=uj_ablak.destroy).pack(pady=5)

    # Gombok az alapfunkciókhoz
    tk.Button(root, text="Ellenőrzés", command=fajl_ellenorzes).pack(pady=10)
    tk.Button(root, text="Új fájl létrehozása", command=uj_fajl_letrehozasa).pack(pady=10)
    tk.Button(root, text="Fájl törlése", command=torol_fajlt).pack(pady=10)
    tk.Button(root, text="Kilépés", command=root.destroy).pack(pady=10)

    root.mainloop()

def main():
    """A program belépési pontja."""
    print("Üdvözöl a PZK fájlkezelő program!")  # Konzolos üzenet
    indit_app()  # A GUI indítása

if __name__ == "__main__":
    main()  # A program indítása
