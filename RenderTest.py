
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

shape1 = Shape.Circle
shape2 = Shape.getRect(50, 70)

shape3 = Shape.getRect(50, 70)
shape3.removeTransform()
shape3.setTransform(tempNode.createChild())

shape4 = Shape.Shape([-.1, 0, -.1, 1, -.5, 1, -.5, 1.2, .5, 1.2, .5, 1.0, .1, 1.0, .1, 0], [0, 1, 6, 7, 2, 3, 4, 5])
shape5 = Shape.Shape([-.29, 0, -.29, 1, -.15, 1, -.15, 0, -.15, .45, -.15, .55, .15, .55, .15, .45, .15, 0, .15, 1, .3, 1, .3, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

sp1 = ScenePrimitive(sceneGraph.newNode(t=vec(-250, 0), s=vec(50, 50)), shape1, color=Color.Red, drawStyle=GL_TRIANGLE_FAN)
sp2 = ScenePrimitive(sceneGraph.newNode(t=vec(-100, 0), s=vec(50, 50)), shape1, color=Color.Green, drawStyle=GL_TRIANGLE_FAN)
sp3 = ScenePrimitive(sceneGraph.newNode(t=vec(100, 0)), shape2, color=Color.Purple, drawStyle=GL_QUADS)
sp4 = ScenePrimitive(tempNode, shape3, color=Color.Orange, drawStyle=GL_QUADS)

sp5 = ScenePrimitive(sceneGraph.newNode(t=vec(0, 200), s=vec(50, 50)), shape4, drawStyle=GL_QUADS)
sp5.setColors(Color.Blue*4 + Color.Teal*4)

sp6 = ScenePrimitive(sceneGraph.newNode(t=vec(-200, -200), s=vec(30, 30)), shape4, color=Color.Purple, drawStyle=GL_QUADS)
sp7 = ScenePrimitive(sceneGraph.newNode(t=vec(200, -200), s=vec(50, 50)), shape5, color=Color.Pink, drawStyle=GL_QUADS)

countdown = 5


#	Define Funcs

def update(dtSecs):
	sp3.scale2f(1.001, 1.001)
	sp4.scale2f(1.001, 1.001)
	
	global countdown
	if countdown > 0:
		countdown-=dtSecs
	elif countdown < 0:
		sp6.attachShape(shape5)
		sp7.attachShape(shape4)
		countdown = 0
		

@window.event
def on_draw():
	window.clear()
	renderer.render()


pyglet.clock.schedule(update)
pyglet.app.run()

