# Script to renmane and resize files for machine learning 

import os
import cv2
import glob

newPath='./symbols/MachineLearning/'
quadrants=['LowerLeftQuadrant-Thousands','LowerRightQuadrant-Hundreds','UpperLeftQuadrant-Tens','UpperRightQuadrant-Ones']
path='./symbols/'

if not os.path.isdir( newPath ) :
    os.mkdir( newPath )  # make sure the directory exists

for i in range(len(quadrants)):
    if not os.path.isdir( newPath+quadrants[i] ) :
        os.mkdir(newPath+quadrants[i] )  # make sure the directory exists

for quad in range(len(quadrants)): 
    for i, file in enumerate(glob.glob(path+quadrants[quad] + '/*.PNG')):
        image = cv2.imread(file)
        half = cv2.resize(image, (0, 0), fx=0.1, fy=0.1)
        print("resized image: ",file)
        print("saved image to: ",newPath+quadrants[quad]+'/'+os.path.basename(file))
        cv2.imwrite(newPath+quadrants[quad]+'/'+os.path.basename(file),half)