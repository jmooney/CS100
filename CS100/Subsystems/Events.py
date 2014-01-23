
'''

	Project:	CS100
	Title:		Events

	Author:		John Mooney
	Date:		1/20/2013

	Description:
		Allows for event listening/management for objects in the world
'''

# Imports
import queue


#------------------------------------------------------#
#	Event
class Event(object):
	
	def __init__(self, source, priority, description, data):
		super().__init__()
		self.source = source
		self.priority = priority
		self.description = description
		self.data = data
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def __lt__(self, e):
		return self.priority < e.priority
		
		
#------------------------------------------------------#
#	EventSource
class EventSource(object):

	def __init__(self):
		super().__init__()
		self._listeners = []
			
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

	def addListener(self, listener):
		self._listeners.append(listener)
	def removeListener(self, listener):
		self._listeners.remove(listener)
		
	def sendEvent(self, priority, description, data):
		e = Event(self, priority, description, data)
		for listener in self._listeners:
			listener.receiveEvent(e)
			
		
#------------------------------------------------------#
#	EventListener
class EventListener(object):

	def __init__(self):
		super().__init__()
		self._eventQueue = queue.PriorityQueue()
		self._eventHandlers = {}
		
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def receiveEvent(self, event):
		self._eventQueue.put_nowait(event)
		
	def processEvent(self, event):
		try:
			self._eventHandlers[event.description](event.data)
		except(KeyError):
			pass
	
	def processEvents(self):
		while not self._eventQueue.empty():
			try:
				self.processEvent(self._eventQueue.get_nowait())
			except queue.Empty:
				return
		
		
