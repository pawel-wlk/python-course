import random

def generate_tree(height):
    if height == 0:
        return None

    val = random.randint(-100, 100)

    big_tree = generate_tree(height-1)
    small_tree = generate_tree(random.randint(0, height-1))


    LEFT_BRANCH = 0
    RIGHT_BRANCH = 1
    choice = random.choice([LEFT_BRANCH, RIGHT_BRANCH])


    if choice == LEFT_BRANCH:
        return [val, big_tree, small_tree]
    else:
        return [val, small_tree, big_tree]

def tree_dfs(t):
    if t == None:
        return
    yield t[0]
    yield from tree_dfs(t[1])
    yield from tree_dfs(t[2])

def tree_bfs(t):
    if t == None:
        return
    

    subtrees = [t]
    while len(subtrees) > 0:
        new_subtrees = []

        for subtree in subtrees:
            if subtree == None:
                continue
            yield subtree[0]
            new_subtrees.append(subtree[1])
            new_subtrees.append(subtree[2])
        
        subtrees = new_subtrees.copy()



t = generate_tree(5)
print(t)
print(list(tree_dfs(t)))
print(list(tree_bfs(t)))
