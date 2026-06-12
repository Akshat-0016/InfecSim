import networkx as nx
import matplotlib.pyplot as plt


def generate_world_map(states, routes):

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
            state.name,
            impact=impact
        )

    # Add routes
    for route in routes:

        G.add_edge(
            route.source.name,
            route.destination.name,
            weight=route.daily_travellers
        )

    # Color nodes by impact
    node_colors = []

    for node in G.nodes:

        impact = G.nodes[node]["impact"]

        if impact < 0.25:
            node_colors.append("green")

        elif impact < 0.50:
            node_colors.append("yellow")

        elif impact < 0.75:
            node_colors.append("orange")

        else:
            node_colors.append("red")

    plt.figure(
        figsize=(10, 8)
    )

    pos = nx.spring_layout(
        G,
        seed=42
    )

    nx.draw_networkx_nodes(
        G,
        pos,
        node_color=node_colors,
        node_size=2000
    )

    nx.draw_networkx_labels(
        G,
        pos,
        font_size=10
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
        edge_labels=edge_labels
    )

    plt.title(
        "World Infection Network"
    )

    plt.axis("off")

    plt.savefig(
        "world_map.png"
    )

    plt.close()