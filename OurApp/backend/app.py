from flask import Flask, jsonify, request, url_for

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive():
    data = request.get_json()
    received_text = data.get('text', '') # input for api
    # call api function here
    # save the traffic image in folder 'backend/static/'
    result = "Traffic Jam" # replace with result string from api
    image_url = url_for('static', filename='Traffic_image.png') # replace filename with the image from api
    return jsonify({'message': result, 'imageUrl': image_url})

if __name__ == '__main__':
    app.run(debug=True)
