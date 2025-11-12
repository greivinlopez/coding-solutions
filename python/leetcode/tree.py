from collections import deque
import json

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        list = print_tree_level_order(self)
        return str(list)

    # Level Order Traversal
    def lot(self):
        # Time: O(n)
        # Space: O(n)
        res = []
        q = deque()
        if self:
            q.append(self)

        while q:
            val = []

            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res
    
def get_tree(s):
    return deserialize_binary_tree(s)

def deserialize_binary_tree(data):
    """
    Deserialize a binary tree from LeetCode format string.
    
    Args:
        data (str): Serialized binary tree in format "[5,4,7,3,null,2,null,-1,null,9]"
    
    Returns:
        TreeNode: Root node of the deserialized binary tree, or None if empty
    """
    if not data or data == "[]":
        return None
    
    # Parse the JSON-like string to get list of values
    values = json.loads(data)
    
    if not values or values[0] is None:
        return None
    
    # Create root node
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    # Process nodes level by level
    while queue and i < len(values):
        node = queue.popleft()
        
        # Process left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Process right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

def print_tree_level_order(root):
    """Print tree in level order to verify deserialization"""
    if not root:
        return "[]"
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result

def serialize_binary_tree(root):
    """
    Serialize a binary tree to LeetCode format string.
    
    Args:
        root (TreeNode): Root node of the binary tree
    
    Returns:
        str: Serialized binary tree in format "[5,4,7,3,null,2,null,-1,null,9]"
    """
    if not root:
        return "[]"
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values to match LeetCode format
    while result and result[-1] is None:
        result.pop()
    
    # Convert to JSON string format
    return json.dumps(result)