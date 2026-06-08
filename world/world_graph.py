def display_world(routes):

    print("\n===== WORLD MAP =====")

    for route in routes:

        print(
            f"{route.source.name}"
            f" --({route.daily_travellers})--> "
            f"{route.destination.name}"
        )

    print("=====================\n")