from typing import List
from tree import tree, Tree


def search(root: Tree, x: str, y: str):
    if root.value == x or root.value == y: return True
    elif root.value != x and root.value != y and not root.nodes: False
    else: return any([search(node, x, y) for node in root.nodes])

def lca(root: Tree, x: str, y: str) -> Tree:
    if root.nodes == []: return None
    if root.value == x or root.value == y: return root
    results = [node for node in root.nodes if search(node, x, y)]
    if len(results) == 2: return root
    elif len(results) == 1: return lca(results[0], x, y)
    
print(lca(tree, "Miami", "Orlando").value)