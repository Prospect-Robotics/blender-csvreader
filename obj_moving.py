import bpy
import csv


#helper functions

def setpos(name,x,y,z):
    bpy.data.objects[name].location.x=x
    bpy.data.objects[name].location.y=y
    bpy.data.objects[name].location.z=z

def setrot(name,x,y,z):
    bpy.data.objects[name].rotation_euler.x = x
    bpy.data.objects[name].rotation_euler.y = y
    bpy.data.objects[name].rotation_euler.z = z

def setplaybackspeed(fps):
    bpy.context.scene.render.fps = fps
    bpy.context.scene.render.fps_base = 1


#csv reading
csvfile = open("C:\\Users\\2adri\\OneDrive\\Documents\\blenderCsvLogStuff\\data.csv","rt")
csvreader = csv.reader(csvfile)
csvhead = {}
csvbody = []

#json reading
jsonfile = open("C:\\Users\\2adri\\OneDrive\\Documents\\blenderCsvLogStuff\\data_usage.json","rt")
jsondata = json.load(jsonfile)

for i,elem in enumerate(next(csvreader)):
    csvhead[elem]=i

for row in csvreader:
    thisrow = []
    for elem in row:
        thisrow.append(float(elem))
    csvbody.append(thisrow)

def get_csv_value(name,row):
    return csvbody[row][csvhead[name]]


#scene setup
scene = bpy.context.scene
scene.frame_start = 0
scene.frame_end = len(csvbody)-1




#callback setup
def frame_change_callback(scene):
    frame = scene.frame_current
    if (scene.frame_start <= frame) and (frame <= scene.frame_end):
        print('frame',frame,csvbody[frame])
    else:
        print("frame out of range")
        return
    setpos("Cube",get_csv_value("x",frame),get_csv_value("y",frame),get_csv_value("z",frame))
                


bpy.app.handlers.frame_change_post.append(frame_change_callback)
