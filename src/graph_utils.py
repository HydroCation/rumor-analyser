import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

def generate_random_graph(n: int = 50, p: float = 0.1, seed: int = None) -> nx.Graph: #n = nodes, p = probability of edge between any two nodes
    return nx.erdos_renyi_graph(n=n, p=p, seed=seed)

def generate_barabasi_albert_graph(n: int = 50, m: int = 2, seed=None) -> nx.Graph:
    if m >= n:
        raise ValueError(f"Constraint violated: m ({m}) must be strictly less than n ({n}).")
    if m < 1:
        raise ValueError(f"Constraint violated: m ({m}) must be at least 1.")
    return nx.barabasi_albert_graph(n=n, m=m, seed=seed)


def visualize_graph(
        graph: nx.Graph,
        status: dict = None,
        pos: dict = None,
        title: str = None,
        color_palette: str = "classic",
        ax: plt.Axes = None
):
    """Visualizes graphs"""

    palettes = {
        "classic": {"S": "yellow", "I": "red", "R": "green"},
        "modern": {"S": "#3498db", "I": "#e74c3c", "R": "#2ecc71"}
    }

    selected_palette = palettes.get(color_palette, palettes["classic"])

    if pos is None:
        pos = nx.spring_layout(graph, seed = 42)

    node_colors = []
    for node in graph.nodes():
        state = status[node] if status and node in status else "S"
        node_colors.append(selected_palette.get(state, "yellow"))
        
    created_fig = False
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
        created_fig = True
        
    nx.draw(
        graph, 
        pos=pos, 
        node_color=node_colors, 
        with_labels=True, 
        edge_color="#bdc3c7",
        node_size=350,
        font_size=8,
        ax=ax
    )
    
    if title:
        ax.set_title(title, fontsize=12, fontweight="bold")
        
    if created_fig:
        plt.show()


def plot_degree_distribution(graph: nx.Graph, title: str = "Degree Distribution"):
    """
    Plots the degree distribution histogram to visually verify scale-free vs random topologies.
    """
    degrees = [d for _, d in graph.degree()]
    
    plt.figure(figsize=(7, 4))
    plt.hist(degrees, bins=range(min(degrees), max(degrees) + 2), align="left", color="#3498db", rwidth=0.8)
    plt.title(title, fontsize=12, fontweight="bold")
    plt.xlabel("Degree (k)")
    plt.ylabel("Count")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


def calculate_centralities(graph: nx.Graph) -> dict:
    """
    Calculate Degree, Betweenness, Closeness for all nodes.
    """
    return{
        "degree": dict(graph.degree()),
        "betweenness": nx.betweenness_centrality(graph),
        "closeness": nx.closeness_centrality(graph),
    }


def get_centrality_seeds(
        graph: nx.Graph,
        metric: str = "degree",
        top_k: int = 1,
        seed: int = None
) -> list:
    """IDs top-k seed nodes based on centrality metrics"""
    metric = metric.lower()
    if metric == "random":
        rng = random.Random(seed)
        return rng.sample(list(graph.nodes()), min(top_k, len(graph)))

    centrality_map = {
        "degree": lambda: dict(graph.degree()),
        "betweenness": lambda: nx.betweenness_centrality(graph),
        "closeness": lambda: nx.closeness_centrality(graph),
    }

    if metric not in centrality_map:
        raise ValueError(f"Unknown metric: '{metric}'. Choose from 'degree', 'betweenness', 'closeness', or 'random'.")
    scores = centrality_map[metric]()
    sorted_nodes = sorted(scores.items(), key = lambda item: item[1], reverse = True)
    return [node for node, _ in sorted_nodes[:top_k]]


def get_network_summary(graph: nx.Graph) -> dict:
    """Summary Computation"""
    degrees = [d for _, d in graph.degree()]
    return{
        "nodes": graph.number_of_nodes(),
        "edges": graph.number_of_edges(),
        "density": nx.density(graph),
        "avg_degree": float(np.mean(degrees)),
        "max_degree": int(np.max(degrees)),
        "is_connected": nx.is_connected(graph),
    }