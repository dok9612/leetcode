def is_same(a, b) -> bool:
    if not a and not b:
        return True
    # this
    if not a or not b:
        return False

    if a.val != b.val:
        return False

    if a.val == b.val:
        return True

    left = is_same(a.left, b.left)
    right = is_same(a.right, b.right)

    return left and right
