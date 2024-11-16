from flask import Flask, send_from_directory
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
    current_directory = os.getcwd() + "\\source\\"  # 获取当前目录
    print(current_directory)
    filenames = []
    for root, directories, files in os.walk(current_directory):
        for file in files:
            path = os.path.join(root, file)
            size = tool.human_size(os.path.getsize(path))
            time = datetime.datetime.fromtimestamp(os.path.getctime(path)).strftime("%Y-%m-%d")

            file = path.split(os.getcwd())[-1]
            file = file[1:].replace("\\", "/")
            filetype = tool.get_file_type(path)
            if filetype != tool.FILR_TYPE_ERROR:
                filenames.append([file, size, time, tool.get_file_type(path)])
    return render_template('index.html', filenames=filenames, name=name)

@app.route("/play/<path:path>/")
def play(path):
    print(path)
    return render_template('play.html', mediafile=path, filetype=tool.get_file_type(path))

@app.route("/about")
def about():
    import psutil
 
    # 获取CPU的使用率，以百分比表示
    cpu_usage_percent = psutil.cpu_percent(interval=1)
    print(f"当前CPU使用率: {cpu_usage_percent}%")
    print(psutil.cpu_count())
    print(psutil.cpu_count(logical=False))
    import platform
    
    print(platform.architecture(),platform.uname())

    mem = psutil.virtual_memory()
    print(tool.human_size(mem.total))
    print(tool.human_size(mem.used))
    print(tool.human_size(mem.free))
    print(format(mem.used / mem.total * 100, '.2f') + "%")
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/source/<path:filename>')
def sendfile(filename):
    return send_from_directory('source', filename)