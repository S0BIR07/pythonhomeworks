'''from PIL import Image
import numpy as np
with Image.open("images/birds.jpg") as img:
    img_arr=np.array(img)
    print(img.mode)'''

# Import required modules
from PIL import Image
import numpy as np

# Create a simple function that autosaves arrays as images to make life easier
def save_image(arr, name, mode):
    img = Image.fromarray(arr, mode)
    img.save(f"images/{name}.jpg")

# Make an array that represents the image
with Image.open('images/birds.jpg') as img:
    img_arr = np.array(img)


# Flip horizontally and vertically
def flip_image(array):
    flip_img = array[::-1, ::-1]
    return save_image(flip_img, "flip_img", "RGB") # save the image


def add_noise(array):
    # Generate random noise
    noise_arr = np.random.randint(0, 50, tuple(array.shape))
    # If the range of the array was 0 to 255, the noise intensity would be very high, so used lower range
    noise_img = np.clip(array + noise_arr, 0, 255).astype(np.uint8)
    return save_image(noise_img, "noise_img", "RGB")

def brighten_channels(array):
    # Increase the red channel by 40. Keep the range 0, 255
    brighten_arr = np.full(array.shape, [40, 0, 0], dtype=np.uint8) # array to add in order to brighten every red color of pixels
    bright_img = np.clip(img_arr+brighten_arr, 0, 255)
    return save_image(bright_img, "bright_img", "RGB")

# create a mask
def apply_mask(array):
    copy_arr = array.copy() # create a copy before changing the original array
    sub_arr = copy_arr[int(copy_arr.shape[0]/2-50):int(copy_arr.shape[0]/2+51), int(copy_arr.shape[1]/2-50):int(copy_arr.shape[1]/2+51)]
    sub_arr.fill(0) # fill with 0 to create black color
    return save_image(copy_arr, "mask_img", "RGB")

flip_image(img_arr)
add_noise(img_arr)
brighten_channels(img_arr)
apply_mask(img_arr)