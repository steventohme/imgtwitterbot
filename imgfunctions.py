from PIL import Image
from PIL import ImageEnhance
import urllib.request

# converts image to black and white
def bw(img):
    urllib.request.urlretrieve(img, 'img.jpg')
    image1 = Image.open("img.jpg")
    image1 = image1.convert('L')
    image1.save("img.jpg")
    
# changes the images charateristics to match that of pop culture style, deepfried.
def deepfried(img):
    urllib.request.urlretrieve(img, 'img.jpg')
    image1 = Image.open("img.jpg")
    enhancer_contrast = ImageEnhance.Contrast(image1)
    image1 = enhancer_contrast.enhance(10)
    enhancer_bright = ImageEnhance.Brightness(image1)
    image1 = enhancer_bright.enhance(5)
    enhancer_sharp = ImageEnhance.Sharpness(image1)
    image1 = enhancer_sharp.enhance(10)
    image1.save("img.jpg")
