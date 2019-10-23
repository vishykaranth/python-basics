from binary_search_tree import BinarySearchTree

bst = BinarySearchTree()

bst.insert(15)
bst.insert(10)
bst.insert(8)
bst.insert(12)
bst.insert(20)
bst.insert(17)
bst.insert(25)
bst.insert(19)

print(bst.find(15))
print(bst.find(10))
print(bst.find(56))
print(bst.find(8))
print(bst.find(12))
print(bst.find(20))
print(bst.find(17))
print(bst.find(25))
print(bst.find(19))
print(bst.find(0))

print()

print('Pre Order')
bst.pre_order()
print()

print('In Order')
bst.in_order()
print()

print('Post Order')
bst.post_order()
print()

print('BFS')
bst.bfs()

print('We are done :)')