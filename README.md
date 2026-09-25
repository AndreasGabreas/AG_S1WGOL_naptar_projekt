# Naptári információs program

## Hallgató

Andrási Gábor

## Program leírása

A program egy megadott év és hónap alapján naptári információkat jelenít meg grafikus felületen.

A program megmutatja:
- hogy a felhasználó által bevitt év szökőév-e,
- hány napból áll a megadott hónap,
- a hét melyik napjára esik a hónap első napja.

A program ellenőrzi a megadott adatokat, és hibás bevitel esetén hibaüzenetet jelenít meg.

## Modulok

### calendar

A naptári adatok meghatározására használt modul.

Használt függvények:
- `calendar.isleap()`
- `calendar.monthrange()`
- `calendar.weekday()`

### tkinter

A program grafikus felületének elkészítésére használt modul.

Használt elemek:
- `Tk`
- `Label`
- `Entry`
- `Button`

### AG_naptar

Saját modul, amely a program naptári működését tartalmazza.

Saját függvény:
- `AG_datum_ellenorzes()`

## Osztály

- `AGNaptar`

Az osztály tárolja az évet és a hónapot, valamint a naptári adatok lekérdezéséhez szükséges metódusokat.