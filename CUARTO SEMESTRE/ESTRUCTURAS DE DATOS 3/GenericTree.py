class Node:
    def __init__(self, key, parent):
        self.key = key
        self.parent = parent
        self.children = [None] * 26 


class genericTree:
    def __init__(self):
        self.root = None