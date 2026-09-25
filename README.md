# Naptári információs program

## Hallgató

Andrási Gábor
S1WGOL

## Feladat leírása

A program egy megadott év, hónap és nap alapján naptári információkat jelenít meg grafikus felületen.

A program megmutatja:
- hogy a megadott év szökőév-e,
- hány napból áll a megadott hónap,
- a hét melyik napjára esik a hónap első napja,
- a hét melyik napjára esik a megadott dátum,
- az adott dátumhoz tartozó névnapot.

A program ellenőrzi a megadott adatokat, és hibás év, hónap vagy nap esetén hibaüzenetet jelenít meg.

## Modulok

### calendar

Bemutatandó modul a naptári adatok meghatározására.

Használt függvények:
- `calendar.isleap()`
- `calendar.monthrange()`
- `calendar.weekday()`

### tkinter és ttk

A program grafikus felületének elkészítésére és az eseménykezelés megvalósítására használt modulok.

Használt elemek:
- `Tk`
- `Frame`
- `Label`
- `Entry`
- `Button`
- `Separator`
- `Style`

A `Lekérdezés` gomb megnyomása meghívja a `lekerdezes()` függvényt.

### AG_naptar

Saját modul, amely a naptári adatok kezelését és ellenőrzését végzi.

Saját függvény:
- `AG_datum_ellenorzes()`

## Osztály

### AGNaptar

Saját osztály.

Az osztály tárolja:
- az évet,
- a hónapot,
- a napot.

Használt metódusok:
- `AG_ervenyes_adatok()`
- `szokoev()`
- `napok_szama()`
- `elso_nap()`
- `datum_napja()`
- `nevnap()`

## Adatfájl

### nevnapok.csv

A program a névnapokat a `nevnapok.csv` fájlból olvassa be.

## Program felépítése

Indítófájl:
- `main.py`

Alapablak:
- `root`

Programfelület:
- `app`