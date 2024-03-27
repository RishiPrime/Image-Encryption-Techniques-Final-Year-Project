from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['image']
    save_path = "DECRYPT/enc.jpg"
    uploaded_file.save(save_path)
    return "Image uploaded successfully!"

if __name__ == '__main__':
    # Use 0.0.0.0 to listen on all available interfaces
    app.run(host='0.0.0.0', port=5555)