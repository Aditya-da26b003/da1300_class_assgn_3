from typing import List


def surviving_ships(ships: List[int]) -> List[int]:
    """
    Problem 2: Spaceship collisions.

    Given a list of ship engine powers (sign = direction: positive is
    right, negative is left), resolve all collisions between ships
    moving toward each other and return the engine powers (with sign)
    of the ships that remain.

    Args:
        ships: list of signed engine powers.

    Returns:
        List of signed engine powers of surviving ships, left to right.
    """
    i = 0
    while i < len(ships):
        if ships[i] > 0:
            i += 1
        else:
            while True:
                if i == 0 or ships[i-1] < 0:
                    i += 1
                    break
                if ships[i-1] < -ships[i]:
                    ships.pop(i-1)
                    i -= 1
                elif ships[i-1] > -ships[i]:
                    ships.pop(i)
                    break
                else:
                    ships.pop(i)
                    ships.pop(i-1)
                    i -= 1
                    break
    return ships


if __name__ == "__main__":
    # Example sanity checks (see test.py for the real test cases)
    print(surviving_ships([6, 3, -5]))  # expected: [6]
    print(surviving_ships([8, -8]))     # expected: []
    print(surviving_ships([-2,-1,1,2]))
