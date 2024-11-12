"""EX01 TEA PARTY - Caua Victor"""

__author__ = "730798914"


def main_planner(guests: int) -> None:
    """Definig the final function which will print the output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")

    # Direct function calls
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Total Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))

    return None


def tea_bags(people: int) -> int:
    """Calculating the number of bags based in the number of people"""
    return 2 * people


def treats(people: int) -> int:
    """calculating the number of treats based in the number of people"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """computing the cost of bags plus treats"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
