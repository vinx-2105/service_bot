#import positiondetect
#pos=positiondetect.position()
#print pos
from time import sleep

#arr = ['S','L','L','R']
arr = ['L','R','L','L']
arr2 = ['R','L','R']
import MotionControl as cont
print("1")
controller=cont.MotionControl()
#controller.takeUTurn()
controller.move(arr)
sleep(2)
controller.move(arr2)

