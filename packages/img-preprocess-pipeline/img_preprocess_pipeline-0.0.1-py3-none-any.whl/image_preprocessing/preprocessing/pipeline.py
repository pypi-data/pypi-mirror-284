import tensorflow as tf
import numpy as np

def preprocess_pipeline(image,width=224, height=224):

    try:
        image = list(image.values())[0]
    except:
        pass

    image_temp = image.copy()

    img_resized_tf = tf.image.resize(image_temp, [width, height],method='nearest')
    scaler = tf.keras.layers.Rescaling(1./255)
    scaled_image = scaler(img_resized_tf)

    new_image = tf.image.random_flip_left_right(scaled_image)
    new_image = tf.image.random_flip_up_down(new_image)
    new_image = tf.image.random_saturation(new_image, 5,10)
    new_image = tf.image.random_brightness(new_image, max_delta=0.1)
    
    new_image = np.array(new_image)

    title = 'Preprocessed'        

    return {title:new_image}
