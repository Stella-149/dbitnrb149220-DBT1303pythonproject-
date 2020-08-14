#hello
'''please note that for any security system ,input of details of persons is key'''

visitor =input("Kindly enter your name: ")

print(" Hi there "+ visitor)

Intention=input("Kindly state he nature of your visit", + visitor)

print(" thank you for coming to "+ Intention)

How_long=input("Dear " + visitor + "how long will you be " + Intention+)

print("you will be expected to be done by "+How_long+"incase of extension ,kindly let us know")

# camera


#1st we need to have a cv2 file imported for the below code to work

'''Disclaimer'''# as i was not in the posesionm of cctv cameras ,below code goes to om=nly verify theory part.

import cv2


#capture from camera at location 0
cap = cv2.VideoCapture(0)
#set the width and height, and UNSUCCESSFULLY set the exposure time
cap.set(3,1280)
cap.set(4,1024)
cap.set(15, 0.1)

while True:
    ret, img = cap.read()
    cv2.imshow("input", img)
    #cv2.imshow("thresholded", imgray*thresh2)

    key = cv2.waitKey(10)
    if key == 27:
        break


cv2.destroyAllWindows()
cv2.VideoCapture(0).release()


