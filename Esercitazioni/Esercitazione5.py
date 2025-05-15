from repo_prof.alberi.alberibinari import AlberoBin

#ESERCIZIO 1
#Restituire True se esiste almeno un nodo in a ad un livello liv tale che compare anche in b a un livello > liv
def verifica(a: AlberoBin, b: AlberoBin) -> bool:
    if a is None or b is None:
        return False

    return _verifica(a, b, 0)

def _verifica(a: AlberoBin, b: AlberoBin, liv_a: int) -> bool:
    if a is None:
        return False

    if _esiste(a.val, b, liv_a, 0):
        return True

    return _verifica(a.sin, b, liv_a + 1) or _verifica(a.des, b, liv_a + 1)

#Restituisce True se esiste x in b ad un livello > liv_a
def _esiste(x: int, b: AlberoBin, liv_a: int, liv_b: int) -> bool:
    if b is None:
        return False

    if b.val == x and liv_b > liv_a:
        return True

    return _esiste(x, b.sin, liv_a, liv_b + 1) or _esiste(x, b.des, liv_a, liv_b + 1)

#CTM(n, m) = CSM(n, m) = Theta(1) - il valore del figlio sinistro di b è uguale al valore della radice di a
#CTP(n, m) = Theta(n * m)
#CSP(n, m) = Theta(n + m)









#ESERCIZIO 2
#Restituire il numero totale di occorrenze di valori che compaiono almeno due volte in a
def conta_ripetuti(a: AlberoBin) -> int:
    if a is None:
        return 0

    return _conta_ripetuti(a, [], [], 0)

def _conta_ripetuti(a: AlberoBin, visti: list[int], ripetuti: list[int], occorrenze: int) -> int:
    if a is None:
        return occorrenze

    if a.val in ripetuti:
        return _conta_ripetuti(a.sin, visti, ripetuti, occorrenze + 1) + _conta_ripetuti(a.des, visti, ripetuti, occorrenze + 1)

    if a.val in visti:
        ripetuti.append(a.val)
        return _conta_ripetuti(a.sin, visti, ripetuti, occorrenze + 2) + _conta_ripetuti(a.des, visti, ripetuti, occorrenze + 2)
    else:
        visti.append(a.val)
        return _conta_ripetuti(a.sin, visti, ripetuti, occorrenze) + _conta_ripetuti(a.des, visti, ripetuti, occorrenze)