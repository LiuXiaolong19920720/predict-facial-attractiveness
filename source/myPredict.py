from sklearn.externals import joblib
import numpy as np
from sklearn import decomposition

#use your own path
root = 'E:/face_rating/my_face_rating/'
clf = joblib.load(root+'model/my_face_rating.pkl')
features = np.loadtxt(root + 'data/features_ALL.txt', delimiter=',')
my_features = np.loadtxt(root + 'data/my_features.txt', delimiter=',')
pca = decomposition.PCA(n_components=20)
pca.fit(features)

predictions = np.zeros([6,1]);

for i in range(0, 6):
	features_test = features[i, :]
	features_test = pca.transform(features_test)
	#regr = linear_model.LinearRegression()
	#regr.fit(features_train, ratings_train)
	predictions[i] = clf.predict(features_test)
#predictions = clf.predict(features)
print predictions
