from flask import Flask, request, Blueprint, send_file
from service import remove_background
from io import BytesIO

app = Flask(__name__)
app.config.from_object(__name__)

image_background_remover = Blueprint('image_background_remover', __name__)

@app.route('/')
def status():  # put application's code here
    return {"status": "Online"}

@image_background_remover.route('/api/bg-remover', methods=['POST'])
def bg_rm():
    url = request.json['url']
    output = remove_background(url)
    bbyte = BytesIO(output)
    return send_file(bbyte,as_attachment=True, download_name='output.jpg')

app.register_blueprint(image_background_remover)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)