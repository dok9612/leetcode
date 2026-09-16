def buildtree(preorder, inorder):
    def build(preorder, inorder):
        if not preorder:
            return

        root_val = preorder[0]
        root = TreeNode(root_val)

        root_index = inorder.find(root_val)
        left_count = root_index

        left_inorder = inorder[:left_count]
        right_inorder = inorder[left_count + 1 :]

        left_preorder = preorder[1 : 1 + left_count]
        right_preorder = preorder[1 + left_count]

        root.left = build(left_preorder, left_inorder)
        root.right = build(right_preorder, right_inorder)

        return root

    return build(preorder, inorder)
