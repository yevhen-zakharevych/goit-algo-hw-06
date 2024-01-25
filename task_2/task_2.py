from collections import deque
import networkx as nx

from bfs import bfs_recursive
from dfs import dfs_recursive


def main():
    graph = nx.Graph()

    graph.add_nodes_from(["G1", "G2", "G3", "G4", "G5", "R1", "R2", "R3", "R4", "B1", "B2", "B3", "B4"])
    graph.add_edges_from([
        ("G1", "G2"), ("G2", "G3"), ("G3", "G4"), ("G3", "G5"),
        ("R1", "R2"), ("R2", "R3"), ("R3", "R4"),
        ("B1", "B2"), ("B2", "B3"), ("B3", "B4"),
        ("G2", "R2"), ("R2", "B1"), ("G2", "B2")
    ])

    print("bfs search:")
    bfs_recursive(graph, deque(["G1"]))
    print("\ndfs search:")
    dfs_recursive(graph, "G1")


if __name__ == "__main__":
    main()
