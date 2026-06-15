import networkx as nx
import matplotlib.pyplot as plt

plt.ion()

fig, ax = plt.subplots(
    figsize=(10, 8)
)

# Fixed map layout
POSITIONS = {

    "state_1": (0, 2),

    "state_2": (2, 3),

    "state_3": (2, 1),

    "state_4": (4, 2),

    "state_5": (3, -1)

}


def update_world_map(states, routes):

    ax.clear()

    G = nx.Graph()

    # Add states
    for state in states:

        healthy, infected, dead = (
            state.get_stats()
        )

        impact = (
            infected + dead
        ) / state.population_size

        G.add_node(
            f"{state.name}\nI:{infected}\nD:{dead}",
            impact=impact
        )

    # Add routes
    for route in routes:

        source = route.source.name
        destination = route.destination.name

        source_label = None
        destination_label = None

        for node in G.nodes:

            if node.startswith(source):
                source_label = node

            if node.startswith(destination):
                destination_label = node

        if source_label and destination_label:

            G.add_edge(
                source_label,
                destination_label,
                weight=route.daily_travellers
            )

    # Node colors
    node_colors = [

        G.nodes[node]["impact"]

        for node in G.nodes
    ]

    # Fixed positions
    pos = {}

    for node in G.nodes:

        state_name = node.split("\n")[0]

        pos[node] = POSITIONS[
            state_name
        ]

    nx.draw_networkx_nodes(
        G,
        pos,
        node_color=node_colors,
        cmap=plt.cm.Reds,
        vmin=0,
        vmax=1,
        node_size=3500
    )

    nx.draw_networkx_labels(
        G,
        pos,
        font_size=8
    )

    nx.draw_networkx_edges(
        G,
        pos,
        width=2
    )

    edge_labels = nx.get_edge_attributes(
        G,
        "weight"
    )

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        font_size=8
    )

    ax.set_title(
        "Live Epidemic Spread"
    )

    ax.axis("off")

    plt.draw()

    plt.pause(0.001)