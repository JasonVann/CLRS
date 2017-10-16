def mst_prim(G, w, r):
    for u in G.V:
        u.key = float('inf')
        u.p = None
    r.key = 0
    Q = G.V
    while len(Q) != 0:
        u = extract_min(Q)
        for i in range(n):
            if G.matrix[u][i] == 1 and i in Q and w(u, i) < v.key:
                i.p = u
                i.key = w(u, i)
