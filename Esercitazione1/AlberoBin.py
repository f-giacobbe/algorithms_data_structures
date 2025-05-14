from repo_prof.alberi.alberibinari import AlberoBin

#True sse tutti i nodi foglia di a hanno valore uguale a quello della radice
def analizza_foglia(a: AlberoBin) -> bool:
    if a is None:
        return True
    return analizza(a, a.val)

#Si ferma alla prima foglia diversa dalla radice
def analizza(a: AlberoBin, val: int) -> bool:
    if a is None:
        return True
    if a.sin is None and a.des is None:
        return a.val == val
    return analizza(a.sin, val) and analizza(a.des, val)

#Questi due metodi sopra hanno CTM(n) = theta(1) e CSM(n) = theta(1)     ---   ATTENZIONE! Non bisogna fare supposizioni su n, ma solo sulla struttura dell'albero!
#CTP(n) = theta(n), CSP(n) = theta(n) - nel caso di un albero degenere