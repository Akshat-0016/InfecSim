class Graph:

    def __init__(self):
        self.adj = {}

    def add_state(self, state):

        if state not in self.adj:
            self.adj[state] = []

    def connect(
        self,
        source,
        destination,
        travellers
    ):

        self.adj[source].append(
            (destination, travellers)
        )

    def neighbors(self, state):

        return self.adj.get(state, [])