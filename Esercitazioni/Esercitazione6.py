from repo_prof.alberi.alberibinari import AlberoBin

#ESERCIZIO 1
#Restituire True se tutti i nodi foglia di a contengono un valore che non appare in nessun altro nodo
#(sia nodi foglia che non) - da provare a fare senza ausilio di dizionari e simili
def verifica_unicita(a: AlberoBin) -> bool:
    return unicita(a, a)

def unicita(a: AlberoBin, radice: AlberoBin) -> bool:
    if a is None:
        return True

    if a.sin is None and a.des is None: #sono in un nodo foglia -> devo verificare se il suo valore non appare da nessun altra parte
        return conta(a.val, radice, 0)

    return unicita(a.sin, radice) and unicita(a.des, radice)

def conta(x: int, a: AlberoBin, count: int) -> bool:
    if a is None:
        return True

    if a.val == x:
        count += 1

    if count > 1:
        return False

    return conta(x, a.sin, count) and conta(x, a.des, count)

#CTP(n) = Theta(n^2) - In un albero completo e bilanciato tutte le foglie (n/2) rispettano la condizione, quindi non mi fermo mai prima e conta è eseguito n volte -> n * n/2
#CSP(n) = Theta(n) - In un albero degenere
#CTM(n) = Theta(1) - Se trovo subito una foglia che non rispetta la condizione
#CSM(n) = Theta(1) - per lo stesso motivo






#ESERCIZIO 2
#Restituire True se la foglia che si trova alla minore profondità è in un livello < liv
def poco_profondo(a: AlberoBin, liv: int) -> bool:
    if a is None or liv <= 0:
        return False

    if a.sin is None and a.des is None:
        return True     #liv, arrivati a questo punto, è maggiore di 0

    return poco_profondo(a.sin, liv - 1) or poco_profondo(a.des, liv - 1)

#CTM(n) = Theta(1) - Trovo subito una foglia che si trova a livello < liv
#CSM(n) = Theta(1)
#CTP(n) = Theta(n) - la foglia è l'ultima sulla destra -> faccio n chiamate
#CSP(n) = Theta(n) - Albero degenere e liv > n (non mi fermo mai, scorro tutto l'albero)