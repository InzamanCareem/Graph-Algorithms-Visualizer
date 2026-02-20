from manim import *
from graph import Graphs
import numpy as np


class GraphAnimation(Scene):

    def __init__(self, algorithm=None, start_node=None, end_node=None, **kwargs):
        self.algorithm = algorithm
        self.start_node = start_node
        self.end_node = end_node
        super().__init__(**kwargs)

    def init_graph(self):
        graph = Graphs()

        # graph.add_edge("A", "B", weight=85, directed=True)
        # graph.add_edge("A", "C", weight=20, directed=True)
        # graph.add_edge("B", "D", weight=10)
        # graph.add_edge("B", "E", weight=29, directed=True)
        # graph.add_edge("C", "F", weight=57, directed=True)

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

        # graph.add_edge("0", "1")
        # graph.add_edge("0", "3")
        # graph.add_edge("1", "2")
        # graph.add_edge("1", "3")
        # graph.add_edge("1", "5")
        # graph.add_edge("1", "6")
        # graph.add_edge("3", "2")
        # graph.add_edge("3", "4")
        # graph.add_edge("2", "4")
        # graph.add_edge("2", "5")
        # graph.add_edge("4", "6")

        graph.display_graph()

        return graph

    def make_position(self, i, n, radius):
        angle = 2 * np.pi * i / n
        return np.array(radius * np.array([np.cos(angle), np.sin(angle), 0]))

    def make_node(self, label, pos):
        circle = Circle(radius=0.2, color=WHITE)
        text = Text(label).scale(0.3).move_to(circle)
        node = VGroup(circle, text).move_to(pos)

        return node

    def make_edges(self, graph, nodes):
        edges = VGroup()

        for s, neighbors in graph.items():  # iterating through neighbours of each node
            for e in neighbors:  # iterating through each neighbour in that node
                a = Arrow(nodes[s].get_center(), nodes[e[0]].get_center(), buff=0.2, path_arc=PI / 8,
                          stroke_opacity=0.3, tip_length=0.2, stroke_width=3, stroke_color=BLUE)
                h = a.point_from_proportion(0.8)
                t = MathTex(e[1], color=YELLOW, font_size=25).move_to(h).set_z(1)
                grp = VGroup(a, t, VGroup(nodes[s], nodes[e[0]]))
                edges.add(grp)

        return edges

    def construct(self) -> None:

        # CREATING THE GRAPH
        graph = self.init_graph()

        nodes = {}

        n = len(graph.graph)
        radius = 3
        positions = {}

        for i, label in enumerate(graph.graph.keys()):
            pos = self.make_position(i, n, radius)
            positions[label] = pos

        for label, pos in positions.items():
            node = self.make_node(label, pos)
            nodes[label] = node

        print(nodes)

        edges = self.make_edges(graph.graph, nodes)
        edges_group = VGroup(*[edge.submobjects[:2] for edge in edges.submobjects])

        nodes_group = VGroup(*nodes.values())

        self.play(Create(nodes_group))
        self.play(Create(edges_group))

        self.wait(2)

        # RUNNING THE SEARCH

        label = Text(f"Animation of {self.algorithm} from {self.start_node} to {self.end_node}", font_size=30).to_edge(
            UL)

        self.play(Create(label))

        parents = None
        path = None

        if self.algorithm == "breadth-first-search":
            parents, path = graph.run_breadth_first_search(self.start_node, self.end_node)
        elif self.algorithm == "depth-first-search":
            parents, path = graph.run_depth_first_search(self.start_node, self.end_node)
        elif self.algorithm == "uniform-cost-search":
            parents, path = graph.run_uniform_cost_search(self.start_node, self.end_node)

        # print(parents)

        for i, (lnode, lparent) in enumerate(parents.items()):
            index_p = [j for j, gnode in enumerate(nodes_group.submobjects) if gnode[1].text == lparent]

            index_e = [j for j, edge in enumerate(edges.submobjects) if
                       edge.submobjects[2].submobjects[0].submobjects[1].text == lparent and
                       edge.submobjects[2].submobjects[1].submobjects[1].text == lnode]

            index_c = [j for j, gnode in enumerate(nodes_group.submobjects) if gnode[1].text == lnode]

            # Circle the parent
            if index_p:
                self.play(Circumscribe(nodes_group[index_p[0]], shape=Circle))

            # Arrow source to destination
            if index_e:
                progress_arrow = edges[index_e[0]].submobjects[0].copy().set_stroke(opacity=1)
                self.play(Create(progress_arrow), run_time=2)

            # Flash the child
            self.play(Flash(nodes_group[index_c[0]]))

        # Make the final path red

        for i in range(len(path)):
            index_e = [j for j, edge in enumerate(edges.submobjects) if
                       edge.submobjects[2].submobjects[0].submobjects[1].text == path[i] and
                       edge.submobjects[2].submobjects[1].submobjects[1].text == path[i + 1]]

            # Arrow source to destination
            if index_e:
                progress_arrow = edges[index_e[0]].submobjects[0].copy()
                progress_arrow.set_stroke(color=RED, opacity=1)
                progress_arrow.set_color(RED)
                self.play(Create(progress_arrow), run_time=2)

        self.wait(2)
