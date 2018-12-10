import sys, os
sys.path.append(os.path.abspath(os.path.join('..', '')))

import MotionControl
import PiCam
import location_api as loc
import orders_api as orders
import getDirections as getdir
import atexit
from time import sleep

#handles keyboard interrupt
def exit_handler():
    #del(control)
    print ('Ending')

atexit.register(exit_handler)


control = MotionControl.MotionControl()

new_source = orders.get_orders()[0]['source']
new_destination = orders.get_orders()[0]['destination']



print(new_source)
print(len(orders.get_orders()))

#control.move(['L','R','S','S'])
#check for the source location it its same as the current location


previous_num_orders = len(orders.get_orders()) 
while 1:

    latest_num_orders = len(orders.get_orders()) 
    print(str(latest_num_orders) + "  " +str(latest_num_orders))
    if(latest_num_orders>previous_num_orders and latest_num_orders>1):
    #means that a new order has been added now
        print("working")
        new_source = orders.get_orders()[latest_num_orders-1]['source']
        new_destination = orders.get_orders()[latest_num_orders-1]['destination']

        old_source = orders.get_orders()[latest_num_orders-2]['source']
        old_destination = orders.get_orders()[latest_num_orders-2]['destination']
	
        print(old_source + "========")
        print(old_destination + "========")
     
        old_source_path = loc.get_path(old_source)
        old_destination_path = loc.get_path(old_destination)
	
        print(old_source_path + "    old s path  ========")
        print(old_destination_path + "  old dest path  ========")

        new_source_path = loc.get_path(new_source)
        new_destination_path = loc.get_path(new_destination)

        print(new_source_path+"new sourc path")
        print(new_destination_path+"new dest path")
        cur_path = getdir.getDirections(old_destination_path, new_source_path)
        print(1)
        print(cur_path)
        print(new_source_path)
        print(new_destination_path)
        #print("source-" + new_source + "new_destination" + new_destination)
        control.move(cur_path)

        cur_path = getdir.getDirections(new_source, new_destination)
        print(2)
        print(cur_path)
        
        #add the barcode part here
        sleep(1)

        control.move(cur_path)
        #add the barcode part here
        sleep(1)


    previous_num_orders = latest_num_orders

