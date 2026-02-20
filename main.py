import argparse
from graph_animator import GraphAnimation


def main(alg, start, end):
    scene = GraphAnimation(algorithm=alg, start_node=start, end_node=end)
    scene.render(preview=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compiling Animation")

    parser.add_argument("--alg", type=str, required=True,
                        choices=["breadth-first-search", "depth-first-search", "uniform-cost-search"],
                        help="Which graph algorithm to run")

    parser.add_argument("--start", type=str, required=False, help="Which graph node to start with")

    parser.add_argument("--end", type=str, required=False, help="Which graph node to end with")

    args = parser.parse_args()

    main(args.alg, args.start, args.end)
