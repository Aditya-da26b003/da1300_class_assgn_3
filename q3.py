from typing import Optional


class TreeNode:
    """Binary tree node for the org chart."""
    def __init__(self, salary=0, left=None, right=None):
        self.salary = salary
        self.left = left
        self.right = right
        self.avg = None

def avg(root):
    if root.left == None and root.right == None:
        if root.avg == None:
            root.avg = [root.salary, 1]
        return root.avg
    elif root.left == None:
        if root.right.avg == None:
            root.right.avg = avg(root.right)
        a = root.right.avg
        return [a[0] + root.salary, a[1] + 1]
    elif root.right == None:
        if root.left.avg == None:
            root.left.avg = avg(root.left)
        a = root.left.avg
        return [a[0] + root.salary, a[1] + 1]
    else:
        if root.left.avg == None:
            root.left.avg = avg(root.left)
        l = root.left.avg
        if root.right.avg == None:
            root.right.avg = avg(root.right)
        r = root.right.avg 

        return [root.salary + l[0] + r[0], l[1] + r[1] + 1]

def count_fair_managers(root: Optional[TreeNode]) -> int:
    """
    Problem 3: Fair managers in an org chart.

    Given the root of a binary tree where each node has a `salary`,
    count the number of nodes whose salary equals the floor-division
    average salary of their entire subtree (including themselves).

    Args:
        root: root TreeNode of the org chart (or None for empty chart).

    Returns:
        Number of fair managers in the tree.
    """
    if root == None:
        return 0

    if root.avg == None:
        root.avg = avg(root)
    a = root.avg
    if root.salary == a[0]//a[1]:
        return 1 + count_fair_managers(root.right) + count_fair_managers(root.left)
    return count_fair_managers(root.right) + count_fair_managers(root.left)


if __name__ == "__main__":
    # Example sanity check (see test.py for the real test cases)
    # root = [1] -> a single employee is trivially a fair manager
    root = TreeNode(1)
    print(count_fair_managers(root))  # expected: 1
