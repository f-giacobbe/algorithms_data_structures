# Lezioni 11/13 - Grafi pesati
- Grafo pesato: $G = < N, E, \lambda >$, dove $\lambda$ è una funzione di costo che prende come chiave $(x,y)$ e restituisce il peso dell\primearco corrispondente
- Costo di un cammino: $costo(c) = \sum_{i=0}^{k-1}\lambda((x_i,x_{i+1}))$
- Distanza: $dist(x,y) = min\{costo(c):\text{c è un cammino da x a y}\}$
- Cammino di costo minimo: $c : costo(c) = dist(c)$
- Albero ricoprente di un grafo G: $A = < N, E\prime, \lambda_{E\prime} >$
- Costo di un albero ricoprente: $\sum_{e \in E\prime} \lambda_{E\prime}(e)$
- Albero minimo ricoprente: $A : \text{A è un albero ricoprente di G}\ \wedge\ \nexists\ A\prime\text{ albero ricoprente di G} : costo(A\prime) < costo(A)$
- Taglio: un sottoinsieme di archi del grafo. $T(N_i) = \{\ (x,y) \in E : x \in N_i \ \wedge \ y \in \bar{N_i} \ \}$, dove $\bar{N_i} = N - N_i$

# Lezione 14 - Programmazione dinamica
## Edit Distance
- Modifica elementare: inserimento, rimozione o sostituzione di un carattere
- Distanza tra due stringhe $\delta(x,y)$: il numero minimo di modifiche elementari necessarie per          modificare una stringa in un'altra
```math
dist(x,y)\  \hat= \ min\{ \ |\sigma| : \sigma \in \sum_{s1} \wedge \ \sigma(s1) = s2 \}.\\
\text{Dove } \sigma \hat=\text{"sequenza di modifiche"},\\ \sum_s \hat=\text{"insieme di tutte le sequenze di modifiche applicabili alla stringa s"}, \\\sigma(s) \hat=\text{"stringa ottenuta applicando le modifiche in $\sigma$ a s (in ordine)"}
```