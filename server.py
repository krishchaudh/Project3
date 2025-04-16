from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from io import BytesIO
from PIL import Image

app = Flask(__name__)
model = load_model("lenet_best.keras")

def preprocess(img_bytes):
    img = Image.open(BytesIO(img_bytes)).convert("RGB")
    img = img.resize((128, 128))
    img_array = image.img_to_array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

@app.route("/summary", methods=["GET"])
def summary():
    model_metadata = {
        "model": "LeNet-5",
        "input_shape": list(model.input_shape[1:]),
        "output_shape": list(model.output_shape[1:]),
        "total_params": model.count_params()
    }
    return jsonify(model_metadata)

@app.route("/inference", methods=["POST"])
def inference():
    try:
        img_bytes = request.get_data()
        img_array = preprocess(img_bytes)
        prediction = model.predict(img_array)
        label = "damage" if prediction[0][0] > 0.5 else "no_damage"
        return jsonify({"prediction": label})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
