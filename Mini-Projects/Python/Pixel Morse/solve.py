from PIL import Image
from morse import morsDecode
import sys

def extractOffset(pixel_array: list)-> str:
    a, b= [0, 0]
    out = []
    for i in pixel_array:
        if i:
            out.append(b - a+1)
            a = b
        else:
            b+=1
    return out

def asciiExtractor(pixel_offsets: str)-> list:
    out = []
    for offset in pixel_offsets:
        out.append(chr(offset))
    return out

def solve(main):
    main_image = Image.open(main, 'r')
    pixels = list(main_image.getdata())
    pixel_offsets = extractOffset(pixels)
    print("{0} \n".format(pixel_offsets))
    char_values = asciiExtractor(pixel_offsets)
    print("{0} \n".format(char_values))
    char_values = "".join(char_values).split("/")
    print(char_values)
    mors_text = "".join(char_values).strip().split()
    real = morsDecode(mors_text)
    #print("PIXEL OFFSETS: {0}\nCHAR VALUES: {1}\nMORS TEXT: {2}\nREAL: {3}".format(pixel_offsets, char_values, mors_text, real))

    


if __name__ == '__main__':
    solve(sys.argv[1])


