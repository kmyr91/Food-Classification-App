import os
import sys
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import tensorflow as tf
import numpy as np
from PIL import Image
import tensorflow_datasets as tfds

# Load the model
model = tf.keras.models.load_model('models/model')
print('Script started')

def preprocess(image_path):
    image = Image.open(image_path)
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)  # Add an extra dimension for the batch
    return image

def predict(image_path):
    image = preprocess(image_path)
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction)
    class_names = tfds.builder('food101').info.features['label'].names

    predicted_class_name = class_names[predicted_class]
    with open('prediction.txt', 'w') as f:
        f.write(f'Predicted food: {predicted_class_name}')

    return predicted_class

# Get the image path from command line arguments and predict
image_path = sys.argv[1]
predict(image_path)
print('Script finished')
