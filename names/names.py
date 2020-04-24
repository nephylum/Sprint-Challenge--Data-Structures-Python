import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

#Replace the nested for loops below with your improvements
## new code: runtime 0.0990145206451416 seconds
import sys
from collections import deque

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
                #self.left.right = self
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
                #self.right.left = self
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else: # target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        cur = self.right
        if cur == None:
            return self.value
        while cur != None:

            if cur.right == None:
                return cur.value
            cur = cur.right
        return cur.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # apply function to initial value
        cb(self.value)

        if self.left:
            self.left.for_each(cb)

        if self.right:
            self.right.for_each(cb)

    # Print all values in order from low to high

    def in_order_print(self, node):
        #Less values (left) first
        if self.left:
            self.left.in_order_print(self.left)
        #base
        print(self.value)
        #greater values (right) last
        if self.right:
            self.right.in_order_print(self.right)
one_list = BinarySearchTree(names_1[0])
for x in names_1[1:]:
    one_list.insert(x)

for x in names_2:
    if one_list.contains(x):
        duplicates.append(x)

# Old code: runtime = 6.807541847229004 seconds
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
