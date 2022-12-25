# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    nodeSums(root, 0, sums)
    return sums

def nodeSums(node, runningSum, sums):
    if node is None:
        return

    runningSum += node.value
    if node.left is None and node.right is None:
        sums.append(runningSum)

    nodeSums(node.left, runningSum, sums)
    nodeSums(node.right, runningSum, sums)
    return runningSum
