# Binary Tree Node class
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Insert a new node with the given key
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Inorder traversal of the binary tree
def inorder(root, sorted_list):
    if root:
        inorder(root.left, sorted_list)
        sorted_list.append(root.val)
        inorder(root.right, sorted_list)

# Tree Sort function
def tree_sort(arr):
    if not arr:
        return []
    
    root = Node(arr[0])
    for i in range(1, len(arr)):
        root = insert(root, arr[i])
    
    sorted_list = []
    inorder(root, sorted_list)
    return sorted_list

# Example usage
if __name__ == "__main__":
    arr = [5, 3, 7, 2, 8, 1, 4]
    print("Original array:", arr)
    sorted_arr = tree_sort(arr)
    print("Sorted array:", sorted_arr)
