
'''

	Project:	CS100
	Title:		EventTest

	Author:		John Mooney
	Date:		1/16/2014

	Description:
		Entry point for running a debug CS100 version - Event
'''

# Imports
import pyglet

from CS100.Subsystems.Tree import Tree
from CS100.Rendering.SceneGraph import SceneGraph
from CS100.Subsystems.EventGraph import EventGraph
from CS100.Space.TransformationGraph import TransformationGraph

from pyglet.graphics import (GL_LINES, GL_TRIANGLES)



#-------------------------------------------------------#	

window 			= pyglet.window.Window(800, 600)
winDimensions 	= [800, 600]

baseTree = Tree()
sceneGraph = SceneGraph(baseTree)
eventGraph = EventGraph(baseTree)
transformationGraph = TransformationGraph(baseTree)


#-------------------------------------------------------#

node2 = baseTree.newNode()
baseTree.debugPrint();	print()
sceneGraph.debugPrint();	print()
transformationGraph.debugPrint();	print()
print('------------------------------------\n')

sceneNode3 = sceneGraph.newNode()
baseTree.debugPrint();	print()
sceneGraph.debugPrint();	print()
transformationGraph.debugPrint();	print()
print('------------------------------------\n')

sn4 = sceneNode3.createChild()
sn5 = sn4.createChild()
baseTree.debugPrint();	print()
sceneGraph.debugPrint();	print()
transformationGraph.debugPrint();	print()
print('------------------------------------\n')


def update(dt):
	pass
	
@window.event
def on_draw():
	window.clear()
	

pyglet.clock.schedule(update)
pyglet.app.run()

