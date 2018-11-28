from PIL import Image
import sys

im = Image.open(sys.argv[1])

print('Picture format: ' + im.format)
print('Picture Matrix size: ' + str(im.size))
print('Picture mode: ' + im.mode)

row = im.size[0]
column = im.size[1]
print('Picture row: ' + str(row))
print('Picture column: ' + str(column))

def print_color_value():
    print('{')
    for i in range(row):
        for j in range(column):
            rgb = im.getpixel((i,j))
            color_data = (rgb[0]<<16) + (rgb[1]<<8) + rgb[2]
            if j == 0:
                print('\t{' + '0x%x'%color_data, end=', ')
            elif j == (column-1):
                print('0x%x'%color_data, end='},')
            else:
                print('0x%x'%color_data, end=', ')
        print();
    print('}')

def image_zoom():
    
print_color_value()

