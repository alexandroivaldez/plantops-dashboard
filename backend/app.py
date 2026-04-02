from flask import Flask, request, jsonify

app = Flask(__name__)

plant_data = [] # temp

@app.route('/api/sensor-data', methods=['POST'])
def receive_sensor_data():
    data = request.json
    plant_data.append(data)
    return jsonify({"status": "received"}), 200

@app.route('/api/plants', methods=['GET'])
def get_plants():
    return jsonify(plant_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)