

import tensorflow as tf
import tensorflow_datasets as tfds

def preprocess(image, label):
    image = tf.image.resize(image, [224, 224])
    image = image / 255.0
    return image, label

# Load the data
data, info = tfds.load('food101', as_supervised=True, with_info=True)

# Select a subset of data
n_data = int(len(data['train'])) # This is an arbitrary number, adjust it according to your needs
data = {k: v.take(n_data) for k, v in data.items()}
print("size of data:",len(data['train']))
train_data = data['train'].map(preprocess).batch(32)

# Define the model
base_model = tf.keras.applications.ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(info.features['label'].num_classes, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_data, epochs=10)

# Save the model
model.save('models/model')