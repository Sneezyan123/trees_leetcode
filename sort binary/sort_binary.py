def tree_by_levels(node):
    if not node:
        return []
    queue = [node]
    ans = [node.value]
    while queue:
        el = queue.pop(0)
        if el and el.left:
            queue.append(el.left)
            ans.append(el.left.value)
        if el and el.right:
            queue.append(el.right)
            ans.append(el.right.value)
    return ans