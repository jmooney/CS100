
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
from pyglet.gl import GL_QUADS

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
shape1 = Shape.Rectangle
shape2 = Shape.getRect(20, 30)
shape2.getTransform().rotate(1)
shape3 = Shape.Shape([-.1, 0, -.1, 1, -.5, 1, -.5, 1.2, .5, 1.2, .5, 1.0, .1, 1.0, .1, 0], [0, 1, 6, 7, 2, 3, 4, 5])

sp1 = ScenePrimitive(sceneGraph.newNode(t=vec(-100, 0)), shape1, color=Color.Red, drawStyle=GL_QUADS)
sp2 = ScenePrimitive(sceneGraph.newNode(t=vec(100, 0), s=vec(20, 30)), shape1, color=Color.Green, drawStyle=GL_QUADS)
sp3 = ScenePrimitive(sceneGraph.newNode(), shape2, color=Color.Purple, drawStyle=GL_QUADS)
sp4 = ScenePrimitive(sp3.getSceneNode().createChild(s=vec(200, 200)), shape3, drawStyle=GL_QUADS)
sp4.setColors(Color.Red*4 + Color.Green*4)


#	Define Funcs

def update(dt):
	sp2.rotate(.01)
	sp3.rotate(.01)

@window.event
def on_draw():
	window.clear()
	renderer.render()


pyglet.clock.schedule(update)
pyglet.app.run()

