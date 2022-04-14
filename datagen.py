import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img

image = load_img("/home/mbillah/Documents/12_1_162_34.jpg")
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

aug = ImageDataGenerator(rotation_range=30,
                         zoom_range=0.15,
                         width_shift_range=0.2,
                         height_shift_range=0.2,
                         shear_range=0.15,
                         horizontal_flip=True,
                         fill_mode="nearest",
                         )

total = 0

imageGen = aug.flow(image, batch_size=1, save_to_dir="/home/mbillah/Documents/stdtest", save_prefix="image", save_format="jpg")
for image in imageGen:
    total += 1
    if total == 100:
        break
