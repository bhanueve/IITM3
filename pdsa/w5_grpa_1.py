#dm is distance_map
def FiberLink(dm):
    out_dist = 0
    infinity = 1 + max([d for u in dm.keys() for (v,d) in dm[u]])
    (visited, distance, TreeEdges) = ({}, {}, [])
    for v in dm.keys():
        (visited[v], distance[v]) = (False, infinity)
    visited[0] = True
    for (v,d) in dm[0]:
        distance[v] = d
    for i in dm.keys():
        (mindist, nextv) = (infinity, None)
        for u in dm.keys():
            for (v,d) in dm[u]:
                if visited[u] and (not visited[v]) and d < mindist:
                    (mindist, nextv, nexte) = (d, v, (u,v))
        if nextv is None:
            break
        visited[nextv] = True
        TreeEdges.append(nexte)
        out_dist += mindist
        for (v,d) in dm[nextv]:
            if not visited[v]:
                distance[v] = min(distance[v], d)
    return out_dist