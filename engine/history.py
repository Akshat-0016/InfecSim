from data.db import init_db, get_connection
import matplotlib.pyplot as plt

init_db()
class History:

    def __init__(self):

        self.days = []

        self.healthy = []

        self.infected = []

        self.dead = []

        self.gdp = []

        self.support = []

    def store(
            self,
            day,
            state_name,
            healthy,
            infected,
            dead,
            gdp,
            support
        ):
        conn = get_connection()
     
        conn.execute(
            """
            INSERT INTO simulation_data
            (
                day,
                state,
                healthy,
                infected,
                dead,
                gdp,
                support
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                day,
                state_name,
                healthy,
                infected,
                dead,
                gdp,
                support
            )
        )

        conn.commit()
        conn.close()

    def graph(self):

        conn = get_connection()

        data = conn.execute(
            """
            SELECT
                day,
                SUM(healthy) AS healthy,
                SUM(infected) AS infected,
                SUM(dead) AS dead
            FROM simulation_data
            GROUP BY day
            ORDER BY day
            """
        ).fetchall()

        conn.close()

        days = [row["day"] for row in data]

        healthy = [
            row["healthy"]
            for row in data
        ]

        infected = [
            row["infected"]
            for row in data
        ]

        dead = [
            row["dead"]
            for row in data
        ]

        plt.figure(figsize=(10,6))

        plt.plot(
            days,
            healthy,
            label="Healthy"
        )

        plt.plot(
            days,
            infected,
            label="Infected"
        )

        plt.plot(
            days,
            dead,
            label="Dead"
        )

        plt.xlabel("Day")

        plt.ylabel("Population")

        plt.title(
            "Disease Progression"
        )

        plt.legend()

        plt.grid()

        plt.savefig(
            "disease_progression.png"
        )

        plt.close()


    def gdp_graph(self):

        conn = get_connection()

        data = conn.execute(
            """
            SELECT
                day,
                AVG(gdp) AS gdp
            FROM simulation_data
            GROUP BY day
            ORDER BY day
            """
        ).fetchall()

        conn.close()

        days = [
            row["day"]
            for row in data
        ]

        gdp = [
            row["gdp"]
            for row in data
        ]

        plt.figure(figsize=(10,6))

        plt.plot(
            days,
            gdp,
            label="GDP"
        )

        plt.xlabel("Day")
        plt.ylabel("GDP")

        plt.title(
            "Average GDP"
        )

        plt.grid()

        plt.savefig(
            "gdp.png"
        )

        plt.close()

    def support_graph(self):

        conn = get_connection()

        data = conn.execute(
            """
            SELECT
                day,
                AVG(support) AS support
            FROM simulation_data
            GROUP BY day
            ORDER BY day
            """
        ).fetchall()

        conn.close()

        days = [
            row["day"]
            for row in data
        ]

        support = [
            row["support"]
            for row in data
        ]

        plt.figure(figsize=(10,6))

        plt.plot(
            days,
            support,
            label="Support"
        )

        plt.xlabel("Day")
        plt.ylabel("Support")

        plt.title(
            "Public Support"
        )

        plt.grid()

        plt.savefig(
            "support.png"
        )

        plt.close()