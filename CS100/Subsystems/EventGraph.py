
'''

	Project:	CS100
	Title:		EventGraph

	Author:		John Mooney
	Date:		1/16/2013

	Description:
		Allows for event listening/management for child/parent nodes within a tree-structure
'''


# Imports
from queue import PriorityQueue, Empty
from CS100.Subsystems.Tree import TreeModifier, TreeNodeModifier


#------------------------------------------------------#
#	SceneGraph

class EventGraph(TreeModifier):

	activeGraph = None
	
	def __init__(self, baseTree):
		self._nodeModifierName = 'EventNode'
		self._nodeModifierCreator = EventNode
		super().__init__(baseTree)
		


#------------------------------------------------------#
#	EventNode

class EventNode(TreeNodeModifier):

	def __init__(self, baseNode):
		super().__init__(baseNode)
		self._modifierName = 'EventNode'
		self._modifierCreator = EventNode
		
		self._eventQueue = PriorityQueue()

		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def getEvent(self):
		return self._eventQueue.get(False)
	def addEvent(self, event):
		self._eventQueue.put(event)
	def sendEvent(self, event):
		self.getParent().addEvent(event)
	def broadcastEvent(self, event):
		p = self.getParent()
		if p is not None:
			p.addEvent(event)
			self.getParent().broadcastEvent(event)

			
			
#------------------------------------------------------#
#	EventListener

class EventListener(object):

	def __init__(self, listenerNode = None):
		super().__init__()
		self._listener = listenerNode
		
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def processEvent(self, event):
		pass
	def processEvents(self):
		while True:
			try:
				self.processEvent(self._listener.getEvent())
			except (Empty):
				return
	
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def addEvent(self, event):
		self._listener.addEvent(event)
	def sendEvent(self, event):
		self._listener.sendEvent(event)
	def broadcastEvent(self, event):
		self._listener.broadcastEvent(event)
	

	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
		
	def setListener(self, listener):
		self._listener = listener
	def getListener(self):
		return self._listener

