import networkx as nx
import matplotlib.pyplot as plt

def generate_random_graph(n = 50, p = 0.1): #n = nodes, p = probability of edge between any two nodes
    return nx.erdos_renyi_graph(n=n, p=p)

def visualize_graph(graph, status = None, pos = None): #status = dict mapping each node to S I or T
    color_map = {
        "S":"yellow",
        "I": "red",
        "R": "green"
    }
    node_colors = []
    for node in graph.nodes():
        state = status[node] if status and node in status else "S" #If status is given and node in status, use that else assume node is susceptible
        node_colors.append(color_map[state])
    nx.draw(graph, pos = pos, node_color = node_colors, with_labels = True)
    plt.show()
