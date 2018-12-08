#import positiondetect
#pos=positiondetect.position()
#print pos

#arr = ['S','L','L','R']
arr = ['R','L','R']
import motioncontrol3 as cont
controller=cont.Control()
#controller.takeUTurn()
controller.move(arr)
