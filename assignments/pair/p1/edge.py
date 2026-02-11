from PIL import Image

kernal_edge = [
    [-1,-1,-1],
    [-1, 8,-1],
    [-1,-1,-1]
]

if __name__ == '__defineEdge__':
    defineEdge('llama.jpg', kernal_edge)

def defineEdge(imgname, kernal):
    img = Image.open(imgname)
    new_img = img.copy()
    x, y = 0, 0
    (width, height) = img.size()
    while x < width:
        while y < height:
            pixel_coords = getCoords(x,y)
            setPixel(img, pixel_coords, new_img, kernal)
            y += 1
        x += 1
    new_img.show()

def getCoords(x, y):
    coords = []
    for x in range(3):
        coords.append([])
        for y in range(3):
            coords[x].append([x,y])
    return coords

def setPixel(img, pixel_coords, new_img, kernal):
    pixels = getPixels(img, pixel_coords)
    new_p = pixels[1][1] * kernal[1][1]
    for x in range(3):
        for y in range(3):
            if x != 1 and y != 1:
                new_p += pixels[x][y] * kernal[-x][-y]
    new_img.putpixel((pixel_coords[1][1][0], pixel_coords[1][1][1]), new_p)


def getPixels(img, pixel_coords):
    pixels = []
    for x in range(3):
        pixels.append([])
        for y in range(3):
            pixels[x].append(img.getpixel(pixel_coords[x][y])[0])
    return pixels 