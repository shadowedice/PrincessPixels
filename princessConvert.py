from PIL import Image

outFile = open("out.txt", "w")
im = Image.open("C:\\tmp\\Tiana.png")
pix = im.load()
for y in range(16):
    outFile.write('\n')
    for x in range(16):
	    if (y%2 == 0):
		    outFile.write(str(pix[15-x,y][0]) + ',' + str(pix[15-x,y][1]) + ',' + str(pix[15-x,y][2]) + ',')
	    else:
		    outFile.write(str(pix[x,y][0]) + ',' + str(pix[x,y][1]) + ',' + str(pix[x,y][2]) + ',')
	    #if (y%2 == 0):
		#    outFile.write('0x%02x%02x%02x' % pix[15-x,y][:3] + ',')
	    #else:
		#    outFile.write('0x%02x%02x%02x' % pix[x,y][:3] + ',')