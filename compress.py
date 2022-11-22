import PIL
from PIL import Image

mywidth = 640

img = Image.open('C:/Users/sai/Desktop/orignal.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('C:/Users/sai/Desktop/compressed.jpg')




# C:\Users\sai\Downloads\image12