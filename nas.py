from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
import os
import tool
import time
import datetime
 
app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/media")
def hello_world(name = None):
    current_directory = os.getcwd() + "\\static\\"  # 获取当前目录
    print(current_directory)
    filenames = []
    for root, directories, files in os.walk(current_directory):
        for file in files:
            path = os.path.join(root, file)
            size = tool.human_size(os.path.getsize(path))
            time = datetime.datetime.fromtimestamp(os.path.getctime(path)).strftime("%Y-%m-%d")
            print("===================1", )
            print(file)
            file = path.split(os.getcwd())[-1]
            print("===================2")
            print(file)
            file = file[1:].replace("\\", "/")
            
            filetype = tool.get_file_type(path)
            if filetype != tool.FILR_TYPE_ERROR:
                filenames.append([file, size, time, tool.get_file_type(path)])
    print("===================3")
    print(filenames)
    print(os.path.join(os.getcwd(), "static"))
    return render_template('index.html', filenames=filenames, name=name)

@app.route("/play/<path:path>/")
def play(path):
    print(path)
    return render_template('play.html', mediafile=path, filetype=tool.get_file_type(path))

@app.route("/about")
def about():
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')