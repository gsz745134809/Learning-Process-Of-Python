myTree = [ 'a',  # root
		[
			'b',  # left subtree
			[
				'd', [], []
			],
			[
				'e', [], []
			]
		],
		[
			'c',  # right subtree
			[
				'f', [], []
			],
			[
			]
		]
]

print(myTree)
print('left subTree = ', myTree[1])
print('root = ', myTree[0])
print('right subTree = ', myTree[2])


def BinaryTree(r):
	return [r, [], []]


def insertLeft(root, newBranch):
	t = root.pop(1)
	print(t)
	if len(t) > 1:
		root.insert(1, [newBranch, t, []])
	else:
		root.insert(1, [newBranch, [], []])
	return root


def insertRight(root, newBranch):
	t = root.pop(2)
	print(t)
	if len(t) > 1:
		root.insert(1, [newBranch, t, []])
	else:
		root.insert(1, [newBranch, [], []])
	return root


def getRootVal(root):
	return root[0]


def setRootVal(root, newVal):
	root[0] = newVal


def getLeftChild(root):
	return root[1]


def getRightChild(root):
	return root[2]


a = BinaryTree(4)
a = insertLeft(a, 2)
print(a)
a = insertRight(a, 5)
print(a)
a = insertLeft(a, 4)
print(a)
a = insertRight(a, 1)
print(a)




