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
    stack = ships

    while True:
        prevStack = stack.copy()
        stack = []
        for i in prevStack:
            if len(stack) == 0:
                stack.append(i)
            elif stack[-1] > 0 and i < 0:
                if stack[-1] > -i:
                    pass
                elif stack[-1] < -i:
                    stack.pop()
                    stack.append(i)
                else:
                    stack.pop()
        if stack == prevStack:
            break

    return prevStack


if __name__ == "__main__":
    # Example sanity checks (see test.py for the real test cases)
    print(surviving_ships([6, 3, -5]))  # expected: [6]
    print(surviving_ships([8, -8]))     # expected: []
