# Lezione 1 - Primi concetti
- Problema: una funzione $P:I \to O$
- Algoritmo risolutore del problema P se e solo se $\forall x \in I, P(x)=A(x)$. Tuttavia, i possibili output di A devono includere anche la sua non-terminazione: $A(x) \in O \cup \bot$

## Complessità degli algoritmi
- Complessità peggiore: $T_A^{worst}(n)=max\{T_A(x)|x \in I \wedge |x| = n \}$
- Complessità migliore: $T_A^{best}(n) = min\{T_A(x)|x \in I \wedge |x| = n \}$
- Complessità media: si considera anche la distribuzione di probabilità che si verifichino certi input
```math
T_A^{avg}(n) = \sum_{x \in I \wedge |x| = n}T_A(x) \times Pr(x)
```
- O grande
```math
f(n) = O(g(n)) \quad \text{se } \exists c>0, n_0 \ge 0 : f(n) \le cg(n) \quad \forall n \ge n_0
```
- Omega
```math
f(n) = \Omega (g(n)) \quad \text{se } \exists c>0, n_0\ge0 : f(n)\ge cg(n) \quad \forall n \ge n_0
```
- Theta
```math
f(n) = \Theta (g(n)) \quad \text{se } \exists c_1,c_2>0, n_0\ge0 : c_1 g(n) \le f(n) \le c_2 g(n) \quad \forall n \ge n_0
```

## Complessità dei problemi
- Limite superiore: qual è, nel caso peggiore, la quantità di tempo sufficiente per la risoluzione del problema. È sufficiente conoscere **qualche** algoritmo.
```math
P \text{ ha upper bound } O(f(n)) \Leftrightarrow \exists A \text{ risolutore di } P : T_A^{worst} \in O(f(n))
```
- Limite inferiore (**complessità intrinseca**): qual è, nel caso peggiore, la quantità di tempo sicuramente necessaria per la risoluzione del problema. È necessario dimostrare che **nessun algoritmo** impieghi meno tempo.
```math
P \text{ ha lower bound } \Omega (f(n)) \Leftrightarrow \forall A \text{ risolutore di } P,\  T_A^{worst} \in \Omega (f(n))
```
- Algoritmo ottimale: se dato un problema P avente complessità intrinseca $\Omega (f(n))$, un algoritmo A ha complessità $O(f(n))$ nel caso peggiore





# Lezione 4 - Alberi di ricerca
- Albero binario di ricerca: un albero binario che soddisfa la seguente proprietà:
    - le chiavi nel sottoalbero sx di v sono $\le chiave(v)$
    - le chiavi nel sottoalbero dx di v sono $\ge chiave(v)$
- Fattore di bilanciamento di un nodo v: $\beta = |\text{altezza del sottoalbero sx di v - altezza del sottoalbero dx di v}|$
- Albero bilanciato: se $\forall v \ \beta(v) \le 1$





# Lezione 5 - Tabelle Hash
- Fattore di carico: $\alpha = \frac n m$
- Funzione hash perfetta (iniettiva): se $\forall u,v \in U : u \ne v \implies h(u) \ne h(v) \quad \text{con } |U| \le m$
- Probabilità di una chiave k presente nel dizionario: $P(k)$
- Probabilità che la cella i sia occupata: $Q(i) = \sum_{k : h(k) = i}P(k)$
- Uniformità semplice se $Q(i) = \frac 1 m$, ovvero tutte le celle hanno la stessa probabilità di essere occupate





# Lezioni 9/10 - Grafi
- Insieme di vertici (nodi) $V$
- Insieme di **coppie** di vertici (archi o spigoli) $E$
- Grafo $G = < V, E >$
- Grado di un nodo: il numero di archi incidenti su quel nodo $\delta(v)$
- Distanza tra due nodi: la lunghezza del più corto cammino tra di loro
- Frangia (visita di un grafo): insieme di nodi visti ma non ancora esplorati (per esplorati si intende aver visitato tutti i suoi figli)
- Grafo connesso se $\forall \text{ coppia di nodi } (x,y) \ \exists \text{ un cammino } x \rightarrow y$
- Componente connessa di G: un insieme $C \subseteq N : \forall x, y \in C, x \ne y \ \exists x \rightarrow y$
- Componente connessa **massimale** di G $\Leftrightarrow \nexists C \prime \text{ componente connessa di G } : C \subset C \prime$. Dunque $C$ non è estendibile e le componenti connesse massimali di G sono **partizioni** del grafo.





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
\text{Dove } \sigma \hat=\text{"sequenza di modifiche"},\\ \sum_s \hat=\text{"insieme di tutte le sequenze di modifiche applicabili alla stringa s"}, \\\sigma(s) \hat=\text{"stringa ottenuta applicando le modifiche in }\sigma \text{ a s (in ordine)"}
```