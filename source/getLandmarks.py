#coding=utf8
import cv2  
import dlib  
import numpy  
import sys  
  
root = 'E:/face_rating/my_face_rating/'
PREDICTOR_PATH = root +  "data/shape_predictor_68_face_landmarks.dat"  
  
#1.使用dlib自带的frontal_face_detector作为我们的人脸提取器  
detector = dlib.get_frontal_face_detector()  
 
#2.使用官方提供的模型构建特征提取器  
predictor = dlib.shape_predictor(PREDICTOR_PATH)  
  
class NoFaces(Exception):  
    pass  
  
im = cv2.imread(root + "image/test.jpg")  

#3.使用detector进行人脸检测 rects为返回的结果  
rects = detector(im,1)  
  
#4.输出人脸数，dets的元素个数即为脸的个数  
if len(rects) >= 1:  
    print("{} faces detected".format(len(rects)))  
      
if len(rects) == 0:  
    raise NoFaces  
	
f = open(root + 'data/landmarks.txt','w')
for i in range(len(rects)):  
      
    #5.使用predictor进行人脸关键点识别  
    landmarks = numpy.matrix([[p.x,p.y] for p in predictor(im,rects[i]).parts()])  
    im = im.copy()  
  
    #使用enumerate 函数遍历序列中的元素以及它们的下标  
    for idx,point in enumerate(landmarks):  
        pos = (point[0,0],point[0,1])  
        
        f.write(str(point[0,0]))
        f.write(',')
        f.write(str(point[0,1]))
        f.write(',')
        #cv2.putText(im,str(idx),pos,  
                    #fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,  
                    #fontScale=0.4,  
  
                    #color=(0,0,255))  
        #6.绘制特征点  
        cv2.circle(im,pos,3,color=(0,255,0))  
    f.write('\n')	
print "landmarks,get!"	
cv2.namedWindow("im",2)  
cv2.imshow("im",im)  
cv2.waitKey(1000)  
