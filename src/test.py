import tensorflow as tf
from tensorflow.keras.preprocessing import image as img_prep
import numpy as np
import tensorflow_datasets as tfds

# Load the trained model
model = tf.keras.models.load_model('models/model')

def preprocess_and_predict(image_path):
    # Load the image file
    img = img_prep.load_img(image_path, target_size=(224, 224))

    # Convert the image to a numpy array
    x = img_prep.img_to_array(img)

    # Normalize the image
    x = x / 255.0

    # Add a fourth dimension for batch size
    x = np.expand_dims(x, axis=0)

    # Use the model to make a prediction
    preds = model.predict(x)

    # Output the category with the highest probability
    predicted_class = tf.argmax(preds, axis=1).numpy()[0]
    class_names = tfds.builder('food101').info.features['label'].names
    predicted_class_name = class_names[predicted_class]
    print('Predicted food:', predicted_class_name)

# Test the model on an image file
preprocess_and_predict('image_test/image.jpeg')
