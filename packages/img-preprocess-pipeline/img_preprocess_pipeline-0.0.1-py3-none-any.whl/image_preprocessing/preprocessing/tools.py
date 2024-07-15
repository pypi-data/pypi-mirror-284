import tensorflow as tf
import numpy as np

def reshape_image(image,width=224,height=224):
    
    try:
        image = list(image.values())[0]
    except:
        pass
    
    title = 'Reshaped'

    img_resized_tf = tf.image.resize(image, [width, height],method='nearest')
    img_resize = {title:img_resized_tf}
    
    return img_resize

def scale_image(image):
    
    try:
        image = list(image.values())[0]
    except:
        pass
    
    title = 'Scaled'
    scaler = tf.keras.layers.Rescaling(1./255)
    img_scaled = {title:scaler(image)}
    return img_scaled

def random_augumentation(image):

    title = 'Augumented image'

    try:
        image = list(image.values())[0]
    except:
        pass
    
    new_image = tf.image.random_flip_left_right(image)
    new_image = tf.image.random_flip_up_down(new_image)
    new_image = tf.image.random_saturation(new_image, 5,10)
    new_image = tf.image.random_brightness(new_image, max_delta=0.1)
    
    new_image = np.array(new_image)

    return {title:new_image}

    
