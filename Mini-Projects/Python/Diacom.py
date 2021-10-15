import pydicom as dicom
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

path = "./img"
ct_images = os.listdir(path)  # to list down content of directory


# we read file using dicom, s represent pile,then we impose force to preserve the path
slices = [dicom.read_file(path+'/'+s, force=True) for s in ct_images]
# now we have sliced the information
slices = sorted(slices, key=lambda x: x.ImagePositionPatient[2])
pixel_spacing = slices[0].PixelSpacing
slices_thickness = slices[0].SliceThickness

axial_aspect_ratio = pixel_spacing[1]/pixel_spacing[0]
sagital_aspect_ratio = pixel_spacing[1]/slices_thickness
coronal_aspect_ratio = slices_thickness/pixel_spacing[0]

img_shape = list(slices[0].pixel_array.shape)
img_shape.append(len(slices))
volume3d = np.zeros(img_shape)
print(img_shape)
# convert array to 2d pixel_array

for i, s in enumerate(slices):
    array2D = s.pixel_array
    volume3d[:, :, i] = array2D

axial = plt.subplot(2, 2, 1)
plt.title("AXIAL")
plt.imshow(volume3d[:, :, img_shape[2]//2])
axial.set_aspect(axial_aspect_ratio)

sagital = plt.subplot(2, 2, 2)
plt.title("SAGITAL")
plt.imshow(volume3d[:, img_shape[1]//2, :])
sagital.set_aspect(sagital_aspect_ratio)

coronal = plt.subplot(2, 2, 3)
plt.title("CORONAL")
plt.imshow(volume3d[img_shape[0]//2, :, :].T)
coronal.set_aspect(coronal_aspect_ratio)


def convert(directory):
    im = dicom.dcmread('./img/'+directory)
    im = im.pixel_array.astype(float)
    rescaled_image = (np.maximum(im, 0)/im.max()) * 255  # float pixel
    final_image = np.uint8(rescaled_image)  # integers pixels
    final_image = Image.fromarray(final_image)
    return final_image


arr_filename = [x for x in ct_images if x.endswith(".dcm")]
image = None
for name in arr_filename:
    image = convert(name)
    image.save('./JPG_IMG/'+name+'.jpg')

plt.show()
