from PIL import Image
from PIL import ImageEnhance
import urllib.request


def bw(img):
    urllib.request.urlretrieve(img, 'img.jpg')
    image1 = Image.open("img.jpg")
    image1 = image1.convert('L')
    image1.save("img.jpg")
    

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
