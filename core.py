# import matplotlib.pyplot as plt
import PIL
from PIL import Image
import os
import tensorflow as tf
from keras.callbacks import ModelCheckpoint
from keras.models import Sequential,load_model
from keras.layers import Dense, Activation, Dropout, Flatten,Conv2D, MaxPooling2D,BatchNormalization
import numpy as np
from random import shuffle
from database import *
import pickle

MODEL_NAME = "tomato"

MODEL_PATH = "models/"

model_id = None
def load_image(filepath,size):
	img = Image.open(filepath)
	img = img.resize(size)
	img = np.array(img)
	img = img /255
	return img

def load_data_set(input):
	def create_output_set(i,n):
		k = np.zeros(n)
		k[i] = 1
		return k
	labels = []
	dataset = {}
	rootdir = "Data"
	for subdir, dirs, files in os.walk(rootdir):
		for dir in dirs:
			if dir not in dataset.keys():
				dataset[dir] = []
			labels.append(dir)
			exp_dir = os.path.join(rootdir,dir)
			for filename in os.listdir(exp_dir):
				filepath = os.path.join(exp_dir,filename)
				dataset[dir].append(load_image(filepath,input))

	for label in labels:
		q = "insert into label(label,model_id)values('%s','%s')" % (label,model_id)
		insert(q)

	Y_set = []
	X_set = []
	prediction_set = {}
	for label in labels:
		prediction_set[label] = np.argmax(create_output_set(labels.index(label),len(labels)))
		for image in  dataset[label]:
			Y_set.append(create_output_set(labels.index(label),len(labels)))
			X_set.append(image)
	Y_set_shuffled = []
	X_set_shuffled = []
	randomize = np.arange(len(X_set))
	np.random.shuffle(randomize)
	for i in randomize:
		Y_set_shuffled.append(Y_set[i])
		X_set_shuffled.append(X_set[i])
	Y_set = Y_set_shuffled
	X_set = X_set_shuffled
	X_train = np.array(X_set[0:500])
	Y_train = np.array(Y_set[0:500])
	X_test = np.array(X_set[500:])
	Y_test = np.array(Y_set[500:])
	# # print(prediction_set)
	data = (X_train,Y_train),(X_test,Y_test)
	# file = open('dataset.pickle',"wb")
	file = open('testdataset.pickle',"wb")
	pickle.dump(data,file)
	file.close()

def load_data_set_pickle():
	file = open('testdataset.pickle',"rb")
	data = pickle.load(file)
	return data[0],data[1]

def create_model():
	model = Sequential()
	# 1st Convolutional Layer
	model.add(Conv2D(filters=96, input_shape=(224,224,3), kernel_size=(11,11),\
	 strides=(4,4), padding='valid'))
	model.add(Activation('relu'))
	# Pooling 
	model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid'))
	# Batch Normalisation before passing it to the next layer
	model.add(BatchNormalization())

	# 2nd Convolutional Layer
	model.add(Conv2D(filters=256, kernel_size=(11,11), strides=(1,1), padding='valid'))
	model.add(Activation('relu'))
	# Pooling
	model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid'))
	# Batch Normalisation
	model.add(BatchNormalization())

	# 3rd Convolutional Layer
	model.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='valid'))
	model.add(Activation('relu'))
	# Batch Normalisation
	model.add(BatchNormalization())

	# 4th Convolutional Layer
	model.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='valid'))
	model.add(Activation('relu'))
	# Batch Normalisation
	model.add(BatchNormalization())

	# 5th Convolutional Layer
	model.add(Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding='valid'))
	model.add(Activation('relu'))
	# Pooling
	model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid'))
	# Batch Normalisation
	model.add(BatchNormalization())

	# Passing it to a dense layer
	model.add(Flatten())
	# 1st Dense Layer
	model.add(Dense(4096, input_shape=(224*224*3,)))
	model.add(Activation('relu'))
	# Add Dropout to prevent overfitting
	model.add(Dropout(0.4))
	# Batch Normalisation
	model.add(BatchNormalization())

	# 2nd Dense Layer
	model.add(Dense(4096))
	model.add(Activation('relu'))
	# Add Dropout
	model.add(Dropout(0.4))
	# Batch Normalisation
	model.add(BatchNormalization())

	# 3rd Dense Layer
	model.add(Dense(1000))
	model.add(Activation('relu'))
	# Add Dropout
	model.add(Dropout(0.4))
	# Batch Normalisation
	model.add(BatchNormalization())

	# Output Layer
	model.add(Dense(10))
	model.add(Activation('softmax'))

	model.compile(optimizer='adam',
				 loss='categorical_crossentropy',
				 metrics=['accuracy'])
	return model


if __name__ == '__main__':
	q = "INSERT INTO model (model_class,model_path)values('%s','%s')" % (MODEL_NAME,(MODEL_PATH + MODEL_NAME))
	model_id = insert(q)


	load_data_set((224,224))

	(X_train,Y_train),(X_test,Y_test) = load_data_set_pickle()

	# checkpoint
	# filepath="trained_models/weights-improvement-{epoch:02d}-{acc:.2f}.hdf5"
	filepath = MODEL_PATH + MODEL_NAME
	checkpoint = ModelCheckpoint(filepath, monitor='acc', verbose=1, save_best_only=True, mode='max')
	callbacks_list = [checkpoint]

	model = create_model()
	model.fit(X_train,Y_train,epochs=30,callbacks=callbacks_list,)
