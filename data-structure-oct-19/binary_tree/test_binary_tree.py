from binary_tree import BinaryTree

tree = BinaryTree('a')
print(tree.value) # a
print(tree.left_child) # None
print(tree.right_child) # None

a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')

b_node = a_node.left_child
b_node.insert_right('d')

c_node = a_node.right_child
c_node.insert_left('e')
c_node.insert_right('f')

d_node = b_node.right_child
e_node = c_node.left_child
f_node = c_node.right_child

print(a_node.value) # a
print(b_node.value) # b
print(c_node.value) # c
print(d_node.value) # d
print(e_node.value) # e
print(f_node.value) # f


node_1 = BinaryTree('1')
node_1.insert_left('2')
node_1.insert_right('5')

node_2 = node_1.left_child
node_2.insert_left('3')
node_2.insert_right('4')

node_5 = node_1.right_child
node_5.insert_left('6')
node_5.insert_right('7')

print("In Order Display ")
node_1.in_order();

print("Pre Order Display ")
node_1.pre_order();

print("Post Order Display ")
node_1.post_order();