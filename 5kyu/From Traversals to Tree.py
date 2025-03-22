from preloaded import TreeNode
    
def build_tree(inorder, postorder):
    # no nodes available 
    if not inorder or not postorder:
        return None
    
    # map the values to their indices in inorder traversal
    inorder_indices = {val: idx for idx, val in enumerate(inorder)}
    
    def build_subtree(left, right):
        # no nodes in subtree (end of recursive loop)
        if left > right:
            return None
        
        # last element of postorder is root
        root_val = postorder.pop()  # save and remove last element
        root = TreeNode(root_val)   # new TreeNode (new branch)

        # find root in inorder list
        root_index_in_inorder = inorder_indices[root_val]

        # build the right and left subtree (recursive)
        # postorder goes from left to right -> first the right subtree
        root.right = build_subtree(root_index_in_inorder + 1, right)
        root.left = build_subtree(left, root_index_in_inorder - 1)
        
        return root
    
    # build the tree using build_subtree
    return build_subtree(0, len(inorder) - 1)
  
