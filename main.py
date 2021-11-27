nodes = None


class node:
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_children(self):
        return self.children


def load_tree():
    with open('tree.txt', 'r') as file:
        lines, num_nodes = map(int, file.readline().split(' '))
        nodes = [None] * num_nodes

        for i in range(lines):
            id1, id2 = map(int, file.readline().split(' '))
            if not nodes[id1]:
                nodes[id1] = node(id1)
            if not nodes[id2]:
                nodes[id2] = node(id2)
            nodes[id1].add_child(nodes[id2])
    return nodes[0]


def tree_depth_dfs(rt):
    children = rt.get_children()
    if not children:
        return 0
    children_depth = 0
    for child in children:
        depth = tree_depth_dfs(child)
        if depth > children_depth:
            children_depth = depth
    return children_depth + 1


def tree_depth_bfs(rt):
    depth = 0
    current = [rt]
    next = []
    while current:
        for ele in current:
            children = ele.get_children()
            next.extend(children)
        depth += 1
        current = next
        next = []
    return depth-1

root = load_tree()
print(tree_depth_dfs(root))
print(tree_depth_bfs(root))
