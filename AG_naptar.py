import calendar

def AG_datum_ellenorzes(ev, honap):
    return ev > 0, 1 <= honap <= 12

class AGNaptar:
    def __init__(self, ev, honap):
        self.ev = ev
        self.honap = honap

    def AG_ervenyes_adatok(self):
        return AG_datum_ellenorzes(self.ev, self.honap)

    def szokoev(self):
        return calendar.isleap(self.ev)

    def napok_szama(self):
        return calendar.monthrange(self.ev, self.honap)[1]

    def elso_nap(self):
        napok = ("hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap")
        nap_index = calendar.weekday(self.ev, self.honap, 1)
        return napok[nap_index]
