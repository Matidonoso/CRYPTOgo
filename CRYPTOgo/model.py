import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt


def prediction( series ):
    new_model = tf.keras.models.load_model('model.h5')
    
    #Evaluate this model
    #loss, acc = model.evaluate(test_images,  test_labels, verbose=2)
    #print("Restored model, accuracy: {:5.2f}%".format(100*acc))

    prediction = new_model.predict(series)
    
    return prediction