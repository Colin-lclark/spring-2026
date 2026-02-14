'''Authors: Colin Sheehan, Lazar Lukac''' 

from PIL import Image

kernal_edge = [[-1,-1,-1],[-1, 8,-1],[-1,-1,-1]]

def defineEdge(imgname, kernal):
    """Get the input image and kernal, create a new image, and sequentially 
    set each pixel to a new value based on edge detection."""
    img = Image.open(imgname)
    new_img = img.copy()
    x = 0
    (width, height) = img.size
    while x < width - 2:
        y = 0
        while y < height - 2:
            pixel_coords = (x,y)
            setEdge(img, pixel_coords, new_img, kernal)
            y += 1
        x += 1
    new_img.show()

def setEdge(img, pixel_coords, new_img, kernal):
    """Get list of three by three pixels and set the center pixel to a new value based on the kernal."""
    pixels = getPixelList(img, pixel_coords)
    new_p = 0
    for x in range(3):
        for y in range(3):
            new_p += pixels[x][y] * kernal[x][y]
    if new_p < 0:
        new_p = 0
    elif new_p > 255:
        new_p = 255
    new_p = (new_p, new_p, new_p)
    new_img.putpixel(((pixel_coords[0] + 1, pixel_coords[1] + 1)), new_p)


def getPixelList(img, pixel_coords):
    """Get a list of 3x3 pixel coordinates based on the top left pixel coordinate in img."""
    pixels = []
    for x in range(3):
        pixels.append([])
        for y in range(3):
            pixels[x].append(img.getpixel((pixel_coords[0]+x, pixel_coords[1]+y))[0])
    return pixels 

if __name__ == '__main__':
    defineEdge(r'rose.jpg', kernal_edge)