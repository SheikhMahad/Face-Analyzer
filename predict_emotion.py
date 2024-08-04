import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np

model = load_model('model/emotion_model.h5')

EMOTIONS = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']


def predict_emotion(img_path):
    # Load image with target size and grayscale mode
    img = image.load_img(img_path, target_size=(48, 48), color_mode='grayscale')
    img_array = image.img_to_array(img)

    # Normalize the image array
    img_array /= 255.0

    # Expand dimensions to match the input shape expected by the model
    img_array = np.expand_dims(img_array, axis=0)

    # Predict the emotion
    predictions = model.predict(img_array)
    emotion = EMOTIONS[np.argmax(predictions)]

    return emotion
