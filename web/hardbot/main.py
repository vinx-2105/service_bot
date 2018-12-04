#import positiondetect
#pos=positiondetect.position()
#print pos

arr = ['L','R','L','R']
import motioncontrol2 as cont
controller=cont.Control()
controller.move(arr)
