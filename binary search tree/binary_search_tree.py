# https://www.youtube.com/watch?v=oSWTXtMglKE&list=PLOuZYwbmgZWXvkghUyMLdI90IwxbNCiWK&index=14
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    def print_in_order(self):
        if self.left is not None:
            self.left.print_in_order()
        print(self.data)
        if self.right is not None:
            self.right.print_in_order()


def build_tree(l=[4, 2, 5, 1, 3, 6]):
    tree = Node(l[0])
    for e in l[1:]:
        tree.insert(e)
    return tree


def traverse_tree():
    tree = build_tree()
    print('traversing tree in order:')
    tree.print_in_order()
    print('')


def search_tree():
    tree = build_tree()
    print('searching tree:')
    print('tree contains 4:', tree.contains(4))
    print('tree contains 10:', tree.contains(10))


def check_BST():
    print('')
    print('create BST and check:')
    root = build_tree()
    print('tree is BST:', check_BST_core(root))
    print('remove the BST property and check:')
    root.left.right.data = 7
    print('tree is BST:', check_BST_core(root))


# https://www.youtube.com/watch?v=i_Q0v_Ct5lY&list=PLOuZYwbmgZWXvkghUyMLdI90IwxbNCiWK&index=19
def check_BST_core(node, node_min=-100, node_max=100):
    if node is None:
        return True
    if node.data < node_min or node.data > node_max:
        return False
    return check_BST_core(node.left, node_min, node.data-1) and check_BST_core(node.right, node.data+1, node_max)

def invert_tree():
   tree = build_tree()
   print('')
   print('tree before inversion:')
   tree.print_in_order()

   print('') 
   print('inverting tree...') 
   inverted_tree = invert_tree_core(tree)

   print('') 
   print('tree after inversion:')
   tree.print_in_order()

def get_data(node): 
   return node.data if node else None 

def invert_tree_core(root):
   # https://favtutor.com/blogs/invert-binary-tree
   if root == None: return None
   print(f'parent: {root.data}') 
   root.left, root.right = invert_tree_core(root.right), invert_tree_core(root.left)
   print(f'children: {get_data(root.left)} {get_data(root.right)}')
   return root

if __name__ == '__main__':
    traverse_tree()
    search_tree()
    check_BST()
    invert_tree()

