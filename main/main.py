import sys, os
sys.path.append(os.path.abspath(os.path.join('..', '')))

from motioncontrol import MotionControl
from barcode import PiCam
import location_api as loc
import orders_api as order

import atexit

#handles keyboard interrupt
def exit_handler():
    del(control)
    print 'Keyboard Interrupt'

atexit.register(exit_handler)


control = MotionControl()

#check for the source location it its same as the current location
while 1:

    latest_num_orders = len(loc.get_locations) 

    if(latest_num_orders>previous_num_orders):
    #means that a new order has been added now

        new_source = loc.get_locations[0]['source']
        new_destination = loc.get_locations[0]['destination']

        control.move(new_source)
        #add the barcode part here
        sleep(10)

        control.move(new_destination)
        #add the barcode part here
        sleep(10)


    previous_num_orders = latest_num_orders