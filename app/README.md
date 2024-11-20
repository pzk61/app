## Hallgató:Pomozi Zoltán Krisztián
**Monogram**: PZK  
**Tantárgy**: Szkript nyelvek 
**Feladat célja**: Egy fájlkezelő alkalmazás, amely képes fájlokat ellenőrizni, létrehozni, olvasni, törölni, és a tartalmukat megjeleníteni grafikus felületen keresztül.

---

## Feladat Leírása
Ez a program egy egyszerű fájlkezelő alkalmazás, amely grafikus felületen (Tkinter) biztosít különböző fájlkezelési funkciókat:
- Fájl létezésének ellenőrzése.
- Fájl tartalmának megjelenítése.
- Új fájl létrehozása és tartalom írása bele.
- Létező fájlok törlése, kiválasztással.

---

## Program Felépítése

- **Indítás**: A program a `main.py` fájlból indítható.
- **Alapablak**: A Tkinter alapú `root` ablak biztosítja a grafikus felületet.
- **Programnév**: Az alkalmazás neve "PZK App".

---

## Modulok és Osztályok

### Modul: `modul_pzk.py`
Ez a modul tartalmazza a programhoz szükséges funkciókat és osztályokat.

- **Osztály**: `OsztalyPZK`
  - Feladata a fájlok olvasása és írása.
  - Metódusok:
    - `olvas_fajl`: A fájl tartalmának visszaadása.
    - `ir_fajl`: Tartalom írása a fájlba.
- **Függvény**: `fuggveny_pzk`
  - Ellenőrzi, hogy egy adott fájl létezik-e.

### Főmodul: `main.py`
A főmodul biztosítja a program indítását és a felhasználói interakciókat a Tkinter grafikus felület segítségével. A főbb funkciók:
- Fájlok ellenőrzése.
- Fájlok létrehozása.
- Fájlok tartalmának megjelenítése.
- Fájlok törlése.