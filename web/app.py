"""
Tong Guan's Flask API.
"""
import os
import configparser
from flask import Flask, abort, send_from_directory

def parse_config(config_paths):
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break

    if config_path is None:
        raise RuntimeError("Configuration file not found!")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config

config = parse_config(["credentials.ini", "default.ini"])
port = config["SERVER"]["PORT"]

app = Flask(__name__)

@app.route("/<path:name>")
def index(name):
    path = './pages/' + name
    if ".." in name or "~" in name:
        abort(403)
    elif os.path.exists(path):
        return send_from_directory('pages/', name), 200
    else:
        abort(404)


@app.errorhandler(403)
def forbidden(e):
   return send_from_directory('pages/', '403.html'), 403

@app.errorhandler(404)
def file_not_found(e):
   return send_from_directory('pages/', '404.html'), 404

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=port)

