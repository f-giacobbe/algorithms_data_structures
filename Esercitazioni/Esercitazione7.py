from repo_prof.grafi.grafi import *
from repo_prof.grafi.grafipesati import *
from repo_prof.grafi.algosugrafipesati import *

#ESERCIZIO 1
#popular(g) restituisce l'utente che ha il maggior numero di "amici" e "amici di amici", ovvero rispettivamente
#i nodi a distanza 1 e a distanza 2
def popolarita_nodo(g: Grafo, i):
    visited = {i: True}
    count = 0
    adiacenti = g.adiacenti(i)
    for (j, _) in adiacenti:
        if j not in visited:
            visited[j] = True
            count += 1

        amici2grado = g.adiacenti(j)
        for (h, _) in amici2grado:
            if h not in visited:
                visited[h] = True
                count += 1

    return count

#CTP = Theta(m) (tutti gli archi) e Theta(n^2) se il nodo i ha n-1 vicini, che a sua volta hanno n-1 vicini
#CSP = Theta(n)
#CTM = Theta(1) se il nodo i-esimo ha un numero molto piccolo di vicini
#CSM = Theta(1)

def popular(g: Grafo):
    v_max = -1
    nodo_max = -1

    nodes = g.n
    for i in range(nodes):
        pi = popolarita_nodo(g, i)

        if pi > v_max:
            v_max = pi
            nodo_max = i

    return nodo_max

#CTP = Theta(n*m) = Theta(n^3) - faccio partire popolarità_nodo n volte
#CSP = Theta(n)
#CTM = Theta(n)
#CSM = Theta(1)











#ESERCIZIO 2
#raggiungibile(g, x1, x2, x3) - g orientato, x1, x2, x3 tre nodi del grafo. Restituisce True se x3 è raggiungibile
#da x1 e da x2

#soluzione mia
def raggiungibile(g: Grafo, x1, x2, x3):
    return _cammino(g, x1, x3) and _cammino(g, x2, x3)

def _cammino(g: Grafo, x, y) -> bool:
    adiacenti_x = g.adiacenti(x)

    if y in adiacenti_x:
        return True

    for u in adiacenti_x:
        if _cammino(g, u, y):
            return True

    return False

#soluzione proposta
def raggiungibile2(g: Grafo, x1, x2, x3):
    vis_x1 = breadth_visit(g, x1)   #restituisce un dizionario
    vis_x2 = breadth_visit(g, x2)

    return vis_x1[x3] != -1 and vis_x2 != -1

def breadth_visit(g: Grafo, s):
    queue = [s]
    pred = {k : -1 for k in range(g.n)}

    while len(queue) > 0:
        v = queue.pop(0)
        adiacenti = g.adiacenti(v)
        for (u, _) in adiacenti:
            if pred[u] == -1:
                pred[u] = v
                queue.append(u)

    return pred

#CT = O(n + m) (Lista di adiacenza)
#CS = Theta(n)











#ESERCIZIO 3
#calcolare il diametro di un grafo, definito come la lunghezza del cammino minimo tra i due nodi più distanti in termini di archi attraversati
def diametro(g: GrafoP) -> int:
    if g is None:
        return 0

    nodi = g.n
    max_val = 0

    for i in range(nodi):
        dist = Dijkstra(g, i)   #Dijkstra costruisce un SPT
        curr = max(p for (_, _, p) in dist)

        if curr > max_val:
            max_val = curr

    return max_val

#Complessità = n volte dijkstra











#ESERCIZIO 4
#g non orientato, k lista di nodi "ancora". Dato un punto ancora la distanza tra due nodi x, y viene calcolata come
#appr(x, y) = somma delle distanze tra x e i nodi ancora + somma delle distanze tra y e i nodi ancora, tutto diviso il numero di nodi ancora
#Dovrò restituire per ogni coppia (x, y) la loro distanza
def distanza(g: GrafoP, k: list[int]):
    nodi = g.n
    somma = {v : 0.0 for v in range(nodi)}

    for e in k:
        d_k = Dijkstra(g, e)

        for v in range(nodi):
            somma[v] += d_k[2]  #il terzo elemento della tupla restituita da Dijkstra è il peso, che vado quindi a sommare

    m = float(len(k))   #il numero di nodi ancora
    appr = {}
    for x in range(nodi):
        for y in range(nodi):
            if x < y:
                appr[(x, y)] = (somma[x] + somma[y])/m

    return appr

#Complessità = len(k) volte dijkstra