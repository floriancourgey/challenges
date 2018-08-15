#! /usr/bin/env python3
# coding: utf-8
import requests
from PIL import Image, ImageFilter
import config

pngSignature = b'\x89\x50\x4E\x47'

# offline
f = open('original/imgcrypted.png', 'rb')
bin_data = f.read()
# online
# r = requests.get('https://www.newbiecontest.org/epreuves/prog/prog11.php', cookies={'SMFCookie89':config.COOKIE})
# with open('results/file.png', "wb") as local_file:
#     local_file.write(r.content)
# split whole file by PNG signature
chunks = bin_data.split(pngSignature) # ['', file1, file2, file3]
if len(chunks) != 4:
    exit('wrong input file format')
del chunks[0] # remove first empty
# create the 3 files
for i,chunk in enumerate(chunks):
    with open("results/file"+str(i)+".png", "wb") as file:
        file.write(pngSignature)
        file.write(chunk)
master = Image.open("results/file0.png")
print('size(x,y)', master.size)
xMax = master.size[0]
yMax = master.size[1]
vertical = Image.open("results/file1.png")
horizontal = Image.open("results/file2.png")
# create output file, with the size of the master
output = Image.new('RGB', master.size)
output.save("results/output.png") # create black PNG file
pixels = output.load() # create the pixel map
# for each pixel(x,y) in master
for y in range(yMax):
    for x in range(xMax):
        r, g, b = master.getpixel((x,y))
        if r+g+b == 0:
            continue
        if r>0:
            # print('pixel found (x='+str(x)+',y='+str(y)+')', r, g, b)
            # horizontal offset first
            deltaY = horizontal.getpixel((x,0))[0]
            yNew = (y-deltaY)%yMax
            # then vertical offset
            deltaX = vertical.getpixel((0,yNew))[0]
            xNew = (x-deltaX)%xMax
            # write it
            # pixels[xNew,yNew] = (r, 0, 0)
            pixels[xNew,yNew] = (255, 255, 255)
    # break

output.save("results/output.png") # save pixels modification

output2 = output.resize((xMax*4, yMax*4))
output2.save("results/output2.png")
output3 = output2.filter(ImageFilter.GaussianBlur(1))
# output3 = output2.filter(ImageFilter.BLUR)
output3.save("results/output3.png")


# print(r,g,b)
# print(master.mode)
