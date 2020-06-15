from flask import Flask, json, json, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder='/static')
CORS(app)

@app.route('/')
def index():
    return 'Hola'

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
