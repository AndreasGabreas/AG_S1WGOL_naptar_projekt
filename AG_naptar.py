import calendar

def AG_datum_ellenorzes(ev, honap, nap):
    ev_jo = ev > 0
    honap_jo = 1 <= honap <= 12

    if not ev_jo or not honap_jo:
        return ev_jo, honap_jo, False

    napok_szama = calendar.monthrange(ev, honap)[1]
    nap_jo = 1 <= nap <= napok_szama

    return ev_jo, honap_jo, nap_jo

class AGNaptar:
    def __init__(self, ev, honap, nap):
        self.ev = ev
        self.honap = honap
        self.nap = nap

    def AG_ervenyes_adatok(self):
        return AG_datum_ellenorzes(self.ev, self.honap, self.nap)

    def szokoev(self):
        return calendar.isleap(self.ev)

    def napok_szama(self):
        return calendar.monthrange(self.ev, self.honap)[1]

    def elso_nap(self):
        napok = ("hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap")
        nap_index = calendar.weekday(self.ev, self.honap, 1)
        return napok[nap_index]

    def datum_napja(self):
        napok = ("hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap")
        nap_index = calendar.weekday(self.ev, self.honap, self.nap)
        return napok[nap_index]