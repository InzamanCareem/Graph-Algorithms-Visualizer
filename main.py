from graph import Graphs
from graph_animator import GraphAnimation

graph = Graphs()

graph.add_edge("S", "A", directed=True, weight=5)
graph.add_edge("S", "B", directed=True, weight=9)
graph.add_edge("S", "D", directed=True, weight=6)
graph.add_edge("D", "S", directed=True, weight=1)
graph.add_edge("A", "G1", directed=True, weight=9)
graph.add_edge("A", "B", directed=True, weight=3)
graph.add_edge("B", "A", directed=True, weight=2)
graph.add_edge("B", "C", directed=True, weight=1)
graph.add_edge("C", "S", directed=True, weight=6)
graph.add_edge("C", "G2", directed=True, weight=5)
graph.add_edge("C", "F", directed=True, weight=7)
graph.add_edge("D", "C", directed=True, weight=2)
graph.add_edge("D", "E", directed=True, weight=2)
graph.add_edge("E", "G3", directed=True, weight=7)
graph.add_edge("F", "D", directed=True, weight=2)
graph.add_edge("F", "G3", directed=True, weight=8)

if __name__ == "__main__":
    scene = GraphAnimation(graph=graph, algorithm="uniform-cost-search", start_node="S", end_node="G3")
    scene.render(preview=True)
