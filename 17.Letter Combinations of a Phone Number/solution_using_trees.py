from typing import List


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        current_node = self
        name = '[ '
        while current_node.next is not None:
            name += f'{current_node.value}, '
            current_node = current_node.next

        return name + f'{current_node.value} ]'

    def append(self, value):
        new_node = ListNode(value)
        current_node = self
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def __str__(self):
        return f'node data = {self.data}'

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def add_parent(self, parent):
        self.parent = parent

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def get_children(self):
        return self.children

    def get_leafs(self, leafs: ListNode):
        current_node = self
        if not current_node.children:
            leafs.append(current_node)
        else:
            for child in current_node.children:
                child.get_leafs(leafs)

    def get_pathway_from_leaf(self, leaf: 'TreeNode') -> ['TreeNode']:
        current_node = leaf
        path = []
        while current_node is not None:
            path.append(current_node)
            current_node = current_node.parent

        return reversed(path)

    def get_pathways(self) -> List['TreeNode']:
        leafs = ListNode('')
        self.get_leafs(leafs)

        current_leaf = leafs.next
        pathway_list = []
        while current_leaf is not None:
            pathway_list.append(self.get_pathway_from_leaf(current_leaf.value))
            current_leaf = current_leaf.next

        return pathway_list

    def print(self):
        print('\t' * self.get_level() + '|__' + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print()


class Solution:
    def get_letters(self, digit: str) -> List[str]:
        digits_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        try:
            return digits_dict[digit]
        except IndexError:
            raise Exception(f'The index {digit} is out of digits_dict range')

    def add_letter_as_child(self, node: TreeNode, letter: str):
        new_node = TreeNode(letter)
        node.add_child(new_node)

    def add_letters_as_children(self, node: TreeNode, letters: List[str]):
        for letter in letters:
            self.add_letter_as_child(node, letter)

    def init_tree(self) -> TreeNode:
        return TreeNode('')

    def fill_tree(self, node: TreeNode, digits: str):
        current_level = node.get_level()
        try:
            current_digit = digits[current_level]
            letters = self.get_letters(current_digit)
            self.add_letters_as_children(node, letters)

            children = node.get_children()
            for child in children:
                self.fill_tree(child, digits)
        except IndexError:
            pass

    def get_string_from_pathway(self, pathway: List[TreeNode]) -> str:
        return_value = ''
        for each in pathway:
            return_value += each.data
        return return_value

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '' or digits is None:
            return []

        tree = self.init_tree()

        self.fill_tree(tree, digits)

        pathway_list = tree.get_pathways()

        letter_combinations = []

        for pathway in pathway_list:
            letter_combinations.append(self.get_string_from_pathway(pathway))

        return letter_combinations


if __name__ == "__main__":
    digits = "23"  # Example input, replace with your desired input
    result = Solution().letterCombinations(digits)

