
'''

	Project:	CS100
	Title:		CollisionTest

	Author:		John Mooney
	Date:		10/13/2013

	Description:
		Entry point for running a debug CS100 version - Collision Test
'''

# Imports
import pyglet
from pyglet.gl import (GL_QUADS, GL_TRIANGLE_FAN)

from CS100.Math import Shape
from CS100.Rendering import Color
from CS100.Math.Vector import vec
from CS100.Subsystems.Tree import Tree
from CS100.Rendering.Renderer import Renderer
from CS100.Rendering.SceneGraph import SceneGraph
from CS100.Rendering.ScenePrimitive import ScenePrimitive
from CS100.Space.TransformationGraph import TransformationGraph


from CS100.Physics.Collision.Collider import Collider
from CS100.Physics.Collision.CollisionWorld import CollisionWorld


#-------------------------------------------------------#	


#	Set up Window/Rendering
window 			= pyglet.window.Window(800, 600)
winDimensions 	= [800, 600]

baseTree = Tree()
sceneGraph = SceneGraph.activeGraph = SceneGraph(baseTree)
transformGraph = TransformationGraph.activeGraph = TransformationGraph(baseTree)

renderer = Renderer(winDimensions, sceneGraph)


#	Create Objects

#	Define Funcs

def update(dtSecs):
	pass

@window.event
def on_draw():
	window.clear()
	renderer.render()


pyglet.clock.schedule(update)
pyglet.app.run()

