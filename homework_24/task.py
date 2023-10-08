# Програма мінімум:

# Розширити структуру, яку побудували на уроці, можливістю
# вставки дерева в наявне дерево та видалення піддерева з дерева,
# що існує.


# Середній рівень:

# -

# Програма максимум:

# Написати алгоритм, що буде парсити html документ та зберігати
# його Document Object Model (DOM) у дереві. Дерево повинно зберігати
# тег та текст, обрамлений цим тегом (якщо є такий). Додати можливість
# пошуку тексту за тегом.

# Вхідні дані: html документ та тег


# Вихідні дані: текст, якщо є.
#
class TreeManager:
    @staticmethod
    def add_tree(target_tree, other_tree):
        for key in other_tree:
            target_tree[key] = other_tree[key]

    @staticmethod
    def remove_tree(target_tree, other_tree):
        for key in other_tree:
            if key in target_tree:
                del target_tree[key]


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None) -> None:
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    @property
    def has_left_child(self) -> bool:
        return bool(self.left_child)

    @property
    def has_right_child(self) -> bool:
        return bool(self.right_child)

    @property
    def is_left_child(self) -> bool:
        return self.parent and self.parent.left_child == self

    @property
    def is_right_child(self) -> bool:
        return self.parent and self.parent.right_child == self

    @property
    def is_root(self) -> bool:
        return not self.parent

    @property
    def is_leaf(self) -> bool:
        return not (self.right_child or self.left_child)

    @property
    def has_any_children(self) -> bool:
        return self.right_child or self.left_child

    @property
    def has_both_children(self) -> bool:
        return self.right_child and self.left_child

    def replace_node_data(self, key, val, lc, rc) -> None:
        self.key = key
        self.payload = val
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child:
            self.left_child.parent = self
        if self.has_right_child:
            self.right_child.parent = self

    def find_successor(self):
        succ = None
        if self.has_right_child:
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child:
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        return succ

    def find_min(self):
        current = self
        while current.has_left_child:
            current = current.left_child
        return current

    def splice_out(self):
        if self.is_leaf:
            if self.is_left_child:
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children:
            if self.has_left_child:
                if self.is_left_child:
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child:
                    self.parent.leftChild = self.right_child
                else:
                    self.parent.rightChild = self.right_child
                self.right_child.parent = self.parent

    def __iter__(self):
        if self:
            if self.has_left_child:
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.has_right_child:
                for elem in self.right_child:
                    yield elem


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def _put(self, key, val, current_node: TreeNode) -> None:
        if key < current_node.key:
            if current_node.has_left_child:
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
        else:
            if current_node.has_right_child:
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)

    def put(self, key, val) -> None:
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
        return None

    def _get(self, key, current_node: TreeNode):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item) -> bool:
        if self._get(item, self.root):
            return True
        return False

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError(f"Error, key: {key} not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError(f"Error, key: {key} not in tree")

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, current_node: TreeNode):
        if current_node.is_leaf:
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children:
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.payload
        else:  # this node has one child
            if current_node.has_left_child:
                if current_node.is_left_child:
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child:
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                else:
                    current_node.replace_node_data(
                        current_node.left_child.key,
                        current_node.left_child.payload,
                        current_node.left_child.left_child,
                        current_node.left_child.right_child,
                    )
            else:
                if current_node.is_left_child:
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child:
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(
                        current_node.right_child.key,
                        current_node.right_child.payload,
                        current_node.right_child.left_child,
                        current_node.right_child.right_child,
                    )


if __name__ == "__main__":
    mytree = BinarySearchTree()
    mytree[3] = "red"
    mytree[4] = "blue"
    mytree[6] = "yellow"
    mytree[2] = "tomayo"

    print("-----My first tree-----")
    for key in mytree:
        print(key, mytree[key])

    second_tree = BinarySearchTree()
    second_tree[8] = "green"
    second_tree[5] = "orange"
    second_tree[9] = "purple"
    second_tree[11] = "gold"

    print("-----My second tree-----")
    for key in second_tree:
        print(key, second_tree[key])

    TreeManager.add_tree(mytree, second_tree)

    print("-----My fist tree add second tree-----")
    for key in mytree:
        print(key, mytree[key])

    TreeManager.remove_tree(mytree, second_tree)

    print("-----My new tree remove second tree-----")
    for key in mytree:
        print(key, mytree[key])
