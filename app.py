from flask import Flask , send_file , request, render_template, jsonify
from modules.app_manager import *
from modules.myGDrive import get_file_list
import requests
app = Flask(__name__)

@app.get("/")
def index():
    req = requests.get(request.host_url+"/api/list-audio")

    return render_template("index.html", data=req.json())
    # return render_template("index.html")
@app.get("/api/list-audio")
def list_file():
    return jsonify(get_file_list())

app.run(debug=True)