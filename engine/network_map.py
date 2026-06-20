import networkx as nx


def draw_world(ax, states, routes):

    ax.clear()

    G = nx.Graph()

    # =====================
    # STATES
    # =====================

    for state in states:

        healthy, infected, dead = (
            state.get_stats()
        )

        impact = (
            infected + dead
        ) / state.population_size

        G.add_node(
            state.name,
            impact=impact,
            infected=infected,
            dead=dead
        )

    # =====================
    # ROUTES
    # =====================

    for route in routes:

        G.add_edge(
            route.source.name,
            route.destination.name,
            weight=route.daily_travellers
        )

    # =====================
    # COLORS
    # =====================

    node_colors = [

        G.nodes[node]["impact"]

        for node in G.nodes
    ]

    # =====================
    # POSITIONS
    # =====================

    pos = nx.spring_layout(
        G,
        seed=42
    )

    # =====================
    # DRAW NODES
    # =====================

    nx.draw_networkx_nodes(
        G,
        pos,
        node_color=node_colors,
        cmap="Reds",
        vmin=0,
        vmax=1,
        node_size=3500,
        ax=ax
    )

    # =====================
    # DRAW EDGES
    # =====================

    nx.draw_networkx_edges(
        G,
        pos,
        width=2,
        ax=ax
    )

    # =====================
    # EDGE LABELS
    # =====================

    edge_labels = nx.get_edge_attributes(
        G,
        "weight"
    )

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        font_size=8,
        ax=ax
    )

    # =====================
    # NODE LABELS
    # =====================

    labels = {}

    for node in G.nodes:

        state_obj = next(
            s for s in states
            if s.name == node
        )

        player_marker = ""

        if state_obj.is_player:
            player_marker = "\n [PLAYER]"

        labels[node] = (
            f"{node}"
            f"{player_marker}\n"
            f"I:{G.nodes[node]['infected']}\n"
            f"D:{G.nodes[node]['dead']}"
        )

    nx.draw_networkx_labels(
        G,
        pos,
        labels=labels,
        font_size=8,
        ax=ax
    )

    # =====================
    # FINAL TOUCHES
    # =====================

    ax.set_title(
        "Live Epidemic Spread"
    )

    ax.axis("off")

    return pos