import time

waitTime = 4.0 #In seconds
onOff = True

while waitTime > 0.0:
	waitTime = waitTime/2
	print(str(onOff) + " || " + str(waitTime))
	time.sleep(waitTime)
	if onOff:
		onOff = False
	else:
		onOff = True