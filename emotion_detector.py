from flask import Flask, jsonify, request
from flask_cors import CORS
from predict_emotion import predict_emotion
import requests
import os

app = Flask(__name__)
CORS(app)

DEEZER_API_URL = 'http://api.deezer.com/search?q={emotion}&limit=10'

@app.route('/predict-emotion', methods=['POST'])
def predict_emotion_route():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        file_path = os.path.join('./uploads', file.filename)
        file.save(file_path)

        emotion = predict_emotion(file_path)
        os.remove(file_path)

        return jsonify({'emotion': emotion})

@app.route('/suggest-song', methods=['GET'])
def suggest_song():
    emotion = request.args.get('emotion')
    if emotion:
        response = requests.get(DEEZER_API_URL.format(emotion=emotion))
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and len(data['data']) > 0:
                songs = data['data']
                return jsonify({'songs': songs})
            else:
                return jsonify({'message': 'No songs found for this emotion.'}), 404
        else:
            return jsonify(
                {'message': 'Failed to fetch songs.', 'status_code': response.status_code}), response.status_code
    else:
        return jsonify({'message': 'Emotion parameter is missing.'}), 400

if __name__ == '__main__':
    if not os.path.exists('./uploads'):
        os.makedirs('./uploads')
    app.run(debug=True)
