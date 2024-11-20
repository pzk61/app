import os  # Az operációs rendszer műveletekhez, például fájl létezésének ellenőrzéséhez

class OsztalyPZK:
    """Fájlkezelő osztály."""

    def __init__(self, file_path):
        """Az osztály inicializálása."""
        self.file_path = file_path

    def olvas_fajl(self):
        """A fájl tartalmának olvasása."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return "A fájl nem található."
        except Exception as e:
            return f"Hiba történt: {e}"

    def ir_fajl(self, tartalom):
        """Tartalom írása a fájlba."""
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                f.write(tartalom)
                return "Sikeres fájlírás!"
        except Exception as e:
            return f"Hiba történt: {e}"

def fuggveny_pzk(fajl_nev):
    """Ellenőrzi, hogy a megadott fájl létezik-e."""
    return os.path.exists(fajl_nev)