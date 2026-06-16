import tkinter as tk


class EventFeed:

    def __init__(self, parent):

        self.frame = tk.Frame(parent)

        self.frame.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            self.frame,
            text="EVENT FEED",
            font=("Arial", 14, "bold")
        ).pack()

        self.feed = tk.Listbox(
            self.frame
        )

        self.feed.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

    def update_events(self, events):

        self.feed.delete(0, tk.END)

        for event in events:

            self.feed.insert(
                tk.END,
                event
            )