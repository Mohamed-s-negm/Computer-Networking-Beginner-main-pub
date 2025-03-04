from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the light threshold
LIGHT_THRESHOLD = 300  # Adjust based on your sensor

@app.route('/light', methods=['POST'])
def check_light():
    data = request.get_json()  # Receive data from Raspberry Pi
    light_level = data.get("light")  # Extract light level
    
    if light_level is None:
        return jsonify({"error": "No light data received"}), 400

    if light_level < LIGHT_THRESHOLD:
        return jsonify({"led": "ON"})  # Tell client to turn on LED
    else:
        return jsonify({"led": "OFF"})  # No need for LED

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Accessible in local network
