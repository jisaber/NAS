from flask import Flask
from flask import render_template
import os
import tool

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('hello.html')

@app.route("/hello/<name>")
def hello_world(name = None):
    current_directory = os.getcwd()  # 获取当前目录
    filenames = []
    for root, directories, files in os.walk(current_directory):
        for file in files:
            path = os.path.join(root, file)
            if tool.is_video_file(path):
                file = path.split("static")[-1]
                file = file[1:].replace("\\", "/")
                filenames.append(file)
    print(filenames)
    print(os.path.join(os.getcwd(), "static"))
    return render_template('hello.html', filenames=filenames, name=name)

@app.route("/play/<path:path>/")
def play(path):
    print(path)
    return render_template('play.html', zhu=path)