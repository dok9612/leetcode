def buildtree(preorder, inorder):
    def build(preorder, inorder):
        if not preorder:
            return None

        # the root is always the first val of 'preorder'
        root_val = preorder[0]
        root = TreeNode(root_val)

        # find the index of the root within the 'inorder' - this also serves as
        # the number of nodes of the left in the preorder.
        root_index = inorder.index(root_val)  # O(n)

        left_size = root_index

        # we find the left/right of the inorder that separates which are for left, which are for right
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1 :]

        left_preorder = preorder[1 : 1 + left_size]  # [1:] bc first is the root
        right_preorder = preorder[1 + left_size :]

        # we fuck it and leave the children to solve for themselves and reconstruction
        root.left = build(left_preorder, left_inorder)  # O(n) copying
        root.right = build(right_preorder, right_inorder)

        return root  # bc we are returning the root nothing else

    return build(preorder, inorder)
