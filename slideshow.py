''' Adapted from vegaseat's Tkinter slideshow (published 03dec2013)
'''
from itertools import cycle
from PIL import Image, ImageTk
#import PIL.Image
#from PIL import ImageTk
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
#from tkinter import *

class App(tk.Tk):
    '''Tk window/label adjusts to size of image'''
    def __init__(self, image_files, x, y, delay):
        # the root will be self
        tk.Tk.__init__(self)
        # set x, y position only
        self.geometry('+{}+{}'.format(x, y))
        self.delay = delay
        # allows repeat cycling through the pictures
        # store as (img_object, img_name) tuple
        self.pictures = cycle((tk.PhotoImage(file=image), Image.open(image).resize((100,100)))
                              for image in image_files)
        self.picture_display = tk.Label(self)
        self.picture_display.pack()
    def show_slides(self):
        '''cycle through the images and show them'''
        # next works with Python26 or higher
        img_object, img_name = next(self.pictures)
        #self.resize((1000,100), Image.ANTIALIAS)
        self.picture_display.config(image=img_object)
        # shows the image filename, but could be expanded
        # to show an associated description of the image
        self.title(img_name)
        self.after(self.delay, self.show_slides)
    def run(self):
        self.mainloop()
# set milliseconds time between slides
delay = 2500
# get a series of gif images you have in the working folder
# or use full path, or set directory to where the images are
#for i in range (9):

image_files = ['/home/pi/OutfitRaspberryPi/imgsOut/pants11.png' ,'/home/pi/OutfitRaspberryPi/imgsOut/pants13.png' ,'/home/pi/OutfitRaspberryPi/imgsOut/pants16.png' ,'/home/pi/OutfitRaspberryPi/imgsOut/pants18.png' ,'/home/pi/OutfitRaspberryPi/imgsOut/pants19.png' ,'/home/pi/OutfitRaspberryPi/imgsOut/pants21.png' ,'/home/pi/OutfitRaspberryPi/imgsOut/pants30.png' ,'/home/pi/OutfitRaspberryPi/imgsOut/pants1.png', '/home/pi/OutfitRaspberryPi/imgsOut/pants23.png']

#images = ['/home/pi/OutfitRaspberryPi/imgsOut/pants11.png' ,'/home/pi/OutfitRaspberryPi/imgsOut/pants13.png' ,'/home/pi/OutfitRaspberryPi/imgsOut/pants16.png' ,'/home/pi/OutfitRaspberryPi/imgsOut/pants18.png' ,'/home/pi/OutfitRaspberryPi/imgsOut/pants19.png' ,'/home/pi/OutfitRaspberryPi/imgsOut/pants21.png' ,'/home/pi/OutfitRaspberryPi/imgsOut/pants30.png' ,'/home/pi/OutfitRaspberryPi/imgsOut/pants1.png','/home/pi/OutfitRaspberryPi/imgsOut/pants23.png']

"""
image_files = [None] * 9

for i in range (9):
	img = Image.open(images[i])
	image_files[i] = img.resize((500,500), Image.ANTIALIAS) #(height, width)
for i in range (9):

	image_files[i] = ImageTk.PhotoImage(Image.open(images[i]).resize((1000,1000), Image.ANTIALIAS))
"""
#what to do what to do maybe put the photo image stuff up there ^ down there? 
#image_files = [Image.open(images[0]).resize((1000,100), Image.ANTIALIAS), Image.open(images[1]).resize((1000,100), Image.ANTIALIAS), Image.open(images[2]).resize((1000,100), Image.ANTIALIAS), Image.open(images[3]).resize((1000,100), Image.ANTIALIAS), Image.open(images[4]).resize((1000,100), Image.ANTIALIAS), Image.open(images[5]).resize((1000,100), Image.ANTIALIAS), Image.open(images[6]).resize((1000,100), Image.ANTIALIAS), Image.open(images[7]).resize((1000,100), Image.ANTIALIAS), Image.open(images[8]).resize((1000,100), Image.ANTIALIAS)] 

# upper left corner coordinates of app window
#root = tk()
x = 100
y =  50
app = App(image_files, x, y, delay)
app.show_slides()
app.run()
