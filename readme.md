### Requests API telepítése
--------------------------

A program futtatásához szükséges a Python 3.10 és a requests API.
Az előző Linuxon alapból telepítve van, Windowson, ha letöltjük a Visual Studio Code alkalmazást, akkor ott telepíthetjük a Python 3.10 fordítót.

Ha van python a gépünkön, de nincs requests API, írjuk be az alábbi parancsot:

```bash
python -m pip install requests
```

![Konzolos letöltés](./media/requestletoltes.png)

### Program használata
-------------------

Lépések:
1. Nyissuk meg a bemenet.txt fájlt
2. Első sorba írjuk be a youtube videó linkjét, majd hagyjunk ki egy sort
3. Második sortól írjuk be, hogy melyik *perc*:*másodperc* pontnál kezdődik egy adott fejezet

> Egy fejezet megadása kétféleképpen lehetséges: 1.: Csak az időt írjuk be *perc*:*másodperc* formátumban. 2.: Megadjuk először az időt, majd a írunk egy szóközt, majd egy "-" kötőjelet, majd megint egy szóközt, és a fejezet nevét megadjuk. Példa: "22:47 - Telepités utáni lépések". A percek és a másodpercek számának nem kell két jegyűnek lenni, de legalább egy jegyűnek igen (akkor is, ha 0, pl.: 0:4). Minden sorban csak egy ilyen metaadat szerepelhet. A fileban csak a 2. sor lehet üres.

4. Indítsuk el a timestamp.py fájlt.