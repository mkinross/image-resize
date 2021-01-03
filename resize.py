
#!/usr/bin/python
from PIL import Image, ImageOps
import os, sys

# change path below to point to the folder containing your images
path = "C:/Users/user/Pictures/resize/images/"

dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)

            # some digital cameras only take pictures in landscape mode
            # the line below uses an API to access the meta information to check if an image is supposed be shown in portrait mode
            im = ImageOps.exif_transpose(im)

            # the lines below create a new folder for your resized images
            newpath = path + "web/"
            if not os.path.exists(newpath):
                os.makedirs(newpath)

            f, e = os.path.splitext(path+"web/"+item)

            width, height = im.size
            print(width, height)
            print(item)
            #print("width is " + str(width))
            #print("height is " + str(height))

            # resize according to image orientation
            if (width > height):
                print("landscape")
                imResize = im.resize((3264,2448), Image.ANTIALIAS)
                imResize.save(f + '.jpg', 'JPEG', quality=90)
            elif (width < height):
                print("portrait")
                imResize = im.resize((2448,3264), Image.ANTIALIAS)
                imResize.save(f + '.jpg', 'JPEG', quality=90)
            else:
                print("square")
                imResize = im.resize((2448,2448), Image.ANTIALIAS)
                imResize.save(f + '.jpg', 'JPEG', quality=90)

resize()
