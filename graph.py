from pyglet.window.key import BREAK

from custom_queue import Queue, PriorityQueue
from custom_stack import Stack

from typing import List, Tuple, Dict, Optional


class Graphs:
    def __init__(self):
        self.graph: Dict[str, List[Tuple[str, int]]] = {}

    def _check_exists(self, node: str) -> bool:
        return node in self.graph.keys()

    def add_node(self, node: str) -> None:
        if not self._check_exists(node):
            self.graph[node]: List[Tuple[str, int]] = []

    def add_edge(self, node: str, other: str, weight: int = 1, directed: bool = False) -> None:

        # Add nodes if not added using the add_node method
        self.add_node(node)
        self.add_node(other)

        self.graph.get(node).append((other, weight))
        if not directed:
            self.graph.get(other).append((node, weight))

    def display_graph(self) -> None:
        print(self.graph)

    def run_breadth_first_search(self, start_node: str, target_node: Optional[str] = None) -> Tuple[
        Dict[str, Optional[str]], List[str]]:
        queue = Queue()
        queue.enqueue(start_node)
        visited_nodes = [start_node]
        parents = {start_node: None}
        final_path = []

        while not queue.is_empty():
            # print(f"Queue: {queue.show()}")
            current_node = queue.dequeue()

            if current_node == target_node:
                break

            for node in self.graph.get(current_node):
                if node[0] not in visited_nodes:
                    queue.enqueue(node[0])
                    parents[node[0]] = current_node
                    visited_nodes.append(node[0])

        print(f"All visited nodes: {visited_nodes}")

        # print(f"Parents: {parents}")

        if target_node:
            node = target_node
            while node is not None:
                final_path.append(node)
                node = parents[node]

            print(f"Path: {final_path[::-1]}")

        return parents, final_path[::-1]

    def run_depth_first_search(self, start_node: str, target_node: Optional[str] = None) -> Tuple[
        Dict[str, Optional[str]], List[str]]:
        stack = Stack()
        stack.push(start_node)
        visited_nodes = [start_node]
        parents = {start_node: None}
        final_path = []

        while not stack.is_empty():
            # print(f"Stack: {stack.show()}")
            current_node = stack.pop()

            if current_node == target_node:
                break

            for node in self.graph.get(current_node):
                if node[0] not in visited_nodes:
                    stack.push(node[0])
                    parents[node[0]] = current_node
                    visited_nodes.append(node[0])

        print(f"All visited nodes: {visited_nodes}")

        # print(f"Parents: {parents}")

        if target_node:
            node = target_node
            while node is not None:
                final_path.append(node)
                node = parents[node]

            print(f"Path: {final_path[::-1]}")

        return parents, final_path[::-1]

    def run_uniform_cost_search(self, start_node: str, target_node: Optional[str] = None) -> Tuple[
        Dict[str, Optional[str]], List[str]]:
        pqueue = PriorityQueue()
        pqueue.enqueue((start_node, 0))
        visited_nodes = [start_node]
        parents = {start_node: None}
        final_path = []

        while not pqueue.is_empty():
            # print(f"Priority Queue: {pqueue.show()}")
            current_node = pqueue.dequeue()

            if current_node == target_node:
                break

            # Get children
            for node in self.graph.get(current_node[0]):
                if node[0] not in visited_nodes:
                    pqueue.enqueue((node[0], node[1] + current_node[1]))
                    visited_nodes.append(node[0])
                    parents[node[0]] = current_node[0]
                else:
                    item = pqueue.get(node[0])
                    if item is not None:
                        if node[1] + current_node[1] < item[1]:
                            pqueue.remove(item)
                            pqueue.enqueue((node[0], node[1] + current_node[1]))

        print(f"All visited nodes: {visited_nodes}")
        # print(parents)

        if target_node:
            node = target_node
            while node is not None:
                final_path.append(node)
                node = parents[node]

            print(f"Path: {final_path[::-1]}")

        return parents, final_path[::-1]

    def run_depth_limited_search(self, start_node: str, target_node: Optional[str] = None, depth_limit: int = 5) -> \
            Tuple[
                Dict[str, Optional[str]], List[str]]:
        stack = Stack()
        stack.push(start_node)
        visited_nodes = []
        parents = {start_node: None}
        final_path = []

        while not stack.is_empty():
            depth_list = []
            current_node = stack.pop()

            if current_node == target_node:
                break

            node = current_node
            while node is not None:
                depth_list.append(node)
                node = parents[node]

            if len(depth_list) - 1 <= depth_limit:
                for node in self.graph.get(current_node):
                    if node[0] not in visited_nodes and node[0] not in stack.stack:
                        stack.push(node[0])
                        parents[node[0]] = current_node

                visited_nodes.append(current_node)

        print(f"All visited nodes: {visited_nodes}")

        print(f"Parents: {parents}")

        if target_node:
            node = target_node
            while node is not None:
                final_path.append(node)
                node = parents[node]

            print(f"Path: {final_path[::-1]}")

        return parents, final_path[::-1]
