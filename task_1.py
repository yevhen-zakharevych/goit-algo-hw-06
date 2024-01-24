import networkx as nx
import matplotlib.pyplot as plt


def main():
    graph = nx.Graph()
    color_map = [
        'green', 'green', 'green', 'green', 'green',
        'red', 'red', 'red', 'red',
        'blue', 'blue', 'blue', 'blue'
    ]

    graph.add_nodes_from(["G1", "G2", "G3", "G4", "G5", "R1", "R2", "R3", "R4", "B1", "B2", "B3", "B4"])
    graph.add_edges_from([
        ("G1", "G2"), ("G2", "G3"), ("G3", "G4"), ("G3", "G5"),
        ("R1", "R2"), ("R2", "R3"), ("R3", "R4"),
        ("B1", "B2"), ("B2", "B3"), ("B3", "B4"),
        ("G2", "R2"), ("R2", "B1"), ("G2", "B2")

    ])

    print(f"кількість вершин: {graph.number_of_nodes()}")
    print(f"кількість ребер: {graph.number_of_edges()}")
    print(f"cтупінь вершин: {graph.degree()}")

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
    plt.show()


if __name__ == "__main__":
    main()
