
'''

	Project:	CS100
	Title:		SpriteTest

	Author:		John Mooney
	Date:		10/13/2013

	Description:
		Entry point for running a debug CS100 version - Rendering Test
'''

# Imports
import pyglet
from pyglet.gl import (GL_QUADS, GL_TRIANGLE_FAN)

from CS100.Rendering import Shape
from CS100.Math.Vector import vec
from CS100.Rendering import Color
from CS100.Subsystems.Tree import Tree
from CS100.Rendering.Renderer import Renderer
from CS100.Rendering.SceneGraph import SceneGraph
from CS100.Rendering.ScenePrimitive import ScenePrimitive
from CS100.Space.TransformationGraph import TransformationGraph


#-------------------------------------------------------#	


#	Set up Window/Rendering
window 			= pyglet.window.Window(800, 600)
winDimensions 	= [800, 600]

baseTree = Tree()
sceneGraph = SceneGraph.activeGraph = SceneGraph(baseTree)
transformGraph = TransformationGraph.activeGraph = TransformationGraph(baseTree)

renderer = Renderer(winDimensions, sceneGraph)


#	Create Objects
tempNode = sceneGraph.newNode(t=vec(250, 0))

shape1 = Shape.getRect(40, 70)

sp1 = ScenePrimitive(sceneGraph.newNode(t=vec(-175, 0)), shape1, color=Color.Green, drawStyle=GL_QUADS)
sp2 = ScenePrimitive(sp1.getSceneNode().createChild(t=vec(-100, -50)), shape1, color=Color.Blue, drawStyle=GL_QUADS)
sp3 = ScenePrimitive(sp1.getSceneNode().createChild(t=vec(100, -50)), shape1, color=Color.Blue, drawStyle=GL_QUADS)

sp4 = ScenePrimitive(sceneGraph.newNode(t=vec(175, 0)), shape1, color=Color.Red, drawStyle=GL_QUADS)
sp5 = ScenePrimitive(sp4.getSceneNode().createChild(t=vec(-100, -50)), shape1, color=Color.Yellow, drawStyle=GL_QUADS)
sp6 = ScenePrimitive(sp4.getSceneNode().createChild(t=vec(100, -50)), shape1, color=Color.Yellow, drawStyle=GL_QUADS)

sp1.getSceneNode().batchSubTree()

#	Define Funcs

def update(dtSecs):
	sp1.translate2f(0, 1)
	sp4.translate2f(0, 1)
	

@window.event
def on_draw():
	window.clear()
	renderer.render()


pyglet.clock.schedule(update)
pyglet.app.run()

