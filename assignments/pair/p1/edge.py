from PIL import Image

def main(imgname):
    img = Image.open(imgname)
    new_img = img.copy()
    x, y = 2, 2
    (width, height) = img.size()
    pixel_coords = [[x-2, y-2],[x,y]]
    while x < width:
        while y < height:
            setpixels(img, pixel_coords, new_img)
            y += 1
        x += 1


def setPixels(img, pixel_coords, new_img):


def getPixels(img, pixel_coords):