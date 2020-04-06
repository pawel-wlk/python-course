import random


class Node(object):
    def __init__(self, value, children):
        self.value = value
        self.children = children


def generate_tree(height):
    val = random.randint(-100, 100)

    if height == 1:
        return Node(val, [])

    subtrees_num = random.randint(1, 10)
    biggest_subtree_idx = random.randrange(0, subtrees_num)

    return Node(val, [generate_tree(height-1) if i == biggest_subtree_idx else generate_tree(random.randint(1, height-1)) for i in range(subtrees_num)])


def tree_dfs(t):
    yield t.value
    for subtree in t.children:
        yield from tree_dfs(subtree)


def tree_bfs(t):
    subtrees = [t]
    while len(subtrees) > 0:
        new_subtrees = []

        for subtree in subtrees:
            yield subtree.value
            for subsubtree in subtree.children:
                new_subtrees.append(subsubtree)

        subtrees = new_subtrees.copy()


t = generate_tree(3)
print(t)
print(list(tree_dfs(t)))
print(list(tree_bfs(t)))
