from AG_naptar import AGNaptar

naptar = AGNaptar(2026, 9)

print("Év:", naptar.ev)
print("Hónap:", naptar.honap)
print("Érvényes hónap:", naptar.AG_ervenyes_honap())
print("Szökőév:", naptar.szokoev())
print("Napok száma:", naptar.napok_szama())
print("Első nap:", naptar.elso_nap())