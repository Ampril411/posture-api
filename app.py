from flask import Flask, request, jsonify
from posture_analysis import analyze_posture
from utils import read_image_from_bytes

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    image = read_image_from_bytes(file.read())
    result = analyze_posture(image)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
