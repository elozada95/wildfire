#grabs a path, slices the files(asuming images) and stores it in a folder
#call using: python split_image.py -p PATH_OF_EXTRACTION

#list of liberies used in this proyect
#parses arguments from the cli
import argparse 
#where all the magic happens
import cv2
import numpy as np

#open directories libraries
from os import listdir
from os.path import isfile, join


#slices an image based on the vertical and horizonal slices received.
#image is the image to be sliced
#externalCount its a counter for the current image being sliced
def sliceImage(externalCount,image,verticalSlices,horizontalSlices):
	#counts the slice numbers
	internalCount = 0
	#obtains the height and width of the image
	(imgHeight, imgWidth) = image.shape[:2]
	
	#obtains the step of the height and width. "//" divides and floors the result
	xStep = imgWidth//horizontalSlices
	yStep = imgHeight//verticalSlices
	
	#range is range(start,stop,step). step is the displacement
	for x in range(0,imgWidth,xStep):
		for y in range(0,imgHeight,yStep):
			internalCount = internalCount + 1
			#obtains the current square. From current y to current y + step. with x too
			roi = image[y:y+yStep,x:x+xStep]
			#set name of img
			img_name = "./img_out/image" + str(externalCount) + "part" + str(internalCount) + ".png"
			#saves image with "img_name" file name
			cv2.imwrite(img_name,roi)


# ../img/fire
# ../img/not_fire
# ../img/smoke
#parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True,help = "Path to the image")
#ap.add_argument("-hs", "--horizontalSlices", required = True, help = "Horizontal slices")
#ap.add_argument("-vs", "--verticalSlices", required = True, help = "Type of kernel")
ap.add_argument("-p","--extractionPath",required = True, help = "Path to the list of images")
args = vars(ap.parse_args())
#get the path
path = args["extractionPath"]
#and casts them to data
#image = cv2.imread(args["image"])
#horizontalSlices = int(args["horizontalSlices"])
#verticalSlices = int(args["verticalSlices"])

#call magic function that stores values
#sliceImage(image,verticalSlices,horizontalSlices)

#get files from path
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

count = 0 #external path
for fileName in onlyfiles:
	if fileName != ".DS_Store":
		count = count + 1
		fullPath = path+"/"+fileName
		image = cv2.imread(fullPath)
		sliceImage(count,image,4,4)


#IGNORE THIS
#def features(image, kernel_size):
#	(hImg, wImg) = image.shape[:2]
#	pad = (kernel_size - 1) // 2
#	print("height")
#	print(hImg)
#	print("range of height")
#	print(range(pad, hImg - pad, kernel_size))
#	print("width")
#	print(wImg)
#	print("range of width")
#	print(range(pad, wImg - pad, kernel_size))
#	#loop over the input image, sliding the kernel across each
#	#(x,y) coordinate from left-to-right and top-to-bottom
#	for y in range(pad, hImg - pad, kernel_size):
#		for x in range(pad, wImg - pad, kernel_size):
#			#extract the ROI of the image around the current (x,y) pixel
#			roi = image[y-pad:y+pad+1,x-pad:x+pad+1]
#			#cv2.imshow("image"+str(y)+str(x),roi)
#			img_name = "./img_out/image"+str(y)+str(x) +".png"
#			cv2.imwrite(img_name,roi)
#			#perform a feature extraction
#			#mean = np.mean(roi)
#			#median = np.median(roi)
#			#print(mean,",",median)
#
#
##range (start stop step)
##start at zero. stop at limit, step is 
#

#how to call scrypt
#python split_image.py -i 1.jpg -hs 4 -vs 4


#python split_image.py -i ./test_imgs/2.jpg -hs 4 -vs 4




#IGNORE THIS TOO

#kernel_size = int(args["kernel"])

#converts image to gray
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#extracts rgb of image
#(B, G, R) = cv2.split(image)

#writes image
#cv2.imwrite("gray.png",gray)

#draws line in image
#cv2.line(image,(width*i,0),(width*i,image.shape[0]-1),(0,255,0))
#image -> grey -> image

##range (start stop step)
##start at zero. stop at limit, step is 

#r.g.b -> b,w -> r.g.b(white and black)
#grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#normal = cv2.cvtColor(grey, cv2.COLOR_GRAY2BGR)