# ternary solution
def max_depth(root):
    if root == None:
        return 0
    elif root.left == None and root.right == None:
        return 0
    else:
        return 1 + (max_depth(root.left) if max_depth(root.left) >= max_depth(root.right) else max_depth(root.right))

# separate function solution
def height(root):
    if root:
        return search(root, 0)
    return 0

def search(root, height):
    if root.left and root.right:
        return max(search(root.left, height + 1), search(root.right, height + 1))
    elif root.left and root.right == None:
        return search(root.left, height + 1)
    elif root.right and root.left == None:
        return search(root.right, height + 1)
    else:
        return height