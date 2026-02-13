from PIL import Image

kernal_edge = [[-1,-1,-1],[-1, 8,-1],[-1,-1,-1]]

def defineEdge(imgname):
    img = Image.open(imgname)
    new_img = img.copy()
    x = 0
    (width, height) = img.size
    while x < width - 2:
        y = 0
        while y < height - 2:
            pixel_coords = getCoords(x,y)
            setPixel(img, pixel_coords, new_img, kernal_edge)
            y += 1
        x += 1
    new_img.show()

def getCoords(x, y):
    coords = []
    for x1 in range(3):
        coords.append([])
        x1 += 1
        for y1 in range(3):
            coords[x1-1].append([x+x1-1,y+y1-1])
            y1 += 1
    return coords

def setPixel(img, pixel_coords, new_img, kernal):
    pixels = getPixels(img, pixel_coords)
    new_p = pixels[1][1] * kernal[0][0]
    for x in range(3):
        for y in range(3):
            if x != 1 and y != 1:
                new_p += pixels[x][y] * kernal[-x][-y]
    if new_p < 0:
        new_p = 0
    elif new_p > 255:
        new_p = 255
    new_p = (new_p, new_p, new_p)
    new_img.putpixel(((pixel_coords[1][1][0], pixel_coords[1][1][1])), new_p)


def getPixels(img, pixel_coords):
    pixels = []
    for x in range(3):
        pixels.append([])
        for y in range(3):
            pixels[x].append(img.getpixel((pixel_coords[x][y][0], pixel_coords[x][y][1]))[0])
    return pixels 

if __name__ == '__main__':
    defineEdge(r'C:\Users\Colin\OneDrive\Documents\GitHub\ComputerScienceII\spring-2026\assignments\pair\p1\rose.jpg')