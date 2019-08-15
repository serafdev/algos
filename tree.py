class Tree:
    def __init__(self, value, nodes=[]):
        self.value: str = value
        self.nodes: List[Tree] = nodes

tree = Tree("Earth",
    [
        Tree("Canada",
            [
                Tree("Ontario",
                    [
                        Tree("Ottawa"),
                        Tree("Toronto"),
                    ]
                ),
                Tree("Quebec",
                    [
                        Tree("Montreal"),
                        Tree("Trois-Rivière"),
                    ]
                ),
            ]
        ),
        Tree("United States",
            [
                Tree("California",
                    [
                        Tree("San José"),
                        Tree("San Francisco"),
                    ]
                ),
                Tree("Florida",
                    [
                        Tree("Miami"),
                        Tree("Fort-Lauderdale"),
                        Tree("Orlando"),
                    ]
                ),
            ]
        ),
    ]
)