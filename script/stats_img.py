#opens a file path, fetches the files(asuming images) and process some statistical data. Name of the file asumed to be a specific format defined below
#file path should be specified but currently hardcoded
#call using: python stats_img.py 

#list of liberies used in this proyect
import argparse
import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

#open directories libraries
from os import listdir
from os.path import isfile, join


def getStats(image, image_name, image_status):
        #RGB ARRAY
        (B, G, R) = cv2.split(image)
        R = R.flatten() #Returns matrix of only 1 channel. we flatten it to one dimentional array
        G = G.flatten() #Returns matrix of only 1 channel. we flatten it to one dimentional array
        B = B.flatten() #Returns matrix of only 1 channel. we flatten it to one dimentional array
        #mean of red
        redMean = np.mean(R)
        #mean of green
        greenMean = np.mean(G)
        #mean of blue
        blueMean = np.mean(B)
        #mean of rgb(gray)
        imgMean = np.mean(image)

        #std dev of red
        redStd = np.std(R)
        #std dev of green
        greenStd = np.std(G)
        #std dev of blue
        blueStd = np.std(B)
        #std dev of rgb(gray)
        imgStd = np.std(image)

        #variation of red
        redVariation = sp.variation(R)
        #variation of green
        greenVariation = sp.variation(G)
        #variation of blue
        blueVariation = sp.variation(B)
        #variation of rgb(gray)
        imgVariation = sp.variation(image.flatten())


        #entropy of red
        redEntropy = sp.entropy(R)
        #entropy of green
        greenEntropy = sp.entropy(G)
        #entropy of blue
        blueEntropy = sp.entropy(B)
        #entropy of rgb(gray)
        imgEntropy = sp.entropy(image.flatten())

        #inertia -> moment
        #moment of red
        redMoment = sp.moment(R)
        #moment of green
        greenMoment = sp.moment(G)
        #moment of blue
        blueMoment = sp.moment(B)
        #moment of rgb(gray)
        imgMoment = sp.moment(image.flatten())

        #kurtosis of red
        redKurtosis = sp.kurtosis(R)
        #kurtosis of green
        greenKurtosis = sp.kurtosis(G)
        #kurtosis of blue
        blueKurtosis = sp.kurtosis(B)
        #kurtosis of rgb(gray)
        imgKurtosis = sp.kurtosis(image.flatten())

        #skewness of red
        redSkew = sp.skew(R)
        #skewness of green
        greenSkew = sp.skew(G)
        #skewness of blue
        blueSkew = sp.skew(B)
        #skewness of rgb(gray)
        imgSkew = sp.skew(image.flatten())

        #appends everything to this array
        data = []
        #first we append the name of the image
        data.append(image_name)

        #then the data
        data.append(redMean)
        data.append(greenMean)
        data.append(blueMean)
        data.append(imgMean)

        data.append(redStd)
        data.append(greenStd)
        data.append(blueStd)
        data.append(imgStd)

        data.append(redVariation)
        data.append(greenVariation)
        data.append(blueVariation)
        data.append(imgVariation)

        data.append(redEntropy)
        data.append(greenEntropy)
        data.append(blueEntropy)
        data.append(imgEntropy)

        data.append(redMoment)
        data.append(greenMoment)
        data.append(blueMoment)
        data.append(imgMoment)

        data.append(redKurtosis)
        data.append(greenKurtosis)
        data.append(blueKurtosis)
        data.append(imgKurtosis)

        data.append(redSkew)
        data.append(greenSkew)
        data.append(blueSkew)
        data.append(imgSkew)

        #then the status
        data.append(image_status)

        #returns it
        return data

#currently hardcoded, should define path on cli
mypath = "../classifications/smoke/"
#get files 
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for fileName in onlyfiles:
    if fileName != ".DS_Store":
        #obtain the name of the image and its status. Asuming the format of the filename to be "something_status.fileformat" 
        # where something is the name of the file
        # status is the status of the image: fire/noFire/smoke
        # fileFormat is the file format...png, jpg, whatever
        subImgName = fileName.split(".")[0]
        image = cv2.imread(mypath+fileName)
        print(getStats(image,subImgName,"smoke"))



#parse the arguments
#   ap = argparse.ArgumentParser()
#   ap.add_argument("-i", "--image", required = True,help = "Path to the image")
#   args = vars(ap.parse_args())
#   #and casts them to data
#   imgName = args["image"]
#   image = cv2.imread(imgName)
#   arrStr = imgName.split("/")[2].split("_")
#   fileName = arrStr[0]
#   status = arrStr[1].split(".")[0]




