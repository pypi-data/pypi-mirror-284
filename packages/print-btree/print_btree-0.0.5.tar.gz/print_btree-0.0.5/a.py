from src.print_btree import print_btree
from src.print_btree.utils import BTree

class N:
    def __init__(self, val):
        self.val = val
        self.l = self.r = None

def show(root): print_btree(root, left='l', right='r')

# root = N(1)
# root.l = N(2)
# root.r = N(3)
# root.l.l = N(4)
# root.l.l.r = N(5)
# root.l.l.r.l = N(6)
# show(root)

root = N('apple')
root.l = N(1)
root.r = N(2)
root.l.l = N('apple')
root.l.r = N('1')
root.r.l = N('pineapple')
root.r.r = N('fuck')
root.l.l.l = N(1)
show(root)