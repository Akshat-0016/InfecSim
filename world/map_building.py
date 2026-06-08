from world.graph import Graph

def create_world(states):

    graph = Graph()

    for state in states:
        graph.add_state(state)

    graph.connect(
        states[0],
        states[1],
        100
    )

    graph.connect(
        states[1],
        states[2],
        100
    )

    graph.connect(
        states[2],
        states[3],
        100
    )

    return graph