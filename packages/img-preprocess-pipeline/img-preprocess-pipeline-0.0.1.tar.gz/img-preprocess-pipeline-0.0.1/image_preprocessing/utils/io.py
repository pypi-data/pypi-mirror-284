import tensorflow as tf
import numpy as np

def load_image(path,grayscale=False):


    img_tf = tf.keras.utils.load_img(path)

    if grayscale:
        title = 'Original Grayscale'
        img_tf = tf.image.rgb_to_grayscale(img_tf)
    else:
        title = 'Original'
    
    img_loaded = {title:img_tf}
    return img_loaded

def save_image(image,path):
    try:
        image = list(image.values())[0]
    except:
        pass
    
    image_array = np.array(image)
    tf.keras.utils.save_img(
    path, image_array)

    print('Image saved!')
