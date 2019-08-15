from lca_tree import lca
from tree import tree

print("Running tests...")
assert lca(tree, "Montreal", "Canada").value == "Canada"
assert lca(tree, "Canada", "United States").value == "Earth"
assert lca(tree, "San Francisco", "San José").value == "California"
print("All tests passed")