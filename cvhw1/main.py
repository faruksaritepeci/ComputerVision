from PIL.Image import Image as ImageType
from PIL import Image
import numpy as np

from utils import image_to_array, array_to_image, render_question_1


input_image = Image.open("images/webbJamesImage.jpeg")


print("start!")
def gray_scale_i(image: ImageType) -> ImageType:
    imageArray = np.asarray(image)
    newImage = np.uint8( imageArray[:, :, 0]/3 + imageArray[:, :, 1]/3 + imageArray[:, :, 2]/3 )
    return Image.fromarray(newImage)


def gray_scale_ii(image: ImageType) -> ImageType:
    imageArray = np.asarray(image)
    newImage = np.uint8( imageArray[:, :, 0]*0.114 + imageArray[:, :, 1]*0.587 + imageArray[:, :, 2]*0.299 )
    return Image.fromarray(newImage)


gray_image_i = gray_scale_i(input_image)
gray_image_ii = gray_scale_ii(input_image)

render_question_1(gray_image_i, gray_image_ii)