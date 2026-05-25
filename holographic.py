import numpy as np
import networkx as nx

def holographic_score(returns):
    """
    Compute per‑ETF geodesic distance to the graph center.
    Steps:
      1. Correlation matrix → distance matrix (1 - |corr|)
      2. Build complete graph with distances as weights.
      3. Find the node that minimizes average distance to all others (graph center).
      4. For each node, compute shortest path distance to that center.
    Returns dict: ticker -> distance (higher = more "entangled").
    """
    returns_clean = returns.dropna()
    n = returns_clean.shape[1]
    if n < 2:
        return {t: 0.0 for t in returns_clean.columns}
    corr = returns_clean.corr().values
    # distance = 1 - |correlation|
    dist_mat = 1 - np.abs(corr)
    np.fill_diagonal(dist_mat, 0)
    # Build graph
    G = nx.Graph()
    nodes = returns_clean.columns.tolist()
    G.add_nodes_from(nodes)
    for i, u in enumerate(nodes):
        for j, v in enumerate(nodes):
            if i >= j:
                continue
            w = dist_mat[i, j]
            G.add_edge(u, v, weight=w)
    # Find graph center (node with smallest eccentricity or average distance)
    # Use closeness centrality: center = node with highest closeness (smallest average distance)
    closeness = nx.closeness_centrality(G, distance='weight')
    center = max(closeness, key=closeness.get)
    # Compute shortest path distances from center to all nodes
    lengths = nx.single_source_dijkstra_path_length(G, center, weight='weight')
    # Fill missing (should be all present) with large number
    scores = {node: lengths.get(node, 1e6) for node in nodes}
    return scores
