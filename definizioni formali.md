# Lezioni 11/13 - Grafi pesati
- Grafo pesato: $G = < N, E, \lambda >$, dove $\lambda$ è una funzione di costo che prende come chiave $(x,y)$ e restituisce il peso dell\primearco corrispondente
- Costo di un cammino: $costo(c) = \sum_{i=0}^{k-1}\lambda((x_i,x_{i+1}))$
- Distanza: $dist(x,y) = min\{costo(c):\text{c è un cammino da x a y}\}$
- Cammino di costo minimo: $c : costo(c) = dist(c)$
- Albero ricoprente di un grafo G: $A = < N, E\prime, \lambda_{E\prime} >$
- Costo di un albero ricoprente: $\sum_{e \in E\prime} \lambda_{E\prime}(e)$
- Albero minimo ricoprente: $A : \text{A è un albero ricoprente di G}\ \wedge\ \nexists\ A\prime\text{ albero ricoprente di G} : costo(A\prime) < costo(A)$
- Taglio: un sottoinsieme di archi del grafo. $T(N_i) = \{\ (x,y) \in E : x \in N_i \ \wedge \ y \in \bar{N_i} \ \}$, dove $\bar{N_i} = N - N_i$