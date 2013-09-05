
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
		self._root = _Node()
	
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def getRoot(self);
		return self._root
	def newNode(self):
		return self._root.createChild()

		
		
#--------------------------------------------------------#

class _Node(object):
	
	def __init__(self, modifierTypes = []):
		super().__init__(self)
		
		self._parent = None
		self._children = []
		
		self._modifiers = {}
		for modifierType in modifierTypes:
			self._modifiers[modifierType[0]] = modifierType[1](self)

			
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def setParent(self, p):
		if self._parent:
			self._parent._children.remove(self)
		self._parent = p
		self._parent._children.append(self)
		
	def createChild(self):
		modifierList = [(key, val[1]) for key, val in self._modifiers.iteritems()]
		
		nn = _Node(modifierList)
		nn.setParent(self)
		self._children.append(nn)
		return nn
		
