import bpy
import csv


#helper functions

def setpos(name,x,y,z):
    bpy.data.objects[name].location.x=x
    bpy.data.objects[name].location.y=y
    bpy.data.objects[name].location.z=z




#csv reading
csvfile = open("C:\\Users\\2adri\\OneDrive\\Documents\\blenderCsvLogStuff\\data.csv","rb")
csvreader = csv.reader(csvfile,delimeter=' ')
for row in csvreader:
    print(','.join(row))


#scene setup
scene = bpy.context.scene
scene.frame_start = 0
scene.frame_end = 100



#callback setup

def frame_change_callback(scene):
    frame = scene.frame_current
    setpos("Cube",((frame/scene.frame_end)*2)-1,0,0)

bpy.app.handlers.frame_change_post.append(frame_change_callback)

