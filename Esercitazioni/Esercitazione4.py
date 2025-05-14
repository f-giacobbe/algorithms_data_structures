from repo_prof.alberi.alberibinari import AlberoBin
from repo_prof.alberi.abr import ABR




#ESERCIZIO 1
#True sse tutti i nodi foglia di a hanno valore uguale a quello della radice
def analizza_foglia(a: AlberoBin) -> bool:
    if a is None:
        return True
    return _analizza(a, a.val)

#Si ferma alla prima foglia diversa dalla radice
def _analizza(a: AlberoBin, val: int) -> bool:
    if a is None:
        return True
    if a.sin is None and a.des is None:
        return a.val == val
    return _analizza(a.sin, val) and _analizza(a.des, val)

#Questi due metodi sopra hanno CTM(n) = theta(1) e CSM(n) = theta(1)     ---   ATTENZIONE! Non bisogna fare supposizioni su n, ma solo sulla struttura dell'albero!
#CTP(n) = theta(n), CSP(n) = theta(n) - nel caso di un albero degenere






#ESERCIZIO 2
#Contare il numero di nodi di a (Albero binario di ricerca) che hanno valore nel range [l, u]
def conta_nodi_range(a: ABR, l: int, u: int) -> int:
    if a is None:
        return 0
    return _conta_nodi_range(a, l, u)

def _conta_nodi_range(a: ABR, l: int, u: int) -> int:
    if a is None:
        return 0
    if a.valori.val > u:
        return _conta_nodi_range(a.valori.sin, l, u)
    if a.valori.val < l:
        return _conta_nodi_range(a.valori.des, l, u)
    return 1 + _conta_nodi_range(a.valori.sin, l, u) + _conta_nodi_range(a.valori.des, l, u)

#CTP(n) = Theta(n) - tutti i nodi hanno valore tra l e u
#CTM(n) = Theta(1) - la radice ha valore inferiore di l oppure maggiore di u
#CSP(n) = Theta(n) - albero degenere con tutti i nodi con valore tra l e u
#CSM(n) = Theta(1)







#ESERCIZIO 3
#Restituire la larghezza di a, ovvero il numero massimo di nodi allo stesso livello
#Abbiamo bisogno di una lista dove l'indice indica il livello dell'albero e il valore un contatore dei nodi su quel livello
def larghezza(a: AlberoBin) -> int:
    if a is None:
        return 0

    l = []
    _larghezza(a, l, 0)
    return max(l)

def _larghezza(a: AlberoBin, l: list[int], liv: int) -> None:
    if a is None:
        return

    if len(l) <= liv:
        l.append(0)     #se non c'è, creo lo slot per il livello i-esimo

    l[liv] += 1
    _larghezza(a.sin, l, liv + 1)
    _larghezza(a.des, l, liv + 1)

#siccome dobbiamo visitare tutto l'albero -> CTP(n) = CTM(n) = Theta(n)
#CSP(n) = Theta(n) - albero degenere
#CSM(n) = Theta(log n) - albero bilanciato









#ESERCIZIO 4
#Restituire True se la somma dei valori dei nodi al livello h è pari alla somma dei nodi al livello k
def livelli_simili(a: AlberoBin, h: int, k: int) -> bool:
    if a is None:
        return False

    somma_livello_h: int = _somma_livello(a, h)
    somma_livello_k: int = _somma_livello(a, k)

    return somma_livello_h == somma_livello_k

def _somma_livello(a: AlberoBin, liv: int) -> int:
    if a is None:
        return 0

    if liv == 0:
        return a.val

    return _somma_livello(a.sin, liv - 1) + _somma_livello(a.des, liv - 1)

#Complessità:
#Temporale -> CTP(n) = Theta(n) - esploriamo tutti i livelli dell'albero 2 volte
#             CTM(n) = Theta(1) - h e k nei primi livelli
#Spaziale -> CSM(n) = Theta(1)
#            CSP(n) = Theta(n) - se h o k sono l'ultimo livello