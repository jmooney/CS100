
'''

	Author: John Mooney
	Date:	9/4/2013
	
	Description:
		Provides a common interface for building/using a tree data structure
	
'''

# Imports


#--------------------------------------------------------#

class Tree(object):
	
	def __init__(self):
		super().__init__()
		self._root = _TreeNode()
	
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def getRoot(self):
		return self._root
	def newNode(self):
		return self._root.createChild()
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def debugPrint(self, node=None, tabs=''):
		if not node:
			node = self.getRoot()
			
		print(tabs + str(type(node)))
		for child in node.getChildren():
			self.debugPrint(child, tabs+'\t')

		
#--------------------------------------------------------#

class _TreeNode(object):
	
	def __init__(self, modifierCreators = {}, modifierArgs={}):
		super().__init__()
		
		self._parent = None
		
		self._children = []
		self._modifiers = {}
		self._modifierCreators = modifierCreators
		
		for name, creator in modifierCreators.items():
			self._addModifier(name, creator, modifierArgs)

			
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def createChild(self):
		return self._createChild(self._modifierCreators.copy(), {})

	def setParent(self, p):
		if self._parent:
			self._parent._children.remove(self)
		self._parent = p
		self._parent._children.append(self)
		
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def getParent(self):
		return self._parent
	def getChildren(self):
		return self._children
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

	def _createChild(self, modifierCreators, modifierArgs):
		nn = _TreeNode(modifierCreators, modifierArgs)
		nn.setParent(self)
		return nn
		
	def _addModifier(self, modifierName, creator, modifierArgs = {}):
		self._modifiers[modifierName] = creator(self, **modifierArgs)
		self._modifierCreators[modifierName] = creator
	def _getModifier(self, modifierName):
		return self._modifiers[modifierName]


#--------------------------------------------------------#

class TreeModifier(Tree):
	
	_nodeModifierName = None
	_nodeModifierCreator = None

	def __init__(self, baseTree):
		self._tree = baseTree
		self._tree.getRoot()._addModifier(self._nodeModifierName, self._nodeModifierCreator)
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def getRoot(self):
		return self._tree._root._getModifier(self._nodeModifierName)
	def newNode(self, **modifierArgs):
		return self.getRoot().createChild(**modifierArgs)
		
		
#--------------------------------------------------------#

class TreeNodeModifier(_TreeNode):

	_modifierName = None
	_modifierCreator = None

	def __init__(self, baseNode, **kwArgs):
		self._node = baseNode


	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def asType(self, modifierTypeName):
		return self._node._getModifier(modifierTypeName)
	
	
	def setParent(self, p):
		self._node.setParent(p)
	def createChild(self, **modifierArgs):
		return self._node._createChild({self._modifierName:self._modifierCreator}, modifierArgs)._getModifier(self._modifierName)
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def getParent(self):
		if self._node.getParent():
			return self._node.getParent()._getModifier(self._modifierName)
		return None
		
	def getChildren(self):
		list = []
		for child in self._node.getChildren():
			try:
				list.append(child._getModifier(self._modifierName))
			except KeyError:
				continue
				
		return list
		
