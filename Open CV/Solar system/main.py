import cv2, cvzone, math, random
import mediapipe as mp

class Planets():
	planet = None
	angle = None
	speed = None
	distance = None
	xx = None
	yy = None
	ox = None
	oy = None
	image = None
	w = None
	h = None
	c = None

	def __init__(self,distance,planet):
		self.angle = random.randint(0,259)
		self.speed = 0.10
		self.distance = distance
		self.planet = planet

		if planet == 'sun':
			self.image = cv2.imread('Planets/small/sun.png', cv2.IMREAD_UNCHANGED)
			self.w,self.h,self.c = self.image.shape
		if planet == 'earth':
			self.image = cv2.imread('Planets/small/Earth.png', cv2.IMREAD_UNCHANGED)
			self.w,self.h,self.c = self.image.shape
		if planet == 'jupiter':
			self.image = cv2.imread('Planets/small/Jupiter.png', cv2.IMREAD_UNCHANGED)
			self.w,self.h,self.c = self.image.shape
		if planet == 'pluto':
			self.image = cv2.imread('Planets/small/Pluto.png', cv2.IMREAD_UNCHANGED)
			self.w,self.h,self.c = self.image.shape
		if planet == 'saturn':
			self.image = cv2.imread('Planets/small/Saturn.png', cv2.IMREAD_UNCHANGED)
			self.w,self.h,self.c = self.image.shape

	def update(self,ox,oy):
		if self.planet == 'sun':
			self.xx = ox
			self.yy = oy
		else:
			self.xx = int(math.cos(self.angle)*self.distance) + ox
			self.yy = int(math.sin(self.angle)*self.distance) + oy
			self.angle += self.speed


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)
cap.set(3,1920)
cap.set(4,1080)

def findHands(img, draw=True):
	imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	result = hands.process(imgRGB)

	if result.multi_hand_landmarks:
		for handLms in result.multi_hand_landmarks:
			if draw:
				mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
	return img, result


def findPosition(img,res, handNo=0, draw=True):
	result = res
	lmlist = []
	if result.multi_hand_landmarks:
		myHand = result.multi_hand_landmarks[handNo]
		for id, lm in enumerate(myHand.landmark):
			h,w,c = img.shape
			cx,cy = int(lm.x*w), int(lm.y*h)
			lmlist.append([id,cx,cy])
	return  lmlist


cir = Planets(distance=50,planet='sun')
cir2 = Planets(distance=80,planet='earth')
cir3 = Planets(distance=120,planet='saturn')
cir4 = Planets(distance=170,planet='jupiter')
planets_list = [cir,cir2,cir3,cir4]

while True:
	success, img = cap.read()
	img, res = findHands(img,draw=True)
	lmList = []
	lmList = findPosition(img,res)

	if lmList:
		for i in planets_list:
			i.update(int(lmList[8][1]-2.5),int(lmList[8][2]-2.5))

			# img = cvzone.overlayPNG(img,i.image,[int(i.xx-i.w/2),int(i.yy-i.h/2)])
			if 610 > i.xx > 30:
				if 450 > i.yy > 30:
					img = cvzone.overlayPNG(img,i.image,[int(i.xx-i.w/2),int(i.yy-i.h/2)])

	cv2.imshow("image",img)
	cv2.waitKey(1)