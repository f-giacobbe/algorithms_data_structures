from repo_prof.grafi.grafipesati import GrafoP
from repo_prof.grafi.algosugrafipesati import *
from repo_prof.grafi.grafinopesati import *
import math



#ESERCIZIO 1
#Dato un grafo orientato e pesato
#Per ogni blocco B restituire gli identificativi delle tre piscine P più vicine. Si suppone di avere un metodo
#G.getType(i: nodo)
def best3piscine(g: GrafoP):
    #fatto con floyd, ma fattibile anche con Dijkstra - la complessità nel caso peggiore è uguale (n^3)
    c = floyd(g)
    best3p = []

    for i in range(g.n):
        if g.getType(i) == "B":     #il nodo i-esimo è un blocco
            m = [math.inf, math.inf, math.inf]  #le 3 minime distanze
            k = [-1, -1, -1]    #i 3 identificativi

            for j in range(g.n):
                dist = c[i][j]
                if g.getType(j) == "P":     #il nodo j-esimo è una piscina
                    if m[0] > dist:     #m[0] è il minimo corrente, che adesso sarà il secondo minimo
                        m[2], m[1], m[0] = m[1], m[0], dist
                        k[2], k[1], k[0] = k[1], k[0], j
                    elif m[1] > dist:
                        m[2], m[1] = m[1], dist
                        k[2], k[1] = k[1], j
                    elif m[2] > dist:
                        m[2] = dist
                        k[2] = j

            best3p.append((i, k))

    return best3p









#ESERCIZIO 2
#Dato un grafo non orientato, connesso, e pesato
#Nodo -> Sensore
#Peso arco -> penalità di comunicazione
#Si vuole ottenere un sottoinsieme di connessioni tra i sensori con le seguenti condizioni:
#1) Ogni sensore deve poter comunicare con tutti gli altri, direttamente o indirettamente (attraverso più sensori)
#2) Le connessioni devono essere sufficienti per garantire la condizione 1
#3) Il costo totale delle connessioni deve essere il più basso possibile
#4) Individuare la connessione con penalità massima ed eliminarla
def connessioni(g: GrafoNOP):
    min_albero_ricoprente = prim(g)

    #rimuovere l'arco col peso massimo
    i_max = -1
    penalita_max = -1
    for i in range(g.n):
        penalita_curr = min_albero_ricoprente[i][2]
        if penalita_curr > penalita_max:
            i_max = i
            penalita_max = penalita_curr

    del min_albero_ricoprente[i_max]

    return min_albero_ricoprente