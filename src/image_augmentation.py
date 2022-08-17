from numpy import expand_dims
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
from PIL import Image, ImageOps
import os

path = "/Users/apoorvareddy/Desktop/data/val/"
dirs = os.listdir(path)
ext = ['jpg','png']


def flipimage(item):
	im = Image.open(path+item)
	im_flip = ImageOps.flip(im)
	im_flip.save(path+item[:-4]+"_1.png", quality=95)

def mirrorimg(item):
	im = Image.open(path+item)
	im_mirror = ImageOps.mirror(im)
	im_mirror.save(path+item[:-4]+"_2.png", quality=95)

def rotateimg(item):
	im = Image.open(path+item)
	im_rotate = im.rotate(90)
	im_rotate.save(path+item[:-4]+"_3.png", quality=95)

for item in dirs:
	if item[-3:] in ext:
		if os.path.isfile(path+item):
			f,e = os.path.splitext(path+item)  
			flipimage(item)
			mirrorimg(item)
			rotateimg(item)

