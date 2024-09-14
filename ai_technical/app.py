from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from transformers import CLIPProcessor, TFCLIPModel
from PIL import Image
import requests
from io import BytesIO

app = Flask(__name__)

# Load the model
model = TFCLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        image_url = data.get('image_url')

        # Fetch the image
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))

        # Preprocess the image
        inputs = processor(text=["a photo of a cat", "a photo of a dog"], images=img, return_tensors="tf", padding=True)

        # Perform prediction
        outputs = model(**inputs)
        logits_per_image = outputs.logits_per_image
        probs = tf.nn.softmax(logits_per_image, axis=1)

        # Get probabilities
        cat_prob = probs[0][0].numpy()
        dog_prob = probs[0][1].numpy()

        # Return the results as JSON
        return jsonify({
            'predictions': {
                'cat_probability': float(cat_prob),
                'dog_probability': float(dog_prob)
            },
            'status': 'success'
        })
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'failed'}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


# Example Links to be used:
# http://images.cocodataset.org/val2017/000000039769.jpg
# https://img.freepik.com/free-photo/adorable-black-white-kitty-with-monochrome-wall-her_23-2148955182.jpg?size=626&ext=jpg&ga=GA1.1.1929702747.1726036465&semt=ais_hybrid
# https://img.freepik.com/free-photo/cute-cat-sitting-chair_23-2148882589.jpg?size=626&ext=jpg&ga=GA1.1.1929702747.1726036465&semt=ais_hybrid
# https://img.freepik.com/free-photo/front-view-poodle-with-tongue-out_23-2148643170.jpg?ga=GA1.1.1929702747.1726036465&semt=ais_hybrid
# https://images.unsplash.com/photo-1518815068914-038920b6f0c6?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8fA%3D%3D