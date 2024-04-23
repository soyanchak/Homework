def tree_by_levels(node):
    if node is None:
        return []
    out = [node.value]
    nodes = [node]
    while nodes:
        node2 = nodes.copy()
        nodes = []
        for node in node2:
            if node.left is not None:
                nodes.append(node.left)
            if node.right is not None:
                nodes.append(node.right)
        out.extend([i.value for i in nodes])
    return out