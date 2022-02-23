import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap =cv2.VideoCapture(0)
detector=FaceMeshDetector(maxFaces=10)
while True:

    success, img=cap.read()
    img,faces=detector.findFaceMesh(img,draw="False")#add ,draw="False" if you dont want to draw outlines
    z=len(faces)

    if faces:# if there is any face do it
        for user in range(z):#for detect more than 1 person
            face=faces[user]


            pointleft=face[145]
            pointright=face[374]#eye points

            #cv2.line(img, pointleft, pointright, (0, 200, 0), 3)
            #cv2.circle(img,pointleft,5,(255,0,0),cv2.FILLED)
            #cv2.circle(img,pointright, 5, (255, 0, 0), cv2.FILLED)

            w,_=detector.findDistance(pointleft,pointright)#small w = weight in pixels
            #print(w[0])
            W=6.3#big W =weight in real life

            #Finding the Focal Length f (FOR 50 CM DISTANCE)
            #d=50
            #f=(w*d)/W
            #print(f)

            f=750
            d=(W*f)/w#calculated distance

            #print(d)

            cvzone.putTextRect(img,f'distance:{int(d)}cm',(face[10][0]-75,face[10][1]-50),scale=2,thickness=3,colorT=(255,255,255),colorR=(0,0,0))
    cv2.imshow("image",img)
    cv2.waitKey(1)


# approach : Although people's faces are different from each other, certain features are almost the same for every person.
# for example distance between eyes (6,3 cm) , nose distance , iris distance .
# we are using distance between eyes in that project
