
'''

	Project:	CS100
	Title:		ScenePrimitives

	Author:		John Mooney
	Date:		1/23/2013

	Description:
		Entry point for running a debug CS100 version
'''

# Imports
import pyglet
import sys
import os

'''		Set Search Directory	'''
for root, direcs, files in os.walk(os.getcwd()):
	for direc in direcs:
		sys.path.append(os.path.join(root, direc))


# Local Imports
import TransformationGraph
import DebugDrawingManager
import Color

from CollisionPrimitives import *
from Vector import vec

#-------------------------------------------------------#
	

window 	= pyglet.window.Window()
tg 		= TransformationGraph.tg = TransformationGraph.TransformationGraph()
ddm 	= DebugDrawingManager.ddm = DebugDrawingManager.DebugDrawingManager()

cr1 = CollisionRect(t=tg.newTransform(t=vec(200, 200)), w=200, h=185)
cr2 = CollisionRect(t=tg.newTransform(t=vec(400, 250)), w=15, h=400)

cr1Color = None
cr2Color = None

pyglet.gl.glPolygonMode(pyglet.gl.GL_FRONT_AND_BACK, pyglet.gl.GL_LINE)
pyglet.gl.glPointSize(5)

def update(dt):
	ddm.update(dt)
	
	cr1.update(dt)
	cr2.update(dt)
	
	cr2.rotate(.001)
	
	if(cr1.testCollision(cr2)):
		cr1Color = Color.Red
		cr2Color = Color.White
	else:
		cr1Color = Color.Green
		cr2Color = Color.Purple
	
	ddm.drawRect(None, cr1._width, cr1._height, t=cr1.getTransform(), color=cr1Color)
	ddm.drawRect(None, cr2._width, cr2._height, t=cr2.getTransform(), color=cr2Color)

@window.event
def on_draw():
	window.clear()	
	ddm.draw()
	

pyglet.clock.schedule(update)
pyglet.app.run()
