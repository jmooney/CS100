
'''

	Author: John Mooney
	Date:	5/28/2013
	
	Description:
		Provides a common interface for building/using a tree data structure
	
'''

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
	
class TreeModifier(Tree):
	
	def __init__(self, base):
		self._base = base
			
	def getRoot(self);
		return self._base.getRoot()

		

#--------------------------------------------------------#

class _Node(object):

	def __init__(self):
		super().__init__(self)
		self._parent = None
		self._children = []
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''	
	def createChild(self):
		nn = _Node()
		self._children.append(nn)
		nn.setParent(self)
		return nn
		
	def setParent(self, p):
		self._parent = p
