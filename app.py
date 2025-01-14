from flask import Flask, request, jsonify

app = Flask(__name__)

# Biến lưu trữ tin nhắn
messages = []

@app.route('/')
def home():
    return "Welcome to the Flask Message API!"


@app.route('/send', methods=['POST'])
def send_message():
    message = request.json.get('message')
    if message:
        messages.append(message)
        return jsonify({"status": "success"})
    return jsonify({"status": "failed"}), 400

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify({"messages": messages})
if __name__ == '__main__':
    app.run(debug=True)
