# predict-facial-attractiveness
Using OpenCV and Dlib to predict facial attractiveness.

Download the shape_predictor_68_face_landmarks.dat from: 
http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
and replace the file: data/shape_predictor_68_face_landmarks.dat

Then use your own path replace the 'root' value in the *.py file,if there is a 'root'.
Do not forget add a '/' (not a '\') at the end of the path.
Just like this:
root = 'E:/Github/predict-facial-attractiveness/'

After that,follow the steps below:
 1.Run source/trainModel.py to generate the model which will be used to predict facial attractiveness later.
 2.Run source/getLandmarks.py to get the landmarks of the faces detected in the image/test.jpg.
 3.Run source/generateFeatures.py to generate the features,which will be as the input of the model we get before.
 4.Run source/myPredict.py to predict facial attractiveness.

Or you can just run the source/run.py alone.

