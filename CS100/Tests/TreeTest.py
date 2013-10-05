
'''

	Project:	CS100
	Title:		TreeTest

	Author:		John Mooney
	Date:		1/23/2013

	Description:
		Entry point for running a debug CS100 version - Tree
'''

# Imports
import pyglet

import CS100 as Src
from Src.Subsystems.Tree import Tree
from Src.Rendering.SceneGraph2 import SceneGraph
from Src.Space.TransformationGraph2 import TransformationGraph

from pyglet.graphics import GL_LINES, GL_TRIANGLES



#-------------------------------------------------------#	

window 			= pyglet.window.Window(800, 600)
winDimensions 	= [800, 600]

baseTree = Tree()
sceneGraph = SceneGraph(baseTree)
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

