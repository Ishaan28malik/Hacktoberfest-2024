import os
import sys
from PIL import Image

img_fold=sys.argv[1]
op_fold=sys.argv[2]

if not os.path.exists(op_fold):
	os.makedirs(op_fold)

for file in os.listdir(img_fold):
	img=Image.open(f'{img_fold}{file}')
	clean=os.path.splitext(file)[0]
	print(clean)
	img.save(f'{op_fold}{clean}.png','png')
	print("done!")