from Phidget22.Phidget import *
from Phidget22.Devices.DigitalInput import *
import time
start_time = time.time()

def onStateChange(self, state):
	global start_time
	print("State: " + str(state))
	first = time.time()
	if state == 1:
		start_time = time.time()
	else:
		first = time.time() 


		netTime = first - start_time 
		speedMps = ((0.219075 / netTime))
		print(speedMps,"m/s")
		print(speedMps*3.6,"kmh")

digitalInput0 = DigitalInput()
digitalInput0.setOnStateChangeHandler(onStateChange)


digitalInput0.openWaitForAttachment(5000)


