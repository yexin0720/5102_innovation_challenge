from flask import Flask, jsonify, request, url_for
from get_location import *
from get_real_time_data import *
from get_comment import *
from predict_image import *

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive():
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
    # call api function here
    # save the traffic image in folder 'backend/static/'
    # result = "Empty roads, you say? What a plot twist! This is your moment to pretend you're the main character in a post-apocalyptic movie, where the streets are yours and yours alone. Just remember, the only things chasing you are deadlines and perhaps a squirrel or two. Enjoy the cinematic freedom—just don't get too used to it. Reality tends to reboot with traffic at the most inconvenient times." # replace with result string from api
    image_url = url_for('static', filename='Traffic_image.png') # replace filename with the image from api
    return jsonify({'message': result, 'imageUrl': image_url})

if __name__ == '__main__':
    app.run(debug=True)
