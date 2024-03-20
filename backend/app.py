from flask import Flask, jsonify, request, url_for
from get_location import *
from get_real_time_data import *
from get_comment import *
from predict_image import *

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive():
    image_url = url_for('static', filename='Traffic_image.png') # replace filename with the image from api
    try:
        data = request.get_json()
        received_text = data.get('text', '') # input for api
        location = get_location_LLM(received_text)
        latitude, longitude = get_location_coordinate(location)
        camera_data = get_data()
        traffic_data = get_best_match(camera_data, latitude, longitude)
        # print(traffic_data)
        image = get_imgae_from_link(traffic_data)
        traffic_prediction = predict_image(image, classes=['Empty', 'High', 'Low', 'Medium', 'Traffic Jam'])
        result = sarcastic_comment(traffic_prediction) # replace with result string from api
    except Exception as e:
        print(e)
        return jsonify({'message': "I'm sorry, I don't understand. Think twice before you speak, human.", 'imageUrl': image_url})
    return jsonify({'message': result, 'imageUrl': image_url})

if __name__ == '__main__':
    app.run(debug=True)
