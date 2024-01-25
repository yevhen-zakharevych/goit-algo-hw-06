import networkx as nx
import matplotlib.pyplot as plt

from dijkstra import dijkstra


def main():
    graph = nx.Graph()
    color_map = [
        'green', 'green', 'green', 'green', 'green',
        'red', 'red', 'red', 'red',
        'blue', 'blue', 'blue', 'blue'
    ]

    graph.add_nodes_from(["G1", "G2", "G3", "G4", "G5", "R1", "R2", "R3", "R4", "B1", "B2", "B3", "B4"])

    graph.add_edge("G1", "G2", weight=3)
    graph.add_edge("G2", "G3", weight=6)
    graph.add_edge("G3", "G4", weight=4)
    graph.add_edge("G3", "G5", weight=8)

    graph.add_edge("R1", "R2", weight=3)
    graph.add_edge("R2", "R3", weight=6)
    graph.add_edge("R3", "R4", weight=7)

    graph.add_edge("B1", "B2", weight=9)
    graph.add_edge("B2", "B3", weight=11)
    graph.add_edge("B3", "B4", weight=3)

    graph.add_edge("G2", "R2", weight=3)
    graph.add_edge("R2", "B1", weight=5)
    graph.add_edge("G2", "B2", weight=7)

    graph_dict = nx.to_dict_of_dicts(graph)

    # map weight values
    for key, value in graph_dict.items():
        for k, v in value.items():
            value[k] = v["weight"]

    dijkstra(graph_dict, "G1")

    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(graph, seed=42)
    nx.draw_networkx(
        graph,
        pos,
        with_labels=True,
        node_size=400,
        node_color=color_map,
        font_size=12,
    )

    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()


if __name__ == "__main__":
    main()
