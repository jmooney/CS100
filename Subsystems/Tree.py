
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
		super().__init__(self)
		self._root = _TreeNode()
	
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def getRoot(self);
		return self._root
	def newNode(self):
		return self._root.createChild()

		
#--------------------------------------------------------#

class _TreeNode(object):
	
	def __init__(self, modifiers = {}, modifierArgs={}):
		super().__init__(self)
		
		self._parent = None
		
		self._children = []
		self._modifiers = {}
		self._modifierCreators = {}
		
		for name, creator in modifierTypes:
			self._addModifier(name, creator, modifierArgs)

			
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def createChild(self):
		return self._createChild(self._modifierTypes.copy())

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

	def _createChild(self, modifierTypes, modifierArgs):
		nn = _TreeNode(modifierTypes, modifierArgs)
		nn.setParent(self)
		self._children.append(nn)
		return nn
		
	def _addModifier(modifierName, creator, modifierArgs):
		self._modifiers[modifierName] = creator(self, **modifierArgs)
		self._modifierCreators[modifierName] = creator
	def _getModifier(modifierName):
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
	def newNode(self):
		return self.getRoot().createChild()
		
		
#--------------------------------------------------------#

class TreeNodeModifier(_TreeNode):

	_modifierName = None
	_modifierCreator = None
	
	def __init__(self, baseNode, **kwArgs):
		self._node = node
		
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
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
		for child in self._children:
			try:
				list.append(child._getModifier(self._modifierName))
			except KeyError:
				continue
				
		return list
		
