class AlberoBin:
    def __init__(self, val, sin = None, des = None):
        self.val = val
        self.sin = sin
        self.des = des



#ESERCIZIO 1
#Funzione che restituisce True se l'info di tutte le foglie è < k
def analizza_foglia(a: AlberoBin, k: int) -> bool:
    if a is None:
        return True

    if a.sin is None and a.des is None:     #sono in una foglia
        return a.val < k

    return analizza_foglia(a.sin, k) and analizza_foglia(a.des, k)

#Complessità - ATTENZIONE! Non dobbiamo fare assunzioni sul numero di nodi ma solo su come si presenta l'albero e sui valori che può contenere
#CTP = Theta(n) - caso in cui ogni foglia è < k -> eseguo l'algoritmo per tutti i nodi
#CSP = Theta(n) - Dipende dal numero di chiamate attive; il caso peggiore è l'albero degenere
#CTM = Theta(1) - Raggiungo la prima foglia in pochi passi e scopro che è >= k
#CSM = Theta(1) - per lo stesso motivo del CTM








#ESERCIZIO 2
#Costo massimo del cammino da radice a foglia. Per costo massimo si intende la somma dei valori che si incontrano (per ipotesi positivi)
def costo_massimo(a: AlberoBin) -> int:
    if a is None:
        return 0

    if a.sin is None and a.des is None:
        return a.val

    return a.val + max(costo_massimo(a.sin), costo_massimo(a.des))

#CTM = CTP = Theta(n) - in quanto dobbiamo sempre vedere tutti i cammini
#CSP = Theta(n) nel caso di un albero degenere
#CSM = Theta(log n) nel caso di un albero bilanciato







#ESERCIZIO 3
#Restituire True se esiste un nodo n in a tale che x appare sia nel sottoalbero sinistro di n che nel sottoalbero destro
def verifica(a: AlberoBin, x: int) -> bool:
    if a is None:
        return False

    return (presente(a.sin, x) and presente(a.des, x)) or verifica(a.sin, x) or verifica(a.des, x)

def presente(a: AlberoBin, x: int) -> bool:
    if a is None:
        return False

    return a.val == x or presente(a.sin, x) or presente(a.des, x)
#CTM = Theta(1)
#CTP = Theta(n^2) - perché n volte chiamo verifica da Theta(n) e per ciascuna chiamo due volte verifica da Theta(n)
#CSM = Theta(1)
#CSP = Theta(n)