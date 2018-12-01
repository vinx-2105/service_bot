#import positiondetect
#pos=positiondetect.position()
#print pos

#arr = ['S','L','L','R']
arr = ['L','R']
import motioncontrol2 as cont
controller=cont.Control()
controller.move(arr)
